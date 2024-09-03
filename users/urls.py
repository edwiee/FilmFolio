from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/edit/', views.edit_movie, name='edit_movie'),
    path('movies/<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
]