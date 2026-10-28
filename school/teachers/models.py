from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='teacher_images/', blank=True, null=True)

    def __str__(self):
        return (f"{self.name} - {self.subject}")
