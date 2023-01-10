from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.home, name="home"),
    path('index/', views.index, name="dashboard"),
    path("manage/", views.manage, name="manage"),
    path("feed/", views.feed, name="feed"),
    path("scan_info/", views.scan_info, name="scan_info"),
    path("about/", views.about, name="about"),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls'))
    #path("register", views.register_request, name="register"),
    #path("postsign/", views.postsign, name="postsign")
    #path("logout/", views.logout_request, name="logout")
]
