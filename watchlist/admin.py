from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'watched', 'date_added')
    list_filter = ('watched', 'date_added')
    search_fields = ('title', 'description')
    readonly_fields = ('date_added',)
    list_per_page = 20
    ordering = ('-date_added',)
