# Generated by Django 3.1.3 on 2021-06-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form1', '0003_form1_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1',
            name='qualified',
            field=models.IntegerField(default=-1),
        ),
    ]