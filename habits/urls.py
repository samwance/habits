from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    PublicHabitListAPIView,
    HabitListAPIView,
    HabitDeleteAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habits/", PublicHabitListAPIView.as_view(), name="habits"),
    path("my_habits/", HabitListAPIView.as_view(), name="my_habits"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/<int:pk>/delete/", HabitDeleteAPIView.as_view(), name="habit_delete"),
]
