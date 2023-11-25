from django.core.exceptions import ValidationError

from habits.models import Habit


def validate_frequency(value):
    """
    Проверяет частоту привычки.
    """
    if value < 7:
        raise ValidationError("Частота привычки не может быть меньше 7 дней.")


def validate_time_required(value):
    """
    Проверяет необходимое время для привычки.
    """
    if value > 120:
        raise ValidationError("Необходимое время не должно превышать 120 секунд.")


class LinkedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        linked_habit = dict(value).get(self.field)
        if linked_habit is not None:
            habit = Habit.objects.get(pk=linked_habit.pk)

            if not habit.is_pleasant:
                raise ValidationError("Связанная привычка может быть только приятной.")


class PleasantHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        is_pleasant = dict(value).get("is_pleasant")
        tmp_val = dict(value).get(self.field)
        if is_pleasant and tmp_val is not None:
            raise ValidationError(
                "Приятная привычка не может иметь награду или связанную привычку."
            )


class LinkedHabitOrRewardValidator:
    """Проверка, что одновременно не назначено вознаграждение и связанная привычка"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        linked_habit = dict(value).get("linked_habit")
        reward = dict(value).get(self.field)
        if linked_habit is not None and reward is not None:
            raise ValidationError(
                "Нельзя одновременно выбрать вознаграждение и связанную привычку"
            )
