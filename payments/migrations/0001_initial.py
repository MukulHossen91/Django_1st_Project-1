# Generated by Django 4.2.5 on 2023-09-26 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pay_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_id', models.IntegerField()),
                ('pay_option', models.CharField(max_length=30)),
                ('min_pay', models.IntegerField()),
            ],
        ),
    ]