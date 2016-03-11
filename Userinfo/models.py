from django.db import models


# Create your models here.


class UserInfo(models.Model):
    UserId = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=1000)
    Email = models.EmailField(max_length=1000)
    Zip = models.IntegerField()

    def __str__(self):
        return self.FullName


class QuestionInfo(models.Model):
    QId = models.AutoField(primary_key=True)
    Question = models.TextField()

    def __str__(self):
        return self.Question


class Poll(models.Model):
    answerto = models.ForeignKey(QuestionInfo, default=1)
    Choice = models.CharField(max_length=10000)
    Score = models.IntegerField(default=0)

    def __str__(self):
        return self.Choice
