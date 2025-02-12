from django.urls import path
from . import views

urlpatterns = [
    path('diarys/', views.DiaryView.as_view()),
    path('diarys/<str:id>/', views.DiaryDetailView.as_view())
    
]