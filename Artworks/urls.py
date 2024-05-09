from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Artwork_index'),
    path('<int:Artwork_id>', views.detail, name='Artwork')
]