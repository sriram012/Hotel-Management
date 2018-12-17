from django.db import models
from django.contrib.auth.models import User
from RoomsManagement.models import Room as AssignedRooms
from datetime import datetime, timedelta


# Address...
class Address(models.Model):
    country = models.CharField(max_length=20, blank=False)
    state = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    street = models.CharField(max_length=40, blank=False)
    house_number = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.country + ', ' + self.city


# Contact_Details...
class ContactDetails(models.Model):
    phone_number = models.BigIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.email + ', ' + str(self.phone_number)


# Customers Database...
class Customers(models.Model):

    # Customer Personals...
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=10, blank=False)
    contact_details = models.OneToOneField(ContactDetails, on_delete=models.CASCADE)

    # Room Assigned...
    room_assigned = models.OneToOneField(AssignedRooms, on_delete=models.CASCADE)
    room_assigned_time = models.DateTimeField(editable=False, default=datetime.now())
    room_assigned_hours = models.IntegerField(blank=False)

    # Number of visits...
    number_of_visits = models.IntegerField(default=0)

    class Meta:
        db_table = "Customers Details"
        order_with_respect_to = 'customer_id'

    def __str__(self):
        return self.user.username + ' ( ' + str(self.room_assigned_time)\
               + ', ' + str(self.room_assigned_hours) + 'hrs )'
