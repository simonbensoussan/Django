from __future__ import unicode_literals

from django.db import models

# Create your models here.table = class object, each variable of the class = column of the table
# parameters inside class is always models.Model
# each variable is equals to models. (String, int, float)

class Album(models.Model):
    artist= models.CharField(max_length=250)
    album_tittle= models.CharField(max_length=500)
    genre= models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    #String method for see the details of the object
    def __str__(self):
        return self.artist + ' - '+ self.album_tittle

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

#  after update or change data, field of the DBB
# cmd line : 1) python manage.py makemigrations + name_of_apps (here = music) 2) python manage.py migrate
# see sql : python manage.py sqlmigrate music 0001
