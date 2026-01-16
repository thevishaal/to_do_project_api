from django.core.mail import EmailMessage
import os
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, smart_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.getenv('DEFAULT_FROM_EMAIL'),
            to=[data['to_email']] 
        )
        email.send()

    @staticmethod
    def send_verification_email(request, user):
        uid = urlsafe_base64_encode(force_bytes(user.id))
        print('Verification Uid ',uid)
        token = PasswordResetTokenGenerator().make_token(user)
        print('Verification Token ',token)
        link = f"http://localhost:3000/api/user/{uid}/{token}/"
        print('Verification Link ',link)
        email_subject = "Verify your email"
        email_body = f"""
        Hi {user.name},  
        Please click the link below to verify your email:
        {link}
        """
        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=os.getenv('DEFAULT_FROM_EMAIL'),
            to=[user.email]
        )
        email.send()