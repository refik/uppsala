from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from uppsala.decorators import *

@rendered_with("users/index.html")
def index(request):
	return locals()

@rendered_with("frontpage/logged_in.html")
def login_user(request):
	username_login = request.POST['username']
	password_login = request.POST['password']
	user = authenticate(username=username_login, password=password_login)
	if user is not None:
		login(request, user)
		return locals()
	else:
		status = "log_fail"
		return locals()

@rendered_with("frontpage/logged_in.html")
def register(request):
	user_new = request.POST['username']
	password_new = request.POST['password']
	email_new = request.POST['email']
	user = User.objects.create_user(user_new,email_new,password_new)
	status = "reg_success"
	return locals()

@login_required
@rendered_with("frontpage/logged_in.html")
def logout_view(request):
    logout(request)
    return locals()
