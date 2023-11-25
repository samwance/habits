from django.db import models
from users.models import User

NULL = {"null": True, "blank": True}

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False)
    linked_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, **NULL
    )
    frequency = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=255, **NULL)
    time_required = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"
