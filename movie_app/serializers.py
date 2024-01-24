from rest_framework import serializers
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