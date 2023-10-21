from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Contacts(models.Model):
    first_name = models.CharField('first name', max_length=20)
    last_name = models.CharField('last name', max_length=20)
    email = models.EmailField("email")
    message = models.TextField('Message')

    def __str__(self):
        return self.first_name