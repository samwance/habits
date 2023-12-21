# Атомные привычки

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

### Технологии:
- Python 3.11
- Django 4.2.2
- Django REST framework 3.14.0
- PostgreSQL
- Celery 5.3.5
- Redis 5.0.1

### Инструкция по развертыванию проекта:


1. Клонируйте репозиторий: ```git clone https://github.com/samwance/habits```
2. Установите Docker и Docker Compose
3. Соберите и запустите Docker контейнеры: ```docker-compose up --build```
4. Перейдите по адресу http://localhost:8000
Запуск периодической задачи отправки в чат Telegram напоминания о выполнении привычки: 
```
celery -A config worker -l INFO -P eventlet  
```
```
celery -A config  beat -l info 
```
### Документация API
```
http://127.0.0.1:8000/docs/
```
