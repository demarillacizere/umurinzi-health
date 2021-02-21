from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime as dt

class Pharmacy(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=40)
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
    pharmacy=models.ForeignKey(Pharmacy, on_delete=models.CASCADE, null=True)

    def save_drug(self):
        self.save()

    def delete_drug(self):
        self.delete()

    def __str__(self):
        return self.name



