from django.db import models
from django.core.validators import MinLengthValidator, int_list_validator

# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=200, unique=True)
    street_name = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    postcode = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10, validators=[int_list_validator(sep=''), MinLengthValidator(10), ])

    def __str__(self):
        return self.client_name
