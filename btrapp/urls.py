from django.urls import path 
from btrapp import views 
urlpatterns = [
    path('', views.index, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('home', views.home, name='home'),
    path('logout', views.user_logout, name='logout'), 
    path('profile',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('lawfirm/', views.lawfirm, name='lawfirm'),
    path('allCase',views.allCase,name='allCase'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('appointments_user',views.appointments_user,name='appointments_user')
]