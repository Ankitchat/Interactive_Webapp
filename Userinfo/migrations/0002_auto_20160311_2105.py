# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='QuestionInfo',
        ),
    ]
