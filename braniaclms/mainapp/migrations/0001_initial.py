# Generated by Django 4.1.2 on 2022-10-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('preamble', models.CharField(max_length=1024, verbose_name='Вступление')),
                ('body', models.TextField(verbose_name='Содержание')),
                ('body_as_markdown', models.BooleanField(default=False, verbose_name='Разметка в формате Markdown')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
        ),
    ]
