from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, PostCreationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from posts.models import Post, Category


# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect(reverse('posts:index'))

    else:
        form = UserLoginForm()

    context = {'form': form}

    return render(request, "login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрировались.')
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'registration.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'profile.html', context)


def user_posts(request):
    posts = Post.objects.filter(by_user=request.user)
    context = {
        'posts': posts
    }
    return render(request, 'user_posts.html', context)


def create_post(request):
    if request.method == "POST":

        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            print('asloxa')
            post = form.save(commit=False)
            post.by_user = request.user
            post.save()
            return redirect('users:user_posts')
        else:
            print(form.errors)
    else:
        form = PostCreationForm()

    context = {
        'form': form
    }
    return render(request, 'create_post.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('posts:index'))
