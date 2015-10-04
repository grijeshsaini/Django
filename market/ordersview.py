from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
__author__ = 'grijesh'


def doorder(request):
    # todo functionality is pending
    return HttpResponseRedirect('/accounts/loggedin')