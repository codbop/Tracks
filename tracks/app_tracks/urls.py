from django.urls import path
from app_tracks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracks/', views.tracks, name='tracks'),
    path('tracks/<str:genre>', views.tracks, name='tracks')
]

