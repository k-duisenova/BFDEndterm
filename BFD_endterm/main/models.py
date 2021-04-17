from django.db import models


class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name + self.email

    class Meta:
        verbose_name = 'Пользователь'
        ordering = ('id', 'name')


class Admin(User):

    def __str__(self):
        return self.name + self.login

    class Meta:
        verbose_name = 'админ'
        verbose_name_plural = 'админы'


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class FoodItem(models.Model):
    item_name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.RESTRICT, related_name='foods')

    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ('item_name', 'price')
