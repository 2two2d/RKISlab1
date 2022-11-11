import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager
from datetime import datetime, timedelta


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


class Question(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField(default=datetime.now(), editable=False)
    img = models.ImageField(null=True, upload_to="images/question")
    description = models.TextField(max_length=600, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    num_of_questions = models.IntegerField(null=False, default=2)

    num_of_questions = models.IntegerField(null=False)
    votes = models.IntegerField(default=0)
    voted_by = models.ManyToManyField(User, related_name='voted_by')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, null=True, )
    votes = models.IntegerField(default=0)


    def lestfuckinggo(self):
        return round(100 * self.votes / self.question.votes)

    def __str__(self):
        return self.choice_text
