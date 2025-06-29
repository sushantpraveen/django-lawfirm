from django.core.mail import send_mail 
from django.http import HttpResponse 
from django.template.loader import render_to_string 
from django.utils.html import strip_tags 

def send_email_view(email):
    subject = 'Your appointment is Recived'
    message ='Hii,Sir/Madam your appointment for concerned lawyer has saved in our database please wait for the lawyer appointment'
    from_email = 'sushantprem2820@gmail.com'
    recipient_list = [email] 

    html_message = render_to_string('appointment_email_template.html')
    plain_message = strip_tags(html_message) 

    try:
        send_mail(
            subject = subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False
        ) 
        return HttpResponse('Email Sent Successfully!') 
    except Exception as e: 
        return HttpResponse(f"Error sending email: {str(e)}")