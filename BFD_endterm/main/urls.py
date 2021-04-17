from django.urls import path
from main import views

urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>', views.CategoryViewSet.as_view({'get': 'retrieve'})),
    path('categories/<int:pk>/food', views.FoodViewSet.as_view({'get': 'retrieve'})),
    path('foods/', views.FoodViewSet.as_view({'get': 'list', 'post': 'create'}))
]