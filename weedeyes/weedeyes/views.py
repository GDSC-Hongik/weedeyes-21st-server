from django.shortcuts import render
import pyrebase

config={
    "apiKey": "AIzaSyC05973cMkAo54VjVdQrAzlqM9t0nLt5aI",
    "authDomain": "weedeyes-3d4ca.firebaseapp.com",
    "databaseURL": "https://weedeyes-3d4ca-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "weedeyes-3d4ca",
    "storageBucket": "weedeyes-3d4ca.appspot.com",
    "messagingSenderId": "547490552512",
    "appId": "1:547490552512:web:e1a1ae80bf6010894bab25",
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
