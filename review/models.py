from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from user.models import UserModel


class Review(models.Model):
    class Meta:
        db_table = "reviews"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    interest = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    satisfaction = models.IntegerField(validators=[MaxValueValidator(5)])