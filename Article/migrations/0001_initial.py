# Generated by Django 3.1.3 on 2020-12-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('link', models.CharField(blank=True, max_length=1000, null=True, verbose_name='原始url')),
                ('imglink', models.CharField(blank=True, max_length=1000, null=True, verbose_name='图片url')),
                ('essay', models.TextField(blank=True, null=True, verbose_name='正文')),
                ('date', models.CharField(blank=True, max_length=100, null=True, verbose_name='新闻日期')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章列表',
                'db_table': 'Article',
            },
        ),
    ]
