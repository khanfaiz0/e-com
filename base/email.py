from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email, email_token):
    subject = "Your accounts need to be varified"
    email_from = settings.EMAIL_HOST_USER
    message = f"Hi, click on the link to activate your account http://127.0.0.1:8000/account/activate/{email_token}"

    send_mail(subject , message , email_from , [email])