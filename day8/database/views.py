from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from database.models import Employee
from django.urls import reverse
 

def saveuser(request):            # create record (c of crud)

    if request.method == 'POST':

        eno = request.POST['eno']
        ename = request.POST['ename']
        esal = request.POST['esal']

        emp = Employee(eno=eno, ename=ename, esal=esal)
        emp.save()

        urls = reverse('employeelist')
        return HttpResponseRedirect(urls)

    return HttpResponse("<h1>Please submit the form</h1>")
    
def employeelist(request): # read record (crud)
    Employees=Employee.objects.all() #it return questset of employee
    res=render(request,'employeelist.html',{'Employees':Employees}) 
    return res 

def updateEmployeeform(request):
    id=request.GET['id']
    employee=Employee.objects.filter(id=id).values()
    res=render(request,'updateEmployeeform.html',{'employee':employee[0]})
    return res 

def updateEmployee(request):
    id=request.POST['id']
    eno=request.POST['eno']
    ename=request.POST['ename']
    esal=request.POST['esal']
    Employee(id=id,eno=eno,ename=ename,esal=esal).save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def deleteEmployee(request):
    id=2
    emp=Employee.objects.filter(id=id)
    emp.delete()
    return HttpResponse("<h1>delete record successfully</h1>") 
def newEmployeeForm(request):
    res=render(request,'newEmployeeForm.html')
    return res 

# Create your views here.
