# Generated by Django 4.2.1 on 2023-05-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.TextField(max_length=200),
        ),
    ]