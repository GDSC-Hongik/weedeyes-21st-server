#from django.urls import path
#from .views import login_view,signup_view

#urlpatterns = [
#    path('login/',login_view,name='login'),
#    path('signup/',signup_view,name='signup'),
#]

from django.contrib import admin
from django.urls import path,include
from . import views
from .views import signup_view

#app_name = 'users'

urlpatterns = [
    #path('admin/', admin.site.urls),
    # Here we are assigning the path of our url
    #path('', views.signIn),
    #path('postsignIn/', views.postsignIn,name='postsignIn'),
    ##path('signUp/', views.signUp, name="signup"),
    #path('logout/', views.logout, name="log"),
    #path('postsignUp/', views.postsignUp,name='postsignUp'),
    #path('signup/',signup_view,name='signup'),
    
    path('',views.home,name='home'),
    path('login/',views.postsignIn,name='login'),
    path('signup/',signup_view,name='signup'),
    path('logout/', views.logout, name="log"),
    #path('login/',views.signIn,name='login'),
    #path('postsignIn/', views.postsignIn,name='postsignIn'),
   
]

