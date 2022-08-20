from tabnanny import verbose
from django.db import models

# Create your models here.

#Academic writing models

class Academic_Writing(models.Model):
    order_type = models.CharField(max_length=200)
    academic_year = models.CharField(max_length=200)
    deadline = models.DateTimeField()

    class Meta:
        verbose_name = 'Academic_Writing'
        verbose_name_plural = 'Academic_Writing'

    def __str__(self):
        return self.order_type

class Academic_Writing_Detail(models.Model):
    order_type = models.ForeignKey(Academic_Writing, on_delete=models.CASCADE)
    paper_type = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    pages = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Academic_Writing_Detail'
        verbose_name_plural = 'Academic_Writing_Details'

    def __str__(self):
        return self.order_type.order_type

class Academic_Writing_Requirement(models.Model):
    order_type = models.ForeignKey(Academic_Writing, on_delete=models.CASCADE)
    instructions = models.TextField()
    instruction_file = models.FileField()
    paper_format = models.CharField(max_length=200)
    referrences = models.IntegerField()

    class Meta:
        verbose_name = 'Academic_Writing_Requirement'
        verbose_name_plural = 'Academic_Writing_Requirements'

    def __str__(self):
        return self.order_type.order_type