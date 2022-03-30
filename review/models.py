from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from user.models import UserModel


class Review(models.Model):
    class Meta:
        db_table = "reviews"

    review_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    interest = models.CharField(max_length=256, default='',validators=[MinValueValidator(0), MaxValueValidator(3)])
    satisfaction = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_content = models.CharField(max_length=256, default='')
    review_date = models.DateTimeField(default=datetime.now)