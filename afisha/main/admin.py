from django.contrib import admin
from .models import Movie,Director,Review,Actor

# Register your models here.
admin.site.register(Movie,Director,Review,Actor)
