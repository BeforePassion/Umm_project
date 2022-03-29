# from django.db import models

# # Create your models here.
# from user.models import UserModel


# class ChatroomModel(models.Model):
#     class Meta:
#         db_table = "chatrooms"

#     mentor = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentor_id')
#     mentee = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentee_id')


# class ChattingModel(models.Model):
#     class Meta:
#         db_table = "chattings"

#     mentor = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentor')
#     mentee = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentee')
#     chatroom = models.ForeignKey(ChatroomModel, on_delete=models.CASCADE)
#     contents = models.CharField(max_length=255)
#     chat_time = models.CharField(max_length=255)

from django.db import models

from core.models import BaseModel


class Message(BaseModel):
    message = models.TextField()
    user = models.ForeignKey(
        "user.UserModel", related_name="messages", on_delete=models.CASCADE)
    chat_room = models.ForeignKey(
        "ChatRoom", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.username} : {self.message}"


class ChatRoom(BaseModel):
    participants = models.ManyToManyField(
        "user.UserModel", related_name="chatroom", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"