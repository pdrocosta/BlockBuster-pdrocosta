from django.contrib import admin
from django.urls import path
from user.views import UserView, UserDetailView
from movies.views import MovieView ,MovieDetailView, MovieOrderView
from rest_framework_simplejwt import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", UserView.as_view()),
    path("api/users/<int:user_id>/", UserDetailView.as_view()),
    path("api/users/login/", views.TokenObtainPairView.as_view()),
    path("api/users/login/refresh", views.TokenRefreshView.as_view()),
    path("api/movies/", MovieView.as_view()),
    path("api/movies/<int:movie_id>/", MovieDetailView.as_view()),
    path("api/movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]
