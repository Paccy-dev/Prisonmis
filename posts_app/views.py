from django.shortcuts import render, get_object_or_404
from .forms import *

# Create your views here.

def posts_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'posts.html',context)
    
def post_add_view(request):
    p_form = Post_Form()
    if request.method == 'POST':
        p_form = Post_Form(request.POST,request.FILES)
        if p_form.is_valid():
            p_form.save()
            print('saved')
    context = {'p_form':p_form}
    return render(request,'post_add.html',context)        

def post_details_view(request, pk):
    post = get_object_or_404(Post,id=pk)
    context = {'post':post}
    return render(request,'post_details.html',context)

def post_update_view(request,pk):
    post = get_object_or_404(Post,id=pk)
    p_form = Post_Form(instance=post)
    if request.method == 'POST':
        p_form = Post_Form(request.POST,request.FILES,instance=post)
        if p_form.is_valid():
            p_form.save()
            print('saved')
    context = {'p_form':p_form}
    return render(request,'post_add.html',context)        

def post_delete_view(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.method == 'POST':
        post.delete()
    context = {'post':post}
    return render(request,'post_delete.html',context)        
