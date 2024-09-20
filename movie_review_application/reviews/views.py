from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm, MovieForm


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = Review.objects.filter(movie=movie)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('movie_detail', pk=movie.pk)

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form
    })


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()

    return render(request, 'add_movie.html', {'form': form})
