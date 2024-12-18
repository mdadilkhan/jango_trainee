from django.shortcuts import render, HttpResponse

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
    return render(request, 'contact.html')
