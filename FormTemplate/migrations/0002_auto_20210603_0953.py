# Generated by Django 3.1.3 on 2021-06-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormTemplate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtemplate',
            name='userName1',
            field=models.CharField(default='default-username', max_length=100),
        ),
        migrations.AddField(
            model_name='formtemplate',
            name='userName2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]