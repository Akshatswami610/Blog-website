from django.core.mail import send_mail
from django.conf import settings

def send_otp_email(recipient: str, code: str):
    subject = "Your verification code"
    body    = f"Use this One-Time Password to verify your e-mail: {code}\n" \
              f"This code is valid for {settings.OTP_VALIDITY_MINUTES} minutes."
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [recipient],
        fail_silently=False,     # let exceptions bubble out for logging
    )
