from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView


# Create your views here.

class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer

class HabitDeleteAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
