from django.shortcuts import render,redirect
from btrapp.forms import register, UserProfileForms,UpdateUserDeatails,UpdateUserProfileDetails
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse 
from django.shortcuts import redirect 
from django.contrib.auth.decorators import login_required
from lawfirmapp.models import AllTypeCases
from btrapp.forms import UserEnquiryForm
from btrapp.forms import userAppointment
from django.shortcuts import render
from .forms import userAppointment
from lawfirmapp.models import Appointment 
from lawfirmapp.models import CaseManagement

def index(request):
    registered = False
    if request.method == 'POST':
        reg = register(request.POST)
        form1 = UserProfileForms(request.POST, request.FILES)
        if reg.is_valid() and form1.is_valid():
            user = reg.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user  # we are merging two models
            profile.save()
            registered = True
    else:
        reg = register()
        form1 = UserProfileForms()

    context = {
        'reg': reg,
        'form1': form1,
        'registered' : registered
    }
    return render(request, "index.html", context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
        else:
            return HttpResponse('pls check your credentials')
    return render(request,"login.html")


@login_required(login_url='user_login')
def home(request):
    return render(request,'home.html')


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('user_login') 

def profile(request):
    all_appointments = Appointment.objects.filter(user=request.user).prefetch_related('appointments__lawyers')
    return render(request, 'userprofile.html', {'all_appointments': all_appointments})

@login_required(login_url='user_login')
def update_profile(request):
    user = request.user  
    if request.method == 'POST':
        form = UpdateUserDeatails(request.POST, instance=user)
        form1 = UpdateUserProfileDetails(request.POST,request.FILES,instance=request.user.registration)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.save() 

            profile = form1.save(commit=False)
            profile.user= user
            profile.save()
            return redirect('profile')
    else:
        form = UpdateUserDeatails(instance=user)
        form1 = UpdateUserProfileDetails(instance=request.user.registration)
    return render(request, 'update_profile.html', {'form': form,'form1':form1}) 

def lawfirm(request):
    return render(request, "lawfirm.html")

# all cases 
def allCase(request):
    all_cases = AllTypeCases.objects.all()
    return render(request,"allcases.html",{'all_cases':all_cases}) 

# enquiry
def enquiry(request):
    registered = False
    if request.method == 'POST':
        user_enq = UserEnquiryForm(request.POST,request.FILES)
        if user_enq.is_valid():
            registered = True
    else:
        user_enq = UserEnquiryForm()
    context ={
        'user_enq':user_enq,
        'registered':registered
    }
    return render(request,"enquiry.html",context) 

from lawfirmapp.utils import send_email_view 
def appointments_user(request): 
    if request.method == 'POST':
        app = userAppointment(request.POST, request.FILES)
        if app.is_valid():
            print("Success") 
            email = app.cleaned_data['email']
            print(email)
            appointment = app.save(commit=False)
            appointment.user = request.user  
            appointment.save()
            response = send_email_view(email)
            return response 
         
    else:
        app = userAppointment()

    all_appointments = Appointment.objects.filter(user=request.user)  
    case_management = CaseManagement.objects.all()

    context = {
        'app': app,
        'all_appointments': all_appointments,
        'case_management': case_management
    }
    return render(request, "appointment.html", context)