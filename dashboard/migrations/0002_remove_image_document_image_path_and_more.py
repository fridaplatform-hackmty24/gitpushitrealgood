# Generated by Django 4.2.13 on 2024-09-15 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='document',
        ),
        migrations.AddField(
            model_name='image',
            name='path',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='uploaded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
