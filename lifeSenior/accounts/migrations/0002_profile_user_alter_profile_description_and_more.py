# Generated by Django 4.2.2 on 2023-07-05 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(default='안녕하세요! 아기사자입니다.', max_length=30, verbose_name='DESCRIPTION'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/img/defaultImg.png', upload_to='userProfile/', verbose_name='IMAGE'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='baby lion', max_length=20, verbose_name='NAME'),
        ),
    ]
