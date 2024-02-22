from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('health/', views.health),
    path('metrics/', views.metrics),
    path('v1/tools/lookup/', views.lookup),
    path('v1/tools/validate/', views.validate),
    path('v1/history/', views.history),
]

