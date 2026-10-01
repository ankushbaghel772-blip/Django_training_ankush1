from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from myuser.models import user
from django.urls import reverse



def home(request): 
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')
def saveuser(request):
    user1=user()
    u=user.object.filter(username=request.POST['username'])
    if not u: 
        user1.username=request.POST['username']
        user1.password=request.POST['password']
        user1.name=request.POST['name']
        user1.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'signup.html',
                      {
                          'errormsg':'Username  already exit'
                      }
                      
                      )
        from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def login(request):
    return render(request, 'login.html')


def loginvalidation(request):

    try:
        user1 = user.objects.get(
            username=request.POST['username'],
            password=request.POST['password']
        )

        return HttpResponseRedirect(reverse('home'))

    except user.DoesNotExist:
        return render(
            request,
            'login.html',
            {'erg': 'Invalid username or password'}
        )
        
        
        
        
    
    
# Create your views here.
