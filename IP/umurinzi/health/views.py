from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect,JsonResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
#from .email import send_welcome_email

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')