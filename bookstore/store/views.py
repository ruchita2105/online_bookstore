from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import logout

def my_view(request):
    return render(request, "my_template.html")

def index(request):
    return render(request, 'store/index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('test')  # 'test.html'
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, "store/login.html")

@login_required(login_url='login')  # This ensures only logged-in users can access
def home(request):
    return render(request, 'test.html')

def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('test')

    return render(request, 'signup.html')

def test_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'store/test.html')

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'store/cart.html')
def logout_view(request):
        logout(request)
        return redirect('login')  # Or your homepage
