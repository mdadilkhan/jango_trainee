from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.
# views.py
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')  # Redirect to the login page
    return render(request, 'home/login.html')  # Update to 'home/login.html' if it's in the app's templates folder


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Checking if user has correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # Login the user and redirect to the home page
            auth_login(request, user)
            return redirect('/')
        else:
            # If authentication fails, show the login page again
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('/login')
