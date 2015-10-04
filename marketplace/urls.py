"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # user auth Urls
    # https://regex101.com/ - Good website to play with regular expression
    url(r'^accounts/$', 'market.views.login'),
    url(r'^accounts/login/$', 'market.views.login'),
    url(r'^accounts/auth/$', 'market.views.auth_view'),
    url(r'^accounts/logout/$', 'market.views.logout'),
    url(r'^accounts/loggedin/$', 'market.views.loggedin'),
    url(r'^accounts/invalid/$', 'market.views.invalid_login'),
    url(r'^accounts/order/$', 'market.ordersview.doorder'),
]
