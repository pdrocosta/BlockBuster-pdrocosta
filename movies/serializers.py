

from rest_framework import serializers
from rest_framework.views import Request, Response, status, APIView
from rest_framework.validators import UniqueValidator
from user.models import User
from movies.models import Movie


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
