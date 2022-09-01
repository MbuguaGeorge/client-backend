from django.db import models
from user_profile.models import User

#Academic writing options

#Academic writing models

class Academic_Writing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_type = models.CharField(max_length=200, null=True, blank=True)
    academic_year = models.CharField(max_length=200, null=True, blank=True)
    deadline = models.CharField(max_length=200, null=True, blank=True)
    paper_level = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    upgrade = models.CharField(max_length=200, null=True, blank=True)
    paper_type = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    pages = models.IntegerField(default=0, null=True, blank=True)
    charts = models.IntegerField(default=0, null=True, blank=True)
    slides = models.IntegerField(default=0, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    instruction_file = models.FileField(null=True, blank=True)
    paper_format = models.CharField(max_length=200, null=True, blank=True)
    references = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    amount = models.CharField(max_length=200, null=True, blank=True)
    prog_language = models.CharField(max_length=200, null=True, blank=True)
    programming_category = models.CharField(max_length=200, null=True, blank=True)
    task_size = models.CharField(max_length=200, null=True, blank=True)
    software = models.CharField(max_length=200, null=True, blank=True)
    discipline = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Academic_Writing'
        verbose_name_plural = 'Academic_Writing'

    def __str__(self):
        return self.order_type