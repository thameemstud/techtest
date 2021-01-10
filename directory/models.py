from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    profilePicture = models.ImageField(default='default.jpg',upload_to='profile_pics')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=150)
    roomNumber = models.CharField(max_length=150)
    subject = models.ManyToManyField(Subject, null=True, blank=True)
    dateCreated = models.DateTimeField(default=timezone.now)
    dateUpdated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        ordering = ["-dateCreated"]

