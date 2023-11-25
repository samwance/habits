from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (
    validate_frequency,
    validate_time_required,
    LinkedHabitValidator,
    PleasantHabitValidator,
    LinkedHabitOrRewardValidator,
)


class HabitSerializer(ModelSerializer):
    frequency = serializers.IntegerField(validators=[validate_frequency])
    time_required = serializers.IntegerField(validators=[validate_time_required])

    class Meta:
        model = Habit
        fields = (
            "user",
            "place",
            "time",
            "action",
            "is_pleasant",
            "linked_habit",
            "frequency",
            "reward",
            "time_required",
            "is_public",
        )

        validators = [
            LinkedHabitValidator(field="linked_habit"),
            PleasantHabitValidator(field="reward"),
            LinkedHabitOrRewardValidator(field="reward"),
        ]
