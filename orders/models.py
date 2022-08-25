from django.db import models
from user_profile.models import User

#Academic writing options

ORDER_TYPE = [
    ("Academic Writing", "Academic Writing"),
    ("Programming Assignment", "Programming Assignment"),
    ("Calculations Assignment", "Calculations Assignment")
]

PAPER_LEVEL = [
    ("Advanced", "Advanced"),
    ("Standard", "Standard"),
    ("Basic", "Basic")
]

#Academic writing models

class Academic_Writing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_type = models.CharField(choices=ORDER_TYPE, default="Academic Writing", max_length=200)
    academic_year = models.CharField(max_length=200)
    deadline = models.CharField(max_length=200, null=True, blank=True)
    paper_level = models.CharField(choices=PAPER_LEVEL, default="Standard", max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)
    upgrade = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Academic_Writing'
        verbose_name_plural = 'Academic_Writing'

    def __str__(self):
        return self.order_type

class Academic_Writing_Detail(models.Model):
    order_type = models.ForeignKey(Academic_Writing, on_delete=models.CASCADE, null=True, blank=True)
    paper_type = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    pages = models.IntegerField(default=0, null=True, blank=True)
    charts = models.IntegerField(default=0, null=True, blank=True)
    slides = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Academic_Writing_Detail'
        verbose_name_plural = 'Academic_Writing_Details'

    def __str__(self):
        return self.paper_type

class Academic_Writing_Requirement(models.Model):
    order_type = models.ForeignKey(Academic_Writing, on_delete=models.CASCADE, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    instruction_file = models.FileField(null=True, blank=True)
    paper_format = models.CharField(max_length=200, null=True, blank=True)
    references = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Academic_Writing_Requirement'
        verbose_name_plural = 'Academic_Writing_Requirements'

    def __str__(self):
        return self.paper_format
