# Generated by Django 3.2.4 on 2021-07-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_twitternew'),
    ]

    operations = [
        migrations.CreateModel(
            name='fbautoNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faceuser', models.CharField(max_length=100)),
                ('facepassword', models.CharField(max_length=100)),
                ('facepath', models.ImageField(upload_to='')),
                ('facecaption', models.CharField(max_length=100)),
            ],
        ),
    ]