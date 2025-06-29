from django.contrib import admin
from.models import LawyerDetails
from.models import AllTypeCases
from.models import EnquiryForm
from lawfirmapp.models import CaseManagement
# Register your models here.

admin.site.register(LawyerDetails)
admin.site.register(AllTypeCases) 
admin.site.register(EnquiryForm)
admin.site.register(CaseManagement)