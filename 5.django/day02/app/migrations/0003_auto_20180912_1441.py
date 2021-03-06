# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-12 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180912_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=10, unique=True, verbose_name='班级名称')),
            ],
            options={
                'db_table': 'grade',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stu', to='app.StudentInfo'),
        ),
        migrations.AddField(
            model_name='student',
            name='g',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Grade'),
        ),
    ]
