from django.db.models.signals import post_save
from django.dispatch import receiver
from auth_.models import User, Profile
from main.models import CreditCard, Order


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        CreditCard.objects.create(customer=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Order)
def notify_user(sender, instance, **kwargs):
    print(instance.price)
