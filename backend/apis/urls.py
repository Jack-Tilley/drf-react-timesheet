from django.urls import path

from .views import ListTimeSheet, DetailTimeSheet

urlpatterns = [
    path('', ListTimeSheet.as_view()),
    path('<int:pk>/', DetailTimeSheet.as_view()),
]