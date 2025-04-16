from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    HomeView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Make this the home page
    path('movies/', MovieListView.as_view(), name='movie-list'),  # Move movie list to /movies/ URL
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/new/', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)