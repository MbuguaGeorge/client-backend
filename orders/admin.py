from django.contrib import admin
from orders.models import Academic_Writing, Academic_Writing_Detail, Academic_Writing_Requirement

# Register your models here.
admin.site.register(Academic_Writing)
admin.site.register(Academic_Writing_Requirement)
admin.site.register(Academic_Writing_Detail)