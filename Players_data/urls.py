from django.urls import path
from .import views

urlpatterns=[
    path('avgscore',views.AverageScore.as_view()),
    path('filterscore/<int:score>',views.PlayerName.as_view())
]
