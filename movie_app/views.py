from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Director, Movie, Reviews
from .serializers import DirectorSerializer, MovieSerializer, ReviewsSerializer, MovieAndReviewsSerializer, MovieValidateSerializer, DirectorValidateSerializer, ReviewsValidateSerializer
from rest_framework import status


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data={'movies_id': movies.id},
                        status=status.HTTP_201_CREATED)
    

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            movie = Movie.objects.get(id=kwargs.get('id'))
        except Movie.DoesNotExist:
            return Response(data={'Error': 'Movie not found'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.save()
        return Response(data={'movies_id': movie.id},
                        status=status.HTTP_201_CREATED)


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
        directors = Director.objects.create(name=name)
        return Response(data={'directors_id': directors.id}, 
                        status=status.HTTP_201_CREATED)


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            director = Director.objects.get(id=kwargs.get('id'))
        except Director.DoesNotExist:
            return Response(data={'error': 'Director not found'},
                            status=status.HTTP_404_NOT_FOUND)
        
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data={'directors_id': director.id},
                        status=status.HTTP_201_CREATED)


class ReviewsListCreateAPIView(ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = ReviewsValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        reviews = Reviews.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data={'reviews_id': reviews.id},
                        status=status.HTTP_201_CREATED)


class ReviewsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            review = Reviews.objects.get(id=kwargs.get('id'))
        except Reviews.DoesNotExist:
            return Response(data={'error': 'Review not found'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewsValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie_id')
        review.stars = serializer.validated_data.get('stars')
        review.save()
        return Response(data={'reviews_id': review.id},
                        status=status.HTTP_201_CREATED)
        
class MovieReviewsListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAndReviewsSerializer
    pagination_class = PageNumberPagination