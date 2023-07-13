# Generated by Django 4.2.2 on 2023-07-13 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communicationApp', '0003_alter_answer_autor_remove_answer_recommend_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(default='질문 내용', max_length=300, verbose_name='CONTENT'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='DATE'),
        ),
    ]
