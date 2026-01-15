from django.core.mail import EmailMessage
import os


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