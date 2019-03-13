from django.urls import path
from . import views

urlpatterns = [
    path('universities/', views.UniversitiesList.as_view()),
    path('universities/<str:nick>/', views.UniversityDetail.as_view()),
]