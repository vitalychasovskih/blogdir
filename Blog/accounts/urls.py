"""Определяет схему URL для пользователей"""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Включить URL авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
]
