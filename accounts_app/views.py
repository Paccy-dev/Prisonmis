from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import datetime
from .forms import *
from .models import *
from prisoners_app.models import *

    
# Create your views here.
def home_view(request):
    return redirect('dashboard')

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
                page = request.GET.get('next')
                if page:
                    messages.success(request, f'Login successful')           
                    return redirect(request.GET.get('next'))
                else:
                    messages.success(request, f'Login successful')           
                    return redirect('dashboard')
        else:
            messages.warning(request, f"Login errors|User doesn't exist")
    context = {'l_form':l_form}
    return render(request,'login.html',context)

def logout_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
    context = {'user':user}
    return render(request,'logout.html',context)

def card_view(request):
    context = {}
    return render(request, 'card.html',context)

@login_required
def dashboard_view(request):
    users = User.objects.all()
    prisoners = Prisoner.objects.all()
    crimes = Crime.objects.all()
    complaints = Complaint.objects.all()
    cells = Cell.objects.all()
    transfers = Transfer.objects.all()
    releases = Release.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST': 
        logout(request)
        return redirect('login')
    all_prisoners = Prisoner.objects.all()
    today = datetime.date.today()
    today_yr = today.year
    releases = []
    for prisoner in all_prisoners:
        if prisoner.release_date is not None:
            year = prisoner.release_date.year
            if year == today_yr:
                releases.append(prisoner)  
    context = {'users':users,'prisoners':prisoners,'crimes':crimes,'complaints':complaints,'cells':cells,'transfers':transfers,'releases':releases,'categories':categories}
    return render(request, 'dashboard.html',context)
    
@login_required
def categorys_view(request):
    categorys = Category.objects.all()
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            category = get_object_or_404(Category,id=pk)
            category.delete()
            messages.success(request, f'Category {category} - deletion successful')
        else: 
            logout(request)
            return redirect('login')
    context = {'categorys':categorys}
    return render(request,'categorys.html',context)

@login_required
def category_add_view(request):
    c_form = Category_Form()
    if request.method == 'POST':
        c_form = Category_Form(request.POST)
        if c_form.is_valid():
            c_form.save()
            name = c_form.cleaned_data.get('name')
            messages.success(request, f'Category {name} - creation successful')
            return redirect('categorys')
    context = {'c_form':c_form}
    return render(request,'category_add.html',context)

@login_required
def category_details_view(request, pk):
    category = get_object_or_404(Category,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            category = get_object_or_404(Category,id=pk)
            category.delete()
            messages.success(request, f'Category {category} - deletion successful')
            return redirect('categorys')
        else: 
            logout(request)
            return redirect('login')
    context = {'category':category}    
    return render(request,'category_details.html',context)

@login_required
def category_update_view(request,pk):
    category = get_object_or_404(Category,id=pk)
    c_form = Category_Form(instance=category)
    if request.method == 'POST':
        c_form = Category_Form(request.POST,instance=category)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, f'Category {category} - update successful')
            return redirect('category_details', pk)
    context = {'c_form':c_form}
    return render(request,'category_update.html',context)

@login_required
def category_delete_view(request, pk):
    category = get_object_or_404(Category,id=pk)
    context = {'instance':category}
    return render(request,'modal_delete.html',context)

@login_required
def users_view(request):
    users = User.objects.all() 
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            user = get_object_or_404(User,id=pk)
            user.delete()
            messages.success(request, f'User {user} - deletion successful')
            return redirect('users')
        else: 
            logout(request)
            return redirect('login')
    context = {'users':users}
    return render(request,'users.html',context)

@login_required
def user_add_view(request):
    u_form = User_Form()
    if request.method == 'POST':
        u_form = User_Form(request.POST,)
        if u_form.is_valid():
            u_form.save()
            name = u_form.cleaned_data.get('username')
            messages.success(request, f'User {name} - creation successful')
            return redirect('users')
    context = {'u_form':u_form}
    return render(request,'user_add.html',context)

@login_required
def user_details_view(request, pk):
    user = get_object_or_404(User,id=pk)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'delete':
            pk = str(request.POST.get('instance_id'))
            user = get_object_or_404(User,id=pk)
            user.delete()
            messages.success(request, f'User {user} - deletion successful')
            return redirect('users')
        else: 
            logout(request)
            return redirect('login')
    context = {'user':user}
    return render(request,'user_details.html',context)

@login_required
def user_update_view(request,pk):
    user = get_object_or_404(User,id=pk)
    p_form = Profile_Form(instance=user)
    if request.method == 'POST':
        name = str(request.POST.get('form'))
        if name == 'update':
            p_form = Profile_Form(request.POST,request.FILES,instance=user)
            if p_form.is_valid():
                p_form.save()
                messages.success(request, f'User {user} - update successful')
                return redirect('user_details', pk)
        else:
            logout(request)
            messages.success(request, f'Logout successful')
            return redirect('login')
    context = {'p_form':p_form}
    return render(request,'user_update.html',context)

@login_required
def user_delete_view(request,pk):
    user = get_object_or_404(User,id=pk)
    context = {'instance':user}
    return render(request,'modal_delete.html',context)