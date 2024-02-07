from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('movies/reviews/', views.MovieReviewsListAPIView.as_view()),
    path('reviews/', views.ReviewsListCreateAPIView.as_view()),
    path('reviews/<int:id>', views.ReviewsDetailAPIView.as_view())
]