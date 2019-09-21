from django.shortcuts import render, redirect, get_object_or_404
from app_version_1.forms import LoginForm, UserForm
from app_version_1.models import User
import sys

def home(request):
    return render(request,'home.html')

def login(request):
    try:
        login_data = LoginForm(request.POST)
        username = login_data.data['username']
        password = login_data.data['password']
        user = get_object_or_404(User, username = username, password = password)
        print(user)
        return render(request, 'success.html', {"username": user.username,'password':user.password})
    except:
        return render(request, 'unsuccess.html')

def registerForm(request):
    return render(request,'register.html')

def register(request):
    try:
        user_data = UserForm(request.POST)
        email_id = user_data.data['email_id']
        password = user_data.data['password']
        dob = user_data.data['dob']
        address = user_data.data['address']
        pincode = user_data.data['pincode']
        mob_no = user_data.data['mob_no']
        type = 'C'
        username = email_id
        print(email_id)
        print(password)
        print(username)
        user = User.create(email_id=email_id,password=password,username=username,dob=dob,address=address,pincode=pincode,mob_no=mob_no,type=type)
        user.save()
        # user = get_object_or_404(User, username = username, password = password)
        print(user)
        return render(request, 'success.html', {"username": user.username,'password':user.password})
    except:
        return render(request, 'unsuccess.html')
