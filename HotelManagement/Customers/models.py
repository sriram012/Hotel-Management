from django.db import models
from django.contrib.auth.models import User


# Gender Options...
gender_options = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
)


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
    gender = models.CharField(choices=gender_options, max_length=10)

    # Number of visits...
    number_of_visits = models.IntegerField(default=0)

    class Meta:
        db_table = "Customers Details"
        order_with_respect_to = 'customer_id'

    def __str__(self):
        return self.user.username


# Notified Emails...
class NotifiedEmails(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'Emails to be notified'

    def __str__(self):
        return self.email
