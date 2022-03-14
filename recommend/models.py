from django.db import models


# Create your models here.
from user.models import UserModel


class Lecture(models.Model):
    class Meta:
        db_table = "lectures"
    name = models.CharField(max_length=40)


class Recommend(models.Model):
    class Meta:
        db_table = "recommends"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)



