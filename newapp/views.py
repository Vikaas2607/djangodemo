from django.shortcuts import render,redirect
from django.http import HttpResponse
from newapp.forms import LoginForm
# Create your views here.

def HelloView(request):
    return render(request,'helloworld.html')

def Login(request):
    login_form=LoginForm()
    if request.method == 'GET':
        return render(
            request,
            template_name="login_form.html",
            context={'form':login_form}
        )
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("Success")
        else:
            return HttpResponse("Form is invalid")
    else:
        return HttpResponse("error")


