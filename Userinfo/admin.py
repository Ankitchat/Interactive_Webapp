from django.contrib import admin
from django.db import models
from .models import UserInfo, QuestionInfo, Poll
# Register your models here.


class RegUserInfo(admin.ModelAdmin):
    pass

admin.site.register(UserInfo, RegUserInfo)


class RegQuestion(admin.ModelAdmin):
    pass

admin.site.register(QuestionInfo, RegQuestion)


class RegPoll(admin.ModelAdmin):
    pass

admin.site.register(Poll, RegPoll)
