from django.db import models

# Create your models here.

class Song(models.Model):
	song = models.TextField(default="None")
	owner = models.TextField(default="None")
	key_of_song = models.TextField(blank=True)
	highest_note = models.TextField(blank=True)
	lowest_note = models.TextField(blank=True)
	submission_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "songtest"
