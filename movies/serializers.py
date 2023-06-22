

from rest_framework import serializers
from rest_framework.views import Request, Response, status, APIView
from rest_framework.validators import UniqueValidator
from user.models import User
from movies.models import Movie, MovieOrder


class MovieSerializer(serializers.ModelSerializer):
    added_by = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'rating', 'synopsis', 'added_by']


    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        user = self.context['request'].user
        movie = Movie.objects.create(user=user, **validated_data)
        return movie

class MovieOrderSerializer(serializers.Serializer):
    movie = serializers.IntegerField()
    user = serializers.IntegerField()
    buyed_at = serializers.DateTimeField(auto_now_add=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    title =serializers.CharField()

    def create(self, validated_data):
        buyed_by = self.context['request'].user
        movie_order = MovieOrder.objects.create(buyed_by=buyed_by.email, **validated_data)
        return movie_order