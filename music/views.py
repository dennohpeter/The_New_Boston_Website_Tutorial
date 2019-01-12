from django.shortcuts import render
from django.http import Http404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("That Album Does Not Exist")
    return render(request, 'music/detail.html', {'album': album})
