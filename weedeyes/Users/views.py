from django.shortcuts import render,redirect
#import firebase_admin
#from firebase_admin import auth
import pyrebase

# Create your views here.

config={
    'apiKey': "AIzaSyC05973cMkAo54VjVdQrAzlqM9t0nLt5aI",
    'authDomain': "weedeyes-3d4ca.firebaseapp.com",
    'databaseURL': "https://weedeyes-3d4ca-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "weedeyes-3d4ca",
    'storageBucket': "weedeyes-3d4ca.appspot.com",
    'messagingSenderId': "547490552512",
    'appId': "1:547490552512:web:e1a1ae80bf6010894bab25",
    'measurementId': "G-2CRVDZ8G59"
}

firebase=pyrebase.initialize_app(config)

authe=firebase.auth()
database=firebase.database()

def signIn(request):
    return render(request,"Login.html")
def home(request):
    return render(request,"Home.html")


def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('password')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
        
    except Exception as e:

        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"Login.html",{"message":message})
    
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"Home.html",{"email":email})

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")

'''
def signUp(request):
    return render(request,"Registration.html")


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
    except:
        return render(request, "Registration.html")
    return render(request,"Login.html")
'''

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = authe.create_user_with_email_and_password(email, password)
            # 회원가입에 성공하면 Firebase UID 등의 정보가 user에 담겨 반환됨
            
            # 회원가입 성공 후의 동작을 추가하기
            # 예: 세션에 사용자 정보 저장 등

            return redirect('success_page')  # 회원가입 성공 후 이동할 페이지
        except Exception as e:
            # 회원가입 실패 처리
            error_message = str(e)
            return render(request, 'Registration.html', {'error_message': error_message})
    return render(request, 'Registration.html')