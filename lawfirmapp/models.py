from django.db import models

# Create your models here.
class LawyerDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    years_of_exp = models.PositiveIntegerField()
    specialisation = models.CharField(max_length=100) 
    total_cases = models.IntegerField()
    description = models.TextField()
    advimg = models.ImageField(upload_to='advimg/',blank=True,null=True) 

class AllTypeCases(models.Model):
    case_title = models.CharField(max_length=200)
    case_description = models.TextField()
    case_image = models.ImageField(upload_to='cases/',blank=True,null=True)


cases_types = [
    ('criminal','CRIMINAL'),
    ('civil','CIVIL'),
    ('family','FAMILY'),
    ('environmental','ENVIRONMENTAL'),
    ('bankrupty' , 'BANKRUPTY'),
    ('tort','TORT'),
    ('child abuse','CHILD ABUSE'),
    ('labour law','LABOUR LAW'),
    ('administrative','ADMINISTRATIVE'),
    ('contract','CONTRACT'),
    ('other','OTHER'),
]

class EnquiryForm(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100,choices=cases_types)
    description = models.TextField()
    any_document = models.FileField(upload_to='documents/') 

courtname = [
    ('supreme court', 'SUPREME COURT'),
    ('high court', 'HIGH COURT'),
    ('district court', 'DISTRICT COURT'),
    ('family court', 'FAMILY COURT'),
    ('civil court', 'CIVIL COURT'),
    ('criminal court', 'CRIMINAL COURT'),
    ('session court', 'SESSION COURT'),
    ('magistrate court', 'MAGISTRATE COURT'),
    ('consumer court', 'CONSUMER COURT'),
    ('labour court', 'LABOUR COURT'),
]
from django.contrib.auth.models import User
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100,choices=cases_types)
    description = models.TextField()
    case_document = models.FileField(upload_to='')
    total_no_hearing = models.IntegerField()
    court_name = models.CharField(max_length=100,choices=courtname)
    fee = models.IntegerField(default=500) 


class CaseManagement(models.Model):
    cases_type = models.ForeignKey(Appointment,related_name='appointments',on_delete=models.CASCADE)
    lawyers = models.ForeignKey(LawyerDetails,related_name='lawyerdetail',on_delete=models.CASCADE)   
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

