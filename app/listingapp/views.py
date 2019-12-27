from django.shortcuts import render
from django.http import HttpResponse
from tmdbv3api import TMDb
from tmdbv3api import Movie
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    popular_movies_list = get_popular_movies()
    paginator = Paginator(popular_movies_list, 20) # Show 20 movies per page
    page = request.GET.get('page')
    popular_movies = paginator.get_page(page)
    return render(request, 'lpv.html', {"popular_movies": popular_movies})

def get_popular_movies():
    tmdb = TMDb()
    tmdb.api_key = 'de1514eb58f4646ac43a38d1a8f4dcd3'
    
    movie = Movie()
    popular_movies = movie.popular(page=1)
    for i in range(2, 9):
        popular_movies = popular_movies + movie.popular(page=i)
    
    return popular_movies