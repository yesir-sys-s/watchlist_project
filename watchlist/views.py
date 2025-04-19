from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Movie

class HomeView(TemplateView):
    template_name = 'watchlist/home.html'

class MovieListView(ListView):
    model = Movie
    template_name = 'watchlist/movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'watchlist/movie_detail.html'

class MovieCreateView(CreateView):
    model = Movie
    template_name = 'watchlist/movie_form.html'
    fields = ['title', 'description', 'watched', 'poster']
    success_url = reverse_lazy('movie-list')

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'watchlist/movie_form.html'
    fields = ['title', 'description', 'watched', 'poster']
    success_url = reverse_lazy('movie-list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'watchlist/movie_confirm_delete.html'
    success_url = reverse_lazy('movie-list')

class ToggleWatchedView(View):
    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.watched = not movie.watched
        movie.save()
        return redirect('movie-list')