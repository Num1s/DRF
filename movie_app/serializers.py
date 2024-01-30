from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Director, Movie, Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = '__all__'

    def movies_count(self, director):
        return len([movie.movie for movie in director.movies.all()])
    
class MovieAndReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rating(self, movie):
        rating = sum([star.stars for star in movie.reviews.all()]) / len([star.stars for star in movie.reviews.all()])
        return rating
    
class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.DateTimeField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found!')
        
        return director_id
    
class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

class ReviewsValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie not found!')
        
        return movie_id