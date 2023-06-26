from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieOrderSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class MovieView(APIView, PageNumberPagination):
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def get(self, request):
        movies = Movie.objects.all().order_by("id")
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
class MovieDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=200)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=204)
    
class MovieOrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, buyed_by=request.user)
        return Response(serializer.data, status=201)

