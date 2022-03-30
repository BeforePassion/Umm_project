from django.db import models


# Create your models here.
from user.models import UserModel


class Lecture(models.Model):
    class Meta:
        db_table = "lectures"

    img = models.CharField(max_length=60)
    title = models.CharField(max_length=80)
    url = models.CharField(max_length=80)
    type = models.CharField(max_length=60)


class Recommend(models.Model):
    class Meta:
        db_table = "recommends"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)



