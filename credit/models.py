from datetime import datetime

from django.db import models

# Create your models here.
from django.utils.timezone import now

from user.models import UserModel



class Credit(models.Model):
    class Meta:
        db_table = "credits"

    now = datetime.now()
    mentoring_id = models.IntegerField(primary_key=True)
    mentor = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='+') # related_name='+' -> 역참조 무시
    credit = models.IntegerField()
    credit_date = models.DateTimeField(default=now.strftime('%Y-%m-%d %H:%M:%S'))
    credit_type = models.BooleanField(default=True)  # 충전: True / 사용: False

