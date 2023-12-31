# Generated by Django 4.2.5 on 2023-09-28 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=50)),
                ('re_mobile', models.CharField(max_length=50)),
                ('laptop', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=100)),
                ('textarea', models.CharField(max_length=250)),
                ('checkbox', models.BooleanField(max_length=50)),
                ('ram', models.IntegerField()),
                ('ssd', models.CharField(max_length=50)),
                ('youtube_chanel', models.BooleanField(max_length=50)),
            ],
        ),
    ]
