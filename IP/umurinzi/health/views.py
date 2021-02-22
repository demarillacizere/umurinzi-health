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


@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            profile=Profile.objects.create(user=user,email=email)
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/registration_form.html', context)

def search_results(request):

    if 'drug' in request.GET and request.GET["drug"]:
        search_term = request.GET.get("drug")
        searched_drugs = Drug.search(search_term)
        print(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"drugs": searched_drugs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/') 
def get_details(request,drugs_id):
    drug = Drug.objects.get(id=drugs_id)
    pharmacies = drug.pharmacy.all()
    return render(request,"details.html",{"drug":drug, "pharmacies":pharmacies})