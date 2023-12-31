# Generated by Django 4.2.2 on 2023-07-10 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communicationApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='답변 내용', max_length=50, verbose_name='CONTENT')),
                ('image', models.ImageField(default='static/img/defaultImg.png', upload_to='questionAnswer/', verbose_name='IMAGE')),
                ('recommend', models.PositiveIntegerField(default=0, verbose_name='RECOMMEND')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='댓글입력', max_length=20, verbose_name='CONTENT')),
                ('date', models.DateField(auto_now_add=True, verbose_name='DATE')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='질문 제목', max_length=20, verbose_name='TITLE')),
                ('content', models.TextField(default='질문 내용', max_length=50, verbose_name='CONTENT')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='DATE')),
                ('recommend', models.PositiveIntegerField(default=0, verbose_name='RECOMMEND')),
                ('category', models.CharField(max_length=10, verbose_name='CATEGORY')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='VIEWS')),
                ('answerd', models.BooleanField(default=False, verbose_name='ANSWERD')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communicationApp.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communicationApp.question'),
        ),
    ]
