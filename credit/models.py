from django.db import models

# Create your models here.
from user.models import UserModel


class Credit(models.Model):
    class Meta:
        db_table = "credits"

    mentor = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    credit = models.IntegerField()
    credit_date = models.IntegerField()
    credit_use = models.IntegerField()