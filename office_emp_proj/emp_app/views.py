from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = int(request.POST['salary'])
        bouns = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee(firstname= firstname, lastname=lastname, salary=salary, bouns=bouns, phone=phone, dept = dept, role = role, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("<h3>Employee Removed Successfully</h3>")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(firstname__icontains = name) | Q(lastname__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')