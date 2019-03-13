from django.urls import path
from . import views

urlpatterns = [
    path('airports/', views.AirportsList.as_view()),
    path('airports/<str:name>/', views.AirportDetail.as_view()),
]