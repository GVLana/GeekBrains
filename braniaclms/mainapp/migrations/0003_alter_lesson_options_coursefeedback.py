# Generated by Django 4.1.2 on 2022-11-28 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_course_lesson_courseteacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('course', 'num'), 'verbose_name': 'урок', 'verbose_name_plural': 'уроки'},
        ),
        migrations.CreateModel(
            name='CourseFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(choices=[(5, '⭐⭐⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (3, '⭐⭐⭐'), (2, '⭐⭐'), (1, '⭐')], default=5, verbose_name='Рейтинг')),
                ('feedback', models.TextField(default='Без отзыва', verbose_name='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course', verbose_name='Курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Полльзователь')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]