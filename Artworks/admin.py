from django.contrib import admin
from .models import Artwork, Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ArtworkAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'daily_views')

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Artist, ArtistAdmin)
