from django.db import models

# Create your models here.
class Booking(models.Model):
    doc_name = models.CharField(max_length=20)
    doc_description = models.TextField()
    doc_image = models.ImageField(upload_to = "doctors")