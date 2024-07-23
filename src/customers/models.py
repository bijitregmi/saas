from django.db import models
from django.contrib.auth import get_user_model
from helpers.billing import create_customer
from allauth.account.signals import (
    user_signed_up as allauth_user_signed_up_signal,
    email_confirmed as allauth_email_confirmed_signal
)
from allauth.account.admin import EmailAddress
from django.dispatch import receiver

User = get_user_model()

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    init_email = models.EmailField(max_length=120, blank=True, null=True)
    init_email_confirmed = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}"
    
    def save (self, *args, **kwargs):
        if not self.stripe_id:
            if self.init_email and self.init_email_confirmed:
                email = self.user.email
                name = self.user.username
                if email != '' or email is not None:
                    stripe_id = create_customer(email=email, name=name)
                    self.stripe_id = stripe_id
        super().save(*args, **kwargs)

@receiver(allauth_user_signed_up_signal)
def allauth_user_signed_up_signal_handler(request, user, *args, **kwargs):
    email = user.email
    Customer.objects.create(
        user=user, 
        init_email=email,
        init_email_confirmed=EmailAddress.objects.filter(user=user, verified=True).exists()
        )

@receiver(allauth_email_confirmed_signal)
def allauth_email_confirmed_signal_handler(request, email_address, *args, **kwargs):
    qs = Customer.objects.filter(init_email=email_address.email, init_email_confirmed=False)
    for obj in qs:
        obj.init_email_confirmed = True
        obj.save()