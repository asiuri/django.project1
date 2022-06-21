from django.shortcuts import render
from main.models import Movie,Director,Review,Actor
import datetime
# Create your views here.
def news(request):
    dict_={

        'key':'New Kyrgyz films',
        'color':'red',
        'list_':["Akyrky sabak",'Koshunany tandabait']
    }
    return render(request,'news.html',context=dict_)
def movie_list_view(request):
    movies = Movie.object.all()
    context={
        'movie_list':movies
    }
    print(movies)
    return render(request,'movie.html',context=context)
def movie_detail_view(reequest):
    movie=Movie.object.get(id=id)
    return render(reequest,"detail.html",context={'movie':movie})
def add_news(request):
    print("  ..............           ")
    now = datetime.datetime.now()
    print(now)
    year = now.year
    month = now.month
    day = now.day
    if len(str(day)) == 1:
        day = "0"+str(day)
    if len(str(month)) == 1:
        month = "0"+str(month)
    print(year, month, day)
    print(" .........               ")
def national(request):
    return render(request,'national.html')

def children(request):
    return render(request, 'children.html')
