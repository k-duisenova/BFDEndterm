# Generated by Django 3.2 on 2021-04-12 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'ordering': ('id', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.user')),
            ],
            options={
                'verbose_name': 'админ',
                'verbose_name_plural': 'админы',
            },
            bases=('main.user',),
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='foods', to='main.foodcategory')),
            ],
            options={
                'ordering': ('item_name', 'price'),
            },
        ),
    ]
