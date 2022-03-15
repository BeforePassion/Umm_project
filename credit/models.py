from django.db import models

# Create your models here.
from user.models import UserModel


class Credit(models.Model):
    class Meta:
        db_table = "credits"


    mentoring_id = models.IntegerField(primary_key=True)
    mentor_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    credit = models.IntegerField()
    credit_date = models.IntegerField()
    credit_use = models.IntegerField()
    credit_history = models.CharField(max_length=255, default="join")
