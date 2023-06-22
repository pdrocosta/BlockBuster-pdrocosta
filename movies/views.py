from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.response import Response

# Create your views here.
class MovieDetailView(APIView):
    permission_classes = [IsAuthenticated | IsAdminUser]

    def get(self, request, movie_id):
        movie=Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return Response(status=204)
    
class MovieView(APIView):
    permission_classes = [IsAuthenticated | IsAdminUser]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        movie = serializer.save(user=request.user)
        return Response(serializer.data, status=201)