
from django.http import HttpResponse
# Create your views here.
# all html code is inside def

def index(response) :
    return HttpResponse('<h1>this is the home page for the music section</h1>')

def details(response, album_id) :
    return HttpResponse('<h2>Deatil of your Album num ID : '+ str(album_id)+'</h1>')
