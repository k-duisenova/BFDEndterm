from django.http import Http404
from rest_framework import viewsets, status
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

    def destroy(self, request, pk):
        try:
            instance = FoodCategory.objects.get(id=pk)
            instance.delete()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['PUT'], detail=False, permission_classes=(IsAuthenticated, ))
    def update(self, request, pk):
        category = FoodCategory.objects.get(id=pk)
        category.category_name = request.data['category_name']
        category.save()
        serializer = FoodCategorySerializer(category)
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

    def destroy(self, request, pk):
        try:
            instance = FoodItem.objects.get(id=pk)
            instance.delete()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def select(self, request, pk=None):
        queryset = FoodItem.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = FoodItemSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        food_item = FoodItem.objects.get(id=pk)
        food_item.item_name = request.data['item_name']
        food_item.price = request.data['price']
        food_item.description = request.data['description']
        category = FoodCategory.objects.get(category_name=request.data['category'])
        food_item.category = category
        food_item.save()
        serializer = FoodItemSerializer(food_item)
        return Response(serializer.data)