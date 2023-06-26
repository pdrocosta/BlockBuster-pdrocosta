

from rest_framework import serializers
from rest_framework.views import Request, Response, status, APIView
from rest_framework.validators import UniqueValidator
from user.models import User
from movies.models import Movie, MovieOrder


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'rating', 'synopsis', 'user']

    def get_user(self, obj):
        return obj.user_id

    def create(self, validated_data):
        user = self.context['request'].user
        movie = Movie.objects.create(user=user, **validated_data)
        return movie

class MovieOrderSerializer(serializers.ModelSerializer):
    buyed_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MovieOrder
        fields = ['movie', 'buyed_by', 'buyed_at', 'price', 'title']

    def create(self, validated_data):
        buyed_by = self.context['request'].user
        movie_order = MovieOrder.objects.create(buyed_by=buyed_by, **validated_data)
        return movie_order

