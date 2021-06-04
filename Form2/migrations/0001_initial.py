# Generated by Django 3.1.3 on 2021-06-02 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FormTemplate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form2',
            fields=[
                ('formtemplate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='FormTemplate.formtemplate')),
                ('expertCategory', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('expertNum', models.IntegerField()),
                ('assessTime', models.DateField()),
            ],
            bases=('FormTemplate.formtemplate',),
        ),
    ]