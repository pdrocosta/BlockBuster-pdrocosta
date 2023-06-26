from rest_framework import serializers
from rest_framework.views import Request, Response, status, APIView
from rest_framework.validators import UniqueValidator
from user.models import User
from movies.models import Movie, MovieOrder


class MovieSerializer(serializers.ModelSerializer):
    added_by = serializers.SerializerMethodField(read_only=True)
    synopsis = serializers.CharField(allow_null = True)
    rating = serializers.CharField(allow_null = True)
    duration = serializers.CharField(allow_null = True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'rating', 'synopsis', 'added_by']

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        user = self.context['request'].user
        movie = Movie.objects.create(user=user, **validated_data)
        return movie


class MovieOrderSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='movie.title')
    buyed_by = serializers.ReadOnlyField(source='buyed_by.email')
    buyed_at = serializers.ReadOnlyField()

    class Meta:
        model = MovieOrder
        fields = ['id', 'title', 'price', 'buyed_by', 'buyed_at']

    def create(self, validated_data):
        buyed_by = self.context['request'].user
        movie_order = MovieOrder.objects.create(buyed_by=buyed_by, **validated_data)
        return movie_order

