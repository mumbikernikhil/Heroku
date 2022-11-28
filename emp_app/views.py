from http.client import HTTPResponse
import imp
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request):
    emp = Employee.objects.all()
    context = {
        'emp':emp
    }
    return render(request, 'index.html', context)

def add_emp(request):
    position = Designation.objects.all()
    context = {
        'position':position
    }
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        post = request.POST.get('position')
        emp = Employee(first_name=first_name, last_name=last_name, email=email, phone=phone, position=post)
        emp.save()
        messages.info(request, "Employee Added Successfully")
        return redirect('/add_emp')
    return render(request, 'add_emp.html', context)

def delete_emp(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    emp.delete()
    return redirect('/')

def update_emp(request, emp_id):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        post = request.POST.get('position')

        edit = Employee.objects.get(id=emp_id)
        edit.first_name = first_name
        edit.last_name = last_name
        edit.email = email
        edit.phone = phone
        edit.position = post
        edit.save()
        return redirect('/')

    position = Designation.objects.all()
    emp = Employee.objects.get(id=emp_id)
    context = {
        'emp':emp,
        'position':position
    }
    return render(request, 'update_emp.html', context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        emp = Employee.objects.all()
        if name:
            emp = emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if email:
            emp = emp.filter(email=email)
        if phone:
            emp = emp.filter(phone=phone)
        context = {
            'emp':emp
        }
        return render(request, 'view_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HTTPResponse("Error")