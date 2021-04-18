from django.urls import path
from main import views

urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>', views.CategoryViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('categories/<int:pk>/food', views.FoodViewSet.as_view({'get': 'retrieve'})),
    path('foods/', views.FoodViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('foods/<int:pk>', views.FoodViewSet.as_view({'delete': 'destroy', 'get': 'select', 'put': 'update'}))
]
