# from django.db import models
# from user_profile.models import User
# from orders.models import Academic_Writing

# STATUS = [
#     ("Recent", "Recent"),
#     ("Canceled", "Canceled"),
#     ("Finished", "Finished")
# ]

# class Recent_Orders(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order = models.ForeignKey(Academic_Writing, on_delete=models.CASCADE)
#     status = models.CharField(choices=STATUS, default="Recent", max_length=200)
#     amount = models.DecimalField(max_digits=6, decimal_places=2)

#     class Meta:
#         verbose_name = 'Recent_Order'
#         verbose_name_plural = 'Recent_Orders'

#     def __int__(self):
#         return self.id