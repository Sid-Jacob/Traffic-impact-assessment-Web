# Generated by Django 3.1.3 on 2021-06-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form1', '0004_form1_qualified'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1',
            name='form2_send',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='form1',
            name='need_examine',
            field=models.BooleanField(default=False),
        ),
    ]