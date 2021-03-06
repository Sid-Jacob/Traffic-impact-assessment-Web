# Generated by Django 3.1.3 on 2021-07-07 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FormTemplate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('reportId', models.AutoField(primary_key=True, serialize=False)),
                ('report', models.TextField()),
                ('userId', models.IntegerField(verbose_name='报告撰写用户id')),
                ('userName', models.CharField(default='default-username', max_length=100)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('formId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FormTemplate.formtemplate')),
            ],
        ),
    ]
