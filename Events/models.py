from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from PIL import Image


# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    region = models.CharField('region', max_length=60, null= True)
    address = models.CharField(max_length=50)
    zip_code = models.CharField('zip code',max_length=60,)
    website = models.CharField('Website Adress',max_length=60,blank=True)
    phone_number = models.CharField('Contact number',max_length=12,blank=True)
    email_address = models.EmailField('Email Address',blank=True)



    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    email= models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name




class Event(models.Model):
    name = models.CharField('Event name', max_length=120)
    event_date = models.DateTimeField('Event date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # photo = models.ImageField(default='default1.jpg', upload_to='uploads')
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank='True')
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


