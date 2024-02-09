import os
#from dotenv import dotenv
from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import credentials
# from rest_framework.decorators import api_view
from firebase_admin import auth #logout 새로 구현하며 추가함. 
from firebase_admin import db
from django.http import HttpResponse #logout 새로 구현하며 추가함. 
#from firebase import firebase
import pyrebase
#import firebase
from django.http import JsonResponse

#from datetime import datetime, timezone
import urllib.parse
from django.contrib.auth import logout as django_logout

from django.contrib.auth.decorators import login_required
# Create your views here.


#cred = credentials.Certificate("serviceAccountKey.json")
#if not firebase_admin._apps:
#    firebase_admin.initialize_app(cred, {
#        'databaseURL': "https://weedeyes-3d4ca-default-rtdb.asia-southeast1.firebasedatabase.app"
#    })

#dotenv()
#service_account_key_path=os.getenv("serviceAccountKey_path")
#cred = credentials.Certificate("service_account_key_path")
#if not firebase_admin._apps:
#    firebase_admin.initialize_app(cred, {
#        'databaseURL': "https://weedeyes-3d4ca-default-rtdb.asia-southeast1.firebasedatabase.app"
#    })

'''


dir = db.reference()
'''


#def home(request):
#    return render(request,"Home.html")

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

#dir = db.reference()

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
    #next_url = request.session.get('next_url', '') 
    #context = {'next_url': next_url}
    
    
    firebase_id_token = request.session.get('firebase_id_token')
    
    if firebase_id_token:
        try:
            # Firebase ID 토큰 검증
            #encoded_id_token = urllib.parse.quote(firebase_id_token, safe='')
            #decoded_token = auth.verify_id_token(encoded_id_token)
            decoded_token = auth.verify_id_token(firebase_id_token)
            # 인증된 사용자 UID 가져오기
            uid = decoded_token['uid']
            # 인증된 사용자 정보를 활용하여 추가 작업 수행
            # 예: 사용자 프로필 가져오기, 보호된 리소스에 접근 등
            # 여기에서는 사용자 정보를 출력하는 예시 코드를 작성
            print("Authenticated user UID:", uid)
        except Exception as e:
            # Firebase ID 토큰 검증 실패 처리
            print("Firebase ID 토큰 검증 실패:", e)
    else:
        # 로그인이 되어있지 않은 상태
        print("User is not authenticated")
    
    
    return render(request, 'Home.html')
    #next_url = request.session.pop('next_url', None)  # 세션에서 URL 가져오기
    #if next_url:
    #    return redirect(next_url)
    #else:
    #    return render(request, 'home.html')


def logout(request):
    try:
        # Django 세션에서 사용자 정보 제거
        del request.session['uid']
        del request.session['email']
        
        # Firebase에서 사용자 토큰 폐기
        uid = request.user.get('uid')
        auth.revoke_refresh_tokens(uid)
    except Exception as e:
        print(f"Error during logout: {e}")
    
    return render(request, "Login.html")


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


# 이 함수가 필요한지에 대해서는 고민을 해 보아야..
def verify_id_token(request):
    # Extract ID token from request
    id_token = request.POST.get('idToken')
    
    try:
        # Verify and decode ID token
        decoded_token = auth.verify_id_token(id_token)
        # Extract UID from decoded token
        uid = decoded_token['uid']
        print(decoded_token)
        # You can now use UID to identify the user
        # For example, you can perform database operations or return a response
        return JsonResponse({'success': True, 'uid': uid})
    
    except Exception as e:
        # Handle token verification errors
        return JsonResponse({'error': str(e)})




def postsignIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        next_url = request.GET.get('next', '/users') 
        print("next_url:",next_url)
        try:
            user = authe.sign_in_with_email_and_password(email, password)
            
            
            raw_id_token = user['idToken']
            print("raw_id_token:",raw_id_token)
            
            # Firebase Admin SDK를 사용하여 ID 토큰 검증 및 디코딩
            decoded_token = auth.verify_id_token(raw_id_token)
            print("decoded_token:",decoded_token)
            uid = decoded_token['uid']
            print("uid:",uid)
            
            
            
            #token=user['idToken']
            #print(token)
            #uid=user['localId']
            #print(uid)
            #email=user['email']
            
            #id_token = user['idToken']
            #decoded_token = auth.verify_id_token(id_token)
            #uid = decoded_token['uid']
            # 로그인에 성공한 사용자의 ID Token을 가져옵니다.
            #id_token = user['idToken']
            # 사용자의 클레임에 요청한 페이지의 경로를 저장합니다.
            # 이 예제에서는 요청한 페이지의 URL을 'next'라는 이름으로 클레임에 저장합니다.
            
            
            #토큰 저장
            #id_token = user['idToken']
            
            ##request.session['id_token'] = id_token
            #request.session['uid']=str(id_token)
            #request.session['email']=email
            #custom_claims={'next':request.GET.get('next')}
            
            #auth.set_custom_user_claims(uid,custom_claims)
            
            request.session['firebase_id_token'] = raw_id_token
            request.session['uid'] = uid
            request.session['email'] = email
            
            #exp_time = datetime.fromtimestamp(decoded_token['exp'], timezone.utc)
            # 만료 시간을 클라이언트가 아닌 서버 시간으로 설정
            #exp_time = exp_time.timestamp()
            #request.session['exp_time'] = exp_time
            
            
            print("session user id:",request.session['uid'])
            print("session user email:",request.session['email'])
            response=redirect('home')
            print(request.session.session_key)
            response.set_cookie('sessionid',request.session.session_key)
            
            
            
            
            return response # 로그인 성공 후 이동할 페이지
            #return redirect('home')
            #return redirect(next_url)
        except Exception as e:
            error_message = str(e)
            if 'INVALID' in error_message:
                error_message = '로그인에 실패했습니다. 다시 시도하세요.'
            
            #error_message='이메일 또는 비밀번호가 잘못되었습니다. 다시 확인하세요'
            return render(request, 'Login.html', {'error_message': error_message})
            
    
    return render(request, 'Login.html')
    