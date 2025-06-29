from django import forms 
from django.contrib.auth.models import User
from btrapp.models import Registration
from django_recaptcha.fields import ReCaptchaField
from lawfirmapp.models import EnquiryForm
from lawfirmapp.models import Appointment
class register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ['username','email','password']  

class UserProfileForms(forms.ModelForm):
    class Meta:
        model = Registration 
        fields = ['phone','address','street','city','state','zipcode','image']
    captcha = ReCaptchaField()
    
class UpdateUserDeatails(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email'] 


class UpdateUserProfileDetails(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['phone','address','street','city','state','zipcode','image'] 

class UserEnquiryForm(forms.ModelForm):
    class Meta:
        model = EnquiryForm 
        fields = '__all__' 

class userAppointment(forms.ModelForm):
    fee = forms.CharField(max_length=100,initial=500,disabled=True)
    class Meta:
        model = Appointment
        exclude = ['user']