# Generated by Django 4.2.2 on 2023-07-10 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='user',
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct',
            field=models.PositiveIntegerField(default=0, verbose_name='CORRECT'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='content',
            field=models.TextField(verbose_name='CONTENT'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10, verbose_name='TEXT')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.quiz')),
            ],
        ),
    ]
