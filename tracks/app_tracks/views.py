from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
import json
import random

from lib import spotifyApi

# Create your views here.
def home(request):
    return redirect('app_tracks:tracks')

def tracks(request, genre=None):
    path = finders.find('json/genres.json')
    with open(path, 'r') as f:
        genres_dict = json.load(f)
    if genre:
        token = spotifyApi.get_token()
        artist_name = random.choice(genres_dict[genre])
        tracks_json = spotifyApi.search(token, (('artist', artist_name),), ('track',), 
                                        50, 0, 'popularity', True)[:10]
        tracks_json_new = []
        for track in tracks_json:
            tracks_json_new.append({
                'artist': artist_name,
                'track': track["name"],
                'album_image_url': track["album"]["images"][2]["url"],
                'preview_url': track["preview_url"]
            })
        return render(request, 'tracks_list.html', {'tracks': tracks_json_new})                          
    else:
        genres_keys = list(genres_dict.keys())
        return render(request, 'tracks_index.html', {'genres_keys': genres_keys})
                
