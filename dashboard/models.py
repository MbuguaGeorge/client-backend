from django.db import models
from user_profile.models import User
from orders.models import Academic_Writing
from django.db.models.signals import post_save

STATUS = [
    ("Recent", "Recent"),
    ("Canceled", "Canceled"),
    ("Finished", "Finished")
]

class Recent_Orders(models.Model):
    details = models.ForeignKey(Academic_Writing, on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=STATUS, default="Recent", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Recent_Order'
        verbose_name_plural = 'Recent_Orders'

    def __int__(self):
        return self.id

def create_order(sender, instance, created, **kwargs):
    if created:
        Recent_Orders.objects.create(details=instance)
        print('order created')

post_save.connect(create_order, sender=Academic_Writing)