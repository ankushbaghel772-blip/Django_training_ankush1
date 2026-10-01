from django.urls import path
from . views import *# . ki jagah appname or * ke jagha views likh sakte hai

urlpatterns =[
    

    path('signup/',signup,name='signup'),
    path('saveuser/',saveuser,name='saveuser'),
    path('login/',login,name='login'),
    path('loginvalidation/',loginvalidation,name='loginvalidation'),
    path('home/',home,name='home'),
    
]