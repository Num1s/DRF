from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Reviews
from .serializers import DirectorSerializer, MovieSerializer, ReviewsSerializer, MovieAndReviewsSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
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
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
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
        name = request.data.get('name')
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
        director.name = request.data.get('name')
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
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
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
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data={'reviews_id': review.id},
                        status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_reviews_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieAndReviewsSerializer(movies, many=True).data
    return Response(data=data,
                    status=status.HTTP_200_OK)