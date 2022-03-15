from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import datetime

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if not email:
            raise ValueError("제대로 된 이메일 형식이 아닙니다 ;)")


        email = self.normalize_email(email)
        user = self.model(email=email)
        username = self.model.normalize_username(username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, username):
        """Create a new superuser profile"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserModel(AbstractUser):
    Mentor = 'mentor'
    Mentee = 'mentee'
    user_type_choices = [
        (Mentor, 'mentor'),
        (Mentee, 'mentee'),
    ]
    user_type = models.CharField(max_length=8, choices=user_type_choices, default=Mentee)
    experience = models.CharField(max_length=8)
    email = models.EmailField(max_length=255, unique=True)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "user"

    is_deleted = models.BooleanField(default=False, verbose_name="delete or not")

    deleted_at = models.DateTimeField(null=True)

    def delete(self, using=None, keep_parent=False):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def __str__(self):
        return self.email
