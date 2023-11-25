from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user) | Habit.objects.filter(
            is_public=True
        )
        return queryset


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
    pagination_class = HabitPaginator

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class PublicHabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class HabitDeleteAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset
