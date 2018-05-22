from django.db import models

# Create your models here.

class Song(models.Model):
	song = models.TextField(default="song")
	owner = models.TextField(default="owner")
	key_of_song = models.TextField(default="Bb")
	submission_date = models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = "songtest"
