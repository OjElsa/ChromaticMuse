from django.http import HttpResponse
from django.shortcuts import render
from .models import Artwork
# Create your views here.


def index(request):
    artworks = Artwork.objects.all()
    return render(request, 'Artworks/index.html', { 'Artworks': artworks})


def detail(request, Artwork_id):
    Artwork = Artwork.object.get(pk=Artwork_id)
    return render(request, 'Artwork/detail.html', {'Artwork': Artwork})