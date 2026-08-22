from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            User.objects.create_user(username=username,
                                     email=email,
                                     password=password)
            return render(request, 'register.html')
    return render(request, 'register.html')