from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieOrderSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.

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

class MovieDetailView(APIView):
    permission_classes = [IsAuthenticated | IsAdminUser]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=204)
    
    
class MovieOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        movie_order = serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=201)

