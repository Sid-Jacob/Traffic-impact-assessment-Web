# Generated by Django 3.1.3 on 2021-06-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]