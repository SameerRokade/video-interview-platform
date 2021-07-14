from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

from django.contrib import messages

@login_required(login_url='login')
def home(request):
	return render(request, 'bot/home.html')



@login_required(login_url='login')
def profile(request):
    return render(request, 'bot/profile.html')

def userLogin(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username= username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else :
			messages.info(request, 'Username or Password is Incorrect')

	context={}
	return render(request, 'bot/login.html', context)




def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Successfully created account for '+ user)
			return redirect('login')
	context={'form':form}
	return render(request, 'bot/register.html', context)


def userLogout(request):
	logout(request)
	return redirect('login')



