from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Reviews
from .serializers import DirectorSerializer, MovieSerializer, ReviewsSerializer, MovieAndReviewsSerializer, MovieValidateSerializer, DirectorValidateSerializer, ReviewsValidateSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data={'movies_id': movies.id},
                        status=status.HTTP_201_CREATED)
    
        

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        data = MovieSerializer(movie, many=False).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.save()
        return Response(data={'movies_id': movie.id},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
        directors = Director.objects.create(name=name)
        return Response(data={'directors_id': directors.id}, 
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(director, many=False).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data={'directors_id': director.id},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Reviews.objects.all()
        data = ReviewsSerializer(reviews, many=True).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewsValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        reviews = Reviews.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data={'reviews_id': reviews.id},
                        status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = Reviews.objects.get(id=id)
    except Reviews.DoesNotExist:
        return Response(data={'error': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        data = ReviewsSerializer(review, many=False).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ReviewsValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie_id')
        review.stars = serializer.validated_data.get('stars')
        review.save()
        return Response(data={'reviews_id': review.id},
                        status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_reviews_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieAndReviewsSerializer(movies, many=True).data
    return Response(data=data,
                    status=status.HTTP_200_OK)