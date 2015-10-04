from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from market.service import getitems, getmyitems


def login(request):
    c = {}
    # To avoid CSRF attack
    # keep CSRF token in UI files
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    # Using Default Authentication provided by Django (Checked against User_Auth table)
    user = authenticate(username=username, password=password)

    if user is not None:
        # To avoid cyclic dependency imported login as different alias
        auth_login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


@login_required(login_url='/accounts/login/')
# Annotation to make sure that User is already logged in, to call method
def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username, 'all_items': getitems(),
                               'my_items': getmyitems(request.user.username)})


@login_required(login_url='/accounts/login/')
def invalid_login(request):
    return render_to_response('invalid_login.html')


@login_required(login_url='/accounts/login/')
def logout(request):
    # To avoid cyclic dependency imported logout as different alias
    auth_logout(request)
    return render_to_response('logout.html')
