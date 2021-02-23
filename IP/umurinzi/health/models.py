from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime as dt

class Location(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Insurance(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Pharmacy(models.Model):
    name=models.CharField(max_length=100)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    insurance = models.ManyToManyField(Insurance)
    direction = models.CharField(max_length=255)
    contact = models.PositiveIntegerField()

    def create_pharm(self):
        self.save()

    def delete_pharm(self):
        self.delete()

    @classmethod
    def find_pharm(cls, pharm_id):
        paharm= cls.objects.get(id=pharm_id)
        return pharm

    def __str__(self):
        return self.name
    location = models.CharField(max_length=255)
    contact = models.PositiveIntegerField()

    def create_pharm(self):
        self.save()

    def delete_pharm(self):
        self.delete()

    @classmethod
    def find_pharm(cls, pharm_id):
        paharm= cls.objects.get(id=pharm_id)
        return pharm

    def __str__(self):
        return self.name

class Drug(models.Model):
    name=models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    # price = models.PositiveIntegerField()
    pic=models.ImageField(upload_to='pictures/')
    pharmacy=models.ManyToManyField(Pharmacy)

    def save_drug(self):
        self.save()

    def delete_drug(self):
        self.delete()

    @classmethod
    def search(cls,searchterm):
        search = Drug.objects.filter(Q(name__icontains=searchterm)|Q(description__icontains=searchterm))
        return search

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profiles/',default='profiles/default.png')
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username
