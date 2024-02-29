from django.shortcuts import render,get_object_or_404,redirect
from  .models import *
from django.http import HttpResponse
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        # Get the form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        profile_picture = request.FILES.get('profile_picture')
        bio = request.POST.get('bio')
        print(username,password)

        # Check if the username or email is already taken
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request,"Username/Email is already in use")
            return redirect('/register')
        user = User.objects.create(username=username,
                                   email=email,
                                   )
        user.set_password(password)                           
        print(username,password)                           
        user.save()
        user_profile = UserProfile.objects.create(user=user, profile_picture=profile_picture, bio=bio)
        user_profile.save()
        messages.success(request,'Account created successfully! You are now able to log in')
        return redirect('login_view')   

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print(username,password)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request,"Login Succesfull")
            return redirect('home')
        else:
            messages.error(request,"Invalid Login Id or Password")

    return render(request, 'login.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    return render(request,'dashboard.html')


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request,"Account Deleted Successfully!")
        return redirect("home")
    return render(request,'delete_account.html')    

@login_required
def upload_posts(request):
    new_post = None
    if request.method =="POST":
        post_pic = request.FILES.get('post_pic')
        post_bio = request.POST.get( 'post_bio' )
        new_post = Posts.objects.create(user=request.user,post_pic=post_pic,post_bio=post_bio)
        new_post.save()
        messages.success(request,"Post Uploaded Successfully!")
        return redirect('dashboard')
    return render(request,'upload_posts.html',{'new_post': new_post})    

@login_required
def delete_post_view(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if post.user == request.user:
        post.delete()
        messages.success(request,'post deleted  successfully!')
        return redirect('dashboard')
    