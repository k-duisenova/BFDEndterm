# Generated by Django 3.2 on 2021-04-22 00:26

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='foodcategory',
            managers=[
                ('categories', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='fooditem',
            managers=[
                ('food_items', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]