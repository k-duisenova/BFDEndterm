from rest_framework import serializers
from .models import FoodCategory, FoodItem


class FoodCategorySerializer(serializers.Serializer):
    category_name = serializers.CharField()

    def create(self, validated_data):
        foodCategory = FoodCategory.objects.create(category_name=validated_data.get('category_name'))
        return foodCategory

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.save()
        return instance

    def validate(self, data):
        if data['categoryName'] == '':
            raise serializers.ValidationError("category name should be written!")
        return data


class FoodItemSerializer(serializers.Serializer):
    item_name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()
    category = FoodCategorySerializer()

    def create(self, validated_data):
        category = FoodCategory.objects.get(category_name=validated_data.get('category')).id
        foodItem = FoodItem.objects.create(item_name=validated_data.get('item_name'),
                                           price=validated_data.get('price'),
                                           description=validated_data.get('description'),
                                           category=category)
        return foodItem

    def update(self, instance, validated_data):
        instance.item_name = validated_data.get('item_name', instance.item_name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

    def validate(self, data):
        if data['price'] < 0:
            raise serializers.ValidationError("price can't be negative number!")
        return data
