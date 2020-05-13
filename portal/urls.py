"""Portal URL Configuration
"""
from django.contrib import admin
from django.urls import include,path,re_path
from portal.views import PortalView
urlpatterns = [
    path('',PortalView.as_view()),
]
