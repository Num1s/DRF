from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Reviews
from .serializers import DirectorSerializer, MovieSerializer, ReviewsSerializer
from rest_framework import status


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data,
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie, many=False).data
    return Response(data=data,
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data,
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director, many=False).data
    return Response(data=data,
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Reviews.objects.all()
    data = ReviewsSerializer(reviews, many=True).data
    return Response(data=data,
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        review = Reviews.objects.get(id=id)
    except Reviews.DoesNotExist:
        return Response(data={'error': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewsSerializer(review, many=False).data
    return Response(data=data,
                    status=status.HTTP_200_OK)