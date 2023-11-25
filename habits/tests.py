from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="user@test.com", password="test")
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="test",
            time="20:30:00",
            action="test",
            frequency=7,
            reward="test",
            time_required=20,
            is_public=True,
        )

    def test_list(self):
        """Тестирование вывода списка привычек пользователя"""
        response = self.client.get(reverse("habits:my_habits"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "user": self.user.pk,
                        "place": self.habit.place,
                        "time": self.habit.time,
                        "action": self.habit.action,
                        "is_pleasant": False,
                        "linked_habit": None,
                        "frequency": self.habit.frequency,
                        "reward": self.habit.reward,
                        "time_required": self.habit.time_required,
                        "is_public": self.habit.is_public,
                    }
                ],
            },
        )

    def test_public_list(self):
        """Тестирование вывода списка уроков"""
        response = self.client.get(reverse("habits:habits"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "user": self.user.pk,
                        "place": self.habit.place,
                        "time": self.habit.time,
                        "action": self.habit.action,
                        "is_pleasant": False,
                        "linked_habit": None,
                        "frequency": self.habit.frequency,
                        "reward": self.habit.reward,
                        "time_required": self.habit.time_required,
                        "is_public": self.habit.is_public,
                    }
                ],
            },
        )

    def test_retrieve(self):
        """Тестирование вывода одного урока"""
        response = self.client.get(
            reverse("habits:habit_retrieve", kwargs={"pk": self.habit.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print(response.json())

        self.assertEqual(
            response.json(),
            {
                "user": self.user.pk,
                "place": self.habit.place,
                "time": self.habit.time,
                "action": self.habit.action,
                "is_pleasant": False,
                "linked_habit": None,
                "frequency": self.habit.frequency,
                "reward": self.habit.reward,
                "time_required": self.habit.time_required,
                "is_public": self.habit.is_public,
            },
        )

    def test_create(self):
        """Тестирование создания привычки"""
        data = {
            "user": self.user.pk,
            "place": "test",
            "time": "20:00:00",
            "action": "test",
            "frequency": "8",
            "reward": "test",
            "time_required": "21",
            "is_public": True,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        print(response.json())

        self.assertEqual(
            response.json(),
            {
                "user": self.user.pk,
                "place": "test",
                "time": "20:00:00",
                "action": "test",
                "is_pleasant": False,
                "linked_habit": None,
                "frequency": 8,
                "reward": "test",
                "time_required": 21,
                "is_public": True,
            },
        )

    def test_update(self):
        """Тестирование обновления урока"""
        data = {
            "action": "test_upd",
        }

        response = self.client.patch(
            reverse("habits:habit_update", kwargs={"pk": self.habit.pk}), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "user": self.user.pk,
                "place": self.habit.place,
                "time": self.habit.time,
                "action": "test_upd",
                "is_pleasant": False,
                "linked_habit": None,
                "frequency": self.habit.frequency,
                "reward": self.habit.reward,
                "time_required": self.habit.time_required,
                "is_public": self.habit.is_public,
            },
        )

    def test_delete(self):
        """Тестирование удаления урока"""
        response = self.client.delete(
            reverse("habits:habit_delete", kwargs={"pk": self.habit.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class HabitValidationTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="user@test.com", password="test")
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="test",
            time="20:30:00",
            action="test",
            frequency=7,
            reward="test",
            time_required=20,
            is_public=True,
        )

    def test_frequency_error_create(self):
        """Тестирование ошибки частоты выполнения привычки"""
        data = {
            "user": self.user.pk,
            "place": "test",
            "time": "20:00:00",
            "action": "test",
            "frequency": "6",
            "reward": "test",
            "time_required": "21",
            "is_public": True,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_time_required_error_create(self):
        """Тестирование времени на выполнение  привычки"""
        data = {
            "user": self.user.pk,
            "place": "test",
            "time": "20:00:00",
            "action": "test",
            "frequency": "8",
            "reward": "test",
            "time_required": "121",
            "is_public": True,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_linked_habit_error_create(self):
        """Тестирование связанной привычки"""
        data = {
            "user": self.user.pk,
            "place": "test",
            "time": "20:00:00",
            "action": "test",
            "frequency": "8",
            "time_required": "20",
            "is_public": True,
            "linked_habit": self.habit.pk,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_plesant_habit_error_create(self):
        """Тестирование приятной привычки"""
        data = {
            "user": self.user.pk,
            "place": "test",
            "time": "20:00:00",
            "action": "test",
            "frequency": "8",
            "reward": "test",
            "time_required": "20",
            "is_public": True,
            "is_pleasant": True,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_linked_habit_or_reward_error_create(self):
        """Тестирование приятной привычки и награды"""
        data = {
            "user": self.user.pk,
            "place": "test",
            "time": "20:00:00",
            "action": "test",
            "frequency": "8",
            "reward": "test",
            "time_required": "20",
            "is_public": True,
            "linked_habit": self.habit.pk,
        }

        response = self.client.post(reverse("habits:habit_create"), data=data)

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
