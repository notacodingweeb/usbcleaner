from django.shortcuts import render, redirect
import pyrebase
from django.contrib import auth
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import requests
from rest_framework.decorators import api_view
from rest_framework import status, response
from .serializers import FileSerializer
from .models import FileModel

#initializing firebase
config = {
    "apiKey": "AIzaSyAKQloozcqTPOuu98FbCghNgt2ealdj92U",
    "authDomain": "usbcleaner-fyp.firebaseapp.com",
    "databaseURL": "https://usbcleaner-fyp-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "usbcleaner-fyp",
    "storageBucket": "usbcleaner-fyp.appspot.com",
    "messagingSenderId": "758068223239",
    "appId": "1:758068223239:web:ec57a9d7c63cf3d18af9a2",
    "measurementId": "G-W1TQVQJQ0L"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Create your views here.

def index(request):
    filepath = db.child('scan_result').child('filepath').get().val()
    filesize = db.child('scan_result').child('filesize').get().val()
    filetype = db.child('scan_result').child('filetype').get().val()
    hashstring = db.child('scan_result').child('hashstring').get().val()
    fbstring = db.child('scan_result').child('fbstring').get().val()
    fileAge = db.child('scan_result').child('fileAge').get().val()
    total_score = db.child('scan_result').child('total_score').get().val()
    message_type = db.child('scan_result').child('message_type').get().val()
    scan_time = db.child('scan_info').child('scan_time').get().val()
    site_name = db.child('scan_info').child('site_name').get().val()
    uid = db.child('scan_info').child('uid').get().val()

    context = {
        'filepath': filepath,
        'filesize': filesize,
        'filetype': filetype,
        'hashstring': hashstring,
        'fbstring': fbstring,
        'fileAge': fileAge,
        'total_score': total_score,
        'message_type': message_type,
        'scan_time': scan_time,
        'site_name': site_name,
        'UID': uid,

    }

    return render(request, "home.html", context)



def home(request):
    filepath = db.child('scan_result').child('filepath').get().val()
    filesize = db.child('scan_result').child('filesize').get().val()
    filetype = db.child('scan_result').child('filetype').get().val()
    hashstring = db.child('scan_result').child('hashstring').get().val()
    fbstring = db.child('scan_result').child('fbstring').get().val()
    fileAge = db.child('scan_result').child('fileAge').get().val()
    total_score = db.child('scan_result').child('total_score').get().val()
    message_type = db.child('scan_result').child('message_type').get().val()
    scan_time = db.child('scan_info').child('scan_time').get().val()
    site_name = db.child('scan_info').child('site_name').get().val()
    uid = db.child('scan_info').child('uid').get().val()

    context = {
        'filepath': filepath,
        'filesize': filesize,
        'filetype': filetype,
        'hashstring': hashstring,
        'fbstring': fbstring,
        'fileAge': fileAge,
        'total_score': total_score,
        'message_type': message_type,
        'scan_time': scan_time,
        'site_name': site_name,
        'UID': uid,

    }

    return render(request, "home.html", context)



def manage(request):
    return render(request, 'manage.html')



def feed(request):
    return render(request, 'feed.html')



def about(request):
    return render(request, 'about.html')



def scan_info(request):
    filepath = db.child('scan_result').child('filepath').get().val()
    filesize = db.child('scan_result').child('filesize').get().val()
    filetype = db.child('scan_result').child('filetype').get().val()
    hashstring = db.child('scan_result').child('hashstring').get().val()
    fbstring = db.child('scan_result').child('fbstring').get().val()
    fileAge = db.child('scan_result').child('fileAge').get().val()
    total_score = db.child('scan_result').child('total_score').get().val()
    message_type = db.child('scan_result').child('message_type').get().val()
    scan_time = db.child('scan_info').child('scan_time').get().val()
    site_name = db.child('scan_info').child('site_name').get().val()
    uid = db.child('scan_info').child('uid').get().val()

    context = {
        'filepath': filepath,
        'filesize': filesize,
        'filetype': filetype,
        'hashstring': hashstring,
        'fbstring': fbstring,
        'fileAge': fileAge,
        'total_score': total_score,
        'message_type': message_type,
        'scan_time': scan_time,
        'site_name': site_name,
        'UID': uid,

    }


    return render(request, "scan_info.html", context)




