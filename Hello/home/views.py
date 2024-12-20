from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the home page'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world. You're at the home index.")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        print(request.POST) 
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('num')
        password = request.POST.get('password')

        contact = Contact.objects.create(
            name=name, 
            email=email, 
            number=number, 
            password=password
        )
        return redirect('contact')
    return render(request, 'contact.html')


