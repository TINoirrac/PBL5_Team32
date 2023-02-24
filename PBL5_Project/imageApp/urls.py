from django.urls import path
from . import views

urlpatterns = [
    path('analyze_image', views.analyze_image, name='analyze_image'),
]
