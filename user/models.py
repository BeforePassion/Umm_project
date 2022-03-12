from django.db import models

# Create your models here.


class UserModel(models.Model):
    class Meta:
        db_table = "users"

    USER_TYPE_CHOICES = (
        ('Mentor', 'Mentor'),
        ('Mentee', 'Mentee')
    )

    EXPERIENCE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10+', '10+')
    )

    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=50)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=6)
    experience = models.CharField(choices=EXPERIENCE_CHOICES, max_length=3)
    is_deleted = models.BooleanField(default=False)