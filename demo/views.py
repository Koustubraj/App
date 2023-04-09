from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'demo/index.html')


def greet(request):
    
    if request.method == 'POST':
        # retrieves value only when we click on submit button
        # name = request.POST['username'] # we can retreive dict value using keys
        name = request.POST.get('username') # we can retreive dict value using keys
        context = {'name' : name}
        return render(request, 'demo/greet.html',context)
    else:  # if the method is GET
        return render(request, 'demo/greet.html')
    


registered_email = 'sample@gmail.com'
registered_pwd = 'sample'

def login(request):
    msg = None
    if request.method == 'POST':
        email = request.POST['user_email']
        pwd = request.POST['user_pwd']

        if registered_email == email and registered_pwd == pwd:
           msg = 'Login Success'
        else:
            msg = 'Login Fail' 

    return render(request, 'demo/login.html', {'msg' : msg})




registered_email = 'sample@gmail.com'
registered_pwd = 'sample'

def login2(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        pwd = request.POST['user_pwd']

        if registered_email == email and registered_pwd == pwd:
           
           messages.success(request,'Welcome...')

           # return redirect(greet)  # view function name
           return redirect('greet_page')  # url name
        else:
            messages.error(request,'Wrong Credentials...')

    return render(request, 'demo/login2.html')
