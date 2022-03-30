

from django.db import models

# Create your models here.

from user.models import UserModel



class Credit(models.Model):
    class Meta:
        db_table = "credits"


    mentor = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='+') # related_name='+' -> 역참조 무시
    credit = models.IntegerField(default=0)
    credit_date = models.DateTimeField(default=0)
    credit_type = models.BooleanField(default=True)  # 충전: True / 사용: False
