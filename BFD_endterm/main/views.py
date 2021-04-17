from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.models import FoodCategory, FoodItem
from main.serializers import FoodCategorySerializer, FoodItemSerializer
from django.shortcuts import get_object_or_404, get_list_or_404


class CategoryViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        queryset = FoodCategory.objects.all()
        serializer = FoodCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = FoodCategory.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = FoodCategorySerializer(user)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False, permission_classes=(IsAuthenticated,))
    def create(self, request):
        category_data = request.data
        new_category = FoodCategory.objects.create(category_name=category_data['category_name'])
        new_category.save()
        serializer = FoodCategorySerializer(new_category)
        return Response(serializer.data)


class FoodViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        queryset = FoodItem.objects.all()
        serializer = FoodItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = FoodItem.objects.filter(category=pk)
        user = get_list_or_404(queryset)
        serializer = FoodItemSerializer(user, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False, permission_classes=(IsAuthenticated,))
    def create(self, request):
        food_data = request.data
        category = FoodCategory.objects.get(category_name=food_data['category'])
        new_food = FoodItem.objects.create(item_name=food_data['item_name'], price=food_data['price'],
                                           description=food_data['description'], category=category)
        new_food.save()
        serializer = FoodItemSerializer(new_food)
        return Response(serializer.data)
