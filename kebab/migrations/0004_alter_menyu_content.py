# Generated by Django 3.2.9 on 2021-12-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kebab', '0003_auto_20211126_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menyu',
            name='content',
            field=models.TextField(default=0),
        ),
    ]
