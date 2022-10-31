from django.db import models
from django.db.models.signals import post_save
from orders.models import Academic_Writing

STATUS = [
    ("Recent", "Recent"),
    ("Canceled", "Canceled"),
    ("Finished", "Finished"),
    ("Revised", "Revised")
]

class Recent_Orders(models.Model):
    details = models.ForeignKey(Academic_Writing, on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=STATUS, default="Recent", max_length=200, blank=True, null=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Recent_Order'
        verbose_name_plural = 'Recent_Orders'

    def __int__(self):
        return self.id

# Signal to create an order when an instance of Academic_Writing model is created
def create_order(sender, instance, created, **kwargs):
    if created:
        Recent_Orders.objects.create(details=instance)
        print('order created')

post_save.connect(create_order, sender=Academic_Writing)
