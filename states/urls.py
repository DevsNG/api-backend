from django.urls import path
from . import views

urlpatterns = [
    path('states/', views.StatesList.as_view()),
    path('states/<str:name>/', views.StateDetail.as_view()),
]