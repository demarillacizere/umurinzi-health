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
    profile = Profile.objects.get(user=request.user)
    locations = Location.objects.all()
    context = {
        'locations':locations,
    }
    return render(request,'index.html',context)

@login_required(login_url='/accounts/login/')
def about_us(request):
    return render(request,'about.html')

@login_required(login_url='/accounts/login/')
def pharmacies(request):
    pharmacies = Pharmacy.objects.all()
    return render(request,'pharmacies.html',{'pharmacies':pharmacies})
    
@login_required(login_url='/accounts/login/') 
def pharm_details(request,pharm_id):
    pharm=Pharmacy.objects.get(id=pharm_id)
    print(pharm.name)
    return render(request,"pharmacy.html",{"pharm":pharm})

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            profile=Profile.objects.create(user=new_user,email=new_user)
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/registration_form.html', context)

def search_results(request):
    profile = Profile.objects.get(user=request.user)
    if 'drug' in request.GET and request.GET["drug"]:
        search_term = request.GET.get("drug")
        searched_drugs = Drug.search(search_term)
        message = f"{search_term}"
        if 'location' in request.GET and request.GET["location"]:
            loc = request.GET.get("location")
            location = Location.objects.get(name=loc)
            if profile.location != location:  
                profile.location=location
                profile.save()
        if searched_drugs:
            profile = Profile.objects.get(user=request.user)
            location = profile.location
            drug = Drug.objects.get(id=searched_drugs.id)
            pharmacies = drug.pharmacy.all()
            nearest = pharmacies.filter(location=location).all()
            others=[]
            for pharm in pharmacies:
                if pharm.location != location.name:
                    others.append(pharm)
            return render(request, 'search.html',{"message":message,"drugs": searched_drugs,"drug":drug, "pharmacies":pharmacies,"nearest":nearest,"others":others})
        else:
            return render(request, 'search.html',{"message":message,"drugs": searched_drugs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/') 
def get_details(request,drugs_id):
    profile = Profile.objects.get(user=request.user)
    location = profile.location
    drug = Drug.objects.get(id=drugs_id)
    pharmacies = drug.pharmacy.all()
    nearest = pharmacies.filter(location=location).all()
    others=[]
    for pharm in pharmacies:
        if pharm.location != location.name:
            others.append(pharm)
    
    return render(request,"details.html",{"drug":drug, "pharmacies":pharmacies,"nearest":nearest,"others":others,})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    print(profile.user)
    form=ProfileUpdateForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    context={
        'form':form,
        'profile':profile,
    }
    return render(request,"profile/profile.html",context=context)

