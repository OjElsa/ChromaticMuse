from django.http import HttpResponse
from django.shortcuts import render
from .models import Artwork
# Create your views here.


def index(request):
    Artworks = Artwork.objects.all()
    return render(request, 'index.html', { 'Artworks': Artwork})