from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def demo(request):
    if request.method == 'POST':
        name = request.POST['txt']
        email = request.POST['email']
        password = request.POST['pswd']

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        messages.info(request, 'Registered successfully')
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        email= request.POST['email']
        user = auth.authenticate(username=username,email=email,password=password)
        if user is not None:
            auth.login(request,user)
        else:
            messages.info(request,'invalid details')
    return render(request,'index.html')
