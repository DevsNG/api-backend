from django.urls import path
from . import views

urlpatterns = [
    path('federal-ministries/', views.FederalMinistriesList.as_view()),
    path('federal-ministries/<str:name>/', views.FederalMinistryDetail.as_view()),
]