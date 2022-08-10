from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(
        validators=[MinLengthValidator(1)], max_length=64,
        verbose_name="Имя", help_text="Укажите имя (длина символов 1–64)."
    )
    last_name = models.CharField(
        validators=[MinLengthValidator(1)], max_length=64,
        verbose_name="Фамилия", help_text="Укажите фамилию (длина символов 1–64)."
    )
    username = models.CharField(
        validators=[MinLengthValidator(6)], max_length=30, unique=True,
        verbose_name="Имя пользователя", help_text="Укажите имя пользователя (длина символов 6–30)."
    )
    email = models.EmailField(
        max_length=25, unique=True,
        verbose_name="Адрес электронной почты", help_text="Укажите адрес электронной почты."
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]

    def __str__(self):
        return self.username
