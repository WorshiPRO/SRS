from django.db import models

# Create your models here.

class Song(models.Model):
	name = models.TextField()
	owner = models.TextField()
	key_of_song = models.TextField()
	highest_note = models.TextField()
	lowest_note = models.TextField()
	submission_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "songtest"
