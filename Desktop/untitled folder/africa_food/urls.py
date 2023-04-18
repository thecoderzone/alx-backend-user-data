from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.getfood.as_view()),
]
