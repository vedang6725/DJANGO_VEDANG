from django.urls import path, include
from food import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('detail/', views.detail, name = 'detail'),
]
