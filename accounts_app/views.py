from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')

def login_view(request):
    l_form = Login_Form()
    if request.method == 'POST':
        l_form = Login_Form(request,request.POST)
        if l_form.is_valid():
            username = l_form.cleaned_data.get('username')
            password = l_form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
    context = {'l_form':l_form}
    return render(request,'login.html',context)

def logout_view(request):
    user = request.user
    logout(request)
    context = {'user':user}
    return render(request,'logout.html',context)

def categorys_view(request):
    categorys = Category.objects.all()
    context = {'categorys':categorys}
    return render(request,'categorys.html',context)

def category_add_view(request):
    c_form = Category_Form()
    if request.method == 'POST':
        c_form = Category_Form(request.POST)
        c_form.save()
    context = {'c_form':c_form}
    return render(request,'category_add.html',context)

def category_details_view(request, pk):
    category = get_object_or_404(Category,id=pk)
    context = {'category':category}    
    return render(request,'category_details.html',context)

def category_update_view(request,pk):
    category = get_object_or_404(Category,id=pk)
    c_form = Category_Form(instance=category)
    if request.method == 'POST':
        c_form = Category_Form(request.POST,instance=category)
        c_form.save()
    context = {'c_form':c_form}
    return render(request,'category_update.html',context)

def category_delete_view(request, pk):
    category = get_object_or_404(Category,id=pk)
    if request.method == 'POST':
        category.delete()
    context = {'category':category}
    return render(request,'category_delete.html',context)

def roles_view(request):
    roles = Role.objects.all()
    context = {'roles':roles}
    return render(request,'roles.html',context)

def role_add_view(request):
    r_form = Role_Form()
    if request.method == 'POST':
        r_form = Role_Form(request.POST)
        r_form.save()
    context = {'r_form':r_form}
    return render(request,'role_add.html',context)

def role_details_view(request, pk):
    role = get_object_or_404(Role,id=pk)
    context = {'role':role}
    return render(request,'role_details.html',context)

def role_update_view(request,pk):
    role = get_object_or_404(Role,id=pk)
    r_form = Role_Form(instance=role)
    if request.method == 'POST':
        r_form = Role_Form(request.POST,instance=role)
        r_form.save()
    context = {'r_form':r_form}
    return render(request,'role_update.html',context)

def role_delete_view(request,pk):
    role = get_object_or_404(Role,id=pk)
    if request.method == 'POST':
        role.delete()
    context = {'role':role}
    return render(request,'role_delete.html',context)

def employees_view(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request,'employees.html',context)

def employee_add_view(request):
    e_form = Employee_Form()
    if request.method == 'POST':
        e_form = Employee_Form(request.POST,request.FILES)
        e_form.save()
    context = {'e_form':e_form}
    return render(request,'employee_add.html',context)

def employee_details_view(request, pk):
    employee = get_object_or_404(Employee,id=pk)
    context = {'employee':employee}
    return render(request,'employee_details.html',context)

def employee_update_view(request,pk):
    employee = get_object_or_404(Employee,id=pk)
    e_form = Employee_Form(instance=employee)
    if request.method == 'POST':
        e_form = Employee_Form(request.POST,request.FILES,instance=employee)
        e_form.save()
    context = {'e_form':e_form}
    return render(request,'employee_update.html',context)

def employee_delete_view(request,pk):
    employee = get_object_or_404(Employee,id=pk)
    if request.method == 'POST':
        employee.delete()
    context = {'employee':employee}
    return render(request,'employee_delete.html',context)

def users_view(request):
    users = User.objects.all() 
    context = {'users':users}
    return render(request,'users.html',context)

def user_add_view(request):
    u_form = User_Form()
    if request.method == 'POST':
        u_form = User_Form(request.POST)
        if u_form.is_valid():
            u_form.save()
    context = {'u_form':u_form}
    return render(request,'user_add.html',context)

def user_details_view(request, pk):
    user = get_object_or_404(User,id=pk)
    context = {'user':user}
    return render(request,'user_details.html',context)

def user_update_view(request,pk):
    user = get_object_or_404(User,id=pk)
    u_form = User_Form(instance=user)
    if request.method == 'POST':
        u_form = User_Form(request.POST,instance=user)
        if u_form.is_valid():
            u_form.save()
    context = {'u_form':u_form}
    return render(request,'user_update.html',context)

def user_delete_view(request,pk):
    user = get_object_or_404(User,id=pk)
    if request.method == 'POST':
            user.delete()
    context = {'user':user}
    return render(request,'user_delete.html',context)

    