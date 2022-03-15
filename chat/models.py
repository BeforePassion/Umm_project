from django.db import models

# Create your models here.
from user.models import UserModel


class ChatroomModel(models.Model):
    class Meta:
        db_table = "chatrooms"

    mentor = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentor_id')
    mentee = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentee_id')


class ChattingModel(models.Model):
    class Meta:
        db_table = "chattings"

    mentor = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentor')
    mentee = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentee')
    chatroom = models.ForeignKey(ChatroomModel, on_delete=models.CASCADE)
    contents = models.CharField(max_length=255)
    chat_time = models.CharField(max_length=255)