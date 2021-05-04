from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    post_code = models.CharField(max_length=255, default="")
    def __str__(self):
        unserlines = "__________________________________________________________________________"
        underlines2 = (len(unserlines) - len(self.username)) * "_"
        return self.username + underlines2 + self.phone