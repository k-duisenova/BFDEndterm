# Generated by Django 3.2 on 2021-04-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
