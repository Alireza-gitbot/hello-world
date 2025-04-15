from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Addresses")
    city = models.CharField(max_length=32, blank=True)
    zipcode = models.CharField(max_length=16)
    address = models.TextField()
    number = models.PositiveSmallIntegerField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)