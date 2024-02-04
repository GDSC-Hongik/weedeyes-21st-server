from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import credentials
# from rest_framework.decorators import api_view
from firebase_admin import auth #logout 새로 구현하며 추가함. 
from firebase_admin import db
from django.http import HttpResponse #logout 새로 구현하며 추가함. 
#from firebase import firebase
import pyrebase

# Create your views here.

cred = credentials.Certificate("serviceAccountKey.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://weedeyes-3d4ca-default-rtdb.asia-southeast1.firebasedatabase.app"
    })


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

dir = db.reference()


def signIn(request):
    return render(request,"Login.html")
def home(request):
    return render(request,"Home.html")

#주석처리한 부분은 고쳐서 이걸로 변경하거나 안고쳐지면 지금처럼 가야할듯
#def postsignIn(request):
#    if request.method=='POST':
#        email=request.POST.get('email')
#        pasw=request.POST.get('password')
#        try:
#           # if there is no error then signin the user with given email and password
#           user=authe.sign_in_with_email_and_password(email,pasw)
#           return redirect('success_page')
#        except Exception as e:
#            message="Invalid Credentials!!Please ChecK your Data"
#            return render(request,"Login.html",{"message":message})
#    
#    return render(request,"Home.html",{"email":email})


'''       
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
''' 

'''
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")

'''

def logout(request):
    try:
        # Django 세션에서 사용자 정보 제거
        del request.session['uid']
        
        # Firebase에서 사용자 토큰 폐기
        uid = request.user.get('uid')
        auth.revoke_refresh_tokens(uid)
    except Exception as e:
        print(f"Error during logout: {e}")
    
    return render(request, "Login.html")


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

'''
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            #user_data = {'email': email, 'password': password}
            #result = firebase.post('/Users', user_data)
            
            user = authe.create_user_with_email_and_password(email, password)
            
            uid=user['localId']
            data={"name":name,"status":"1"}
            database.child("users").child(uid).child("details").set(data)
            
            #user_data = {'email': email, 'uid': user['uid']}
            #db.reference('/Users').child(user['uid']).set(user_data)
            # 회원가입에 성공하면 Firebase UID 등의 정보가 user에 담겨 반환됨
            
            # 회원가입 성공 후의 동작을 추가하기
            # 예: 세션에 사용자 정보 저장 등

            return redirect('success_page')  # 회원가입 성공 후 이동할 페이지
        except Exception as e:
            # 회원가입 실패 처리
            error_message = str(e)
            return render(request, 'Registration.html', {'error_message': error_message})
    return render(request, 'Registration.html')

'''

def home(request):
    return render(request, 'Home.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = authe.create_user_with_email_and_password(email, password)
            # 회원가입에 성공하면 Firebase UID 등의 정보가 user에 담겨 반환됨

            # 회원가입 성공 후의 동작을 추가하세요
            # 예: 세션에 사용자 정보 저장 등

            return redirect('success_page')  # 회원가입 성공 후 이동할 페이지
        except Exception as e:
            # 회원가입 실패 처리
            error_message = str(e)
            return render(request, 'Registration.html', {'error_message': error_message})

    return render(request, 'Registration.html')

def postsignIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = authe.sign_in_with_email_and_password(email, password)
            # 로그인에 성공하면 Firebase UID 등의 정보가 user에 담겨 반환됨

            # 로그인 성공 후의 동작을 추가하세요
            # 예: 세션에 사용자 정보 저장 등

            return redirect('home')  # 로그인 성공 후 이동할 페이지
        except Exception as e:
            # 로그인 실패 처리
            #print("Exception:", repr(e))
            error_message = str(e)
            
            
            #if 'INVALID_EMAIL' in error_message:
            #    error_message = '유효하지 않은 이메일 주소입니다.'
            #elif 'INVALID_PASSWORD' in str(e):
            #    error_message = '잘못된 비밀번호입니다.'
            if 'INVALID' in error_message:
                error_message = '로그인에 실패했습니다. 다시 시도하세요.'
            
            #error_message='이메일 또는 비밀번호가 잘못되었습니다. 다시 확인하세요'
            return render(request, 'Login.html', {'error_message': error_message})
            
    
    return render(request, 'Login.html')