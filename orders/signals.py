from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from orders.models import Academic_Writing
from user_profile.models import User
from dashboard.models import Recent_Orders

@receiver(post_save, sender=User)
def create_order(sender, instance, created, **kwargs):
    if created:
        Recent_Orders.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_order(sender, instance, **kwargs):
    instance.profile.save()