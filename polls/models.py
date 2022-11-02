import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    full_name = models.CharField(max_length=50, help_text="Напишите ФИО")
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=254)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, upload_to="images/profile")

    USERNAME_FIELD = 'username'  # Идентификатор для обращения
    REQUIRED_FIELDS = ['email']  # Список имён полей для Superuser

    objects = UserManager()

    def __str__(self):
        return self.username

class Choice(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    img = models.ImageField(null=True, upload_to="images/profile")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, null=True,)
    description = models.TextField(max_length=600, null=True,)
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return self.choice_text