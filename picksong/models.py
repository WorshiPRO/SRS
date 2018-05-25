from django.db import models

# Create your models here.

class Song(models.Model):
	name = models.TextField()
	owner = models.TextField()
	key_of_song = models.TextField()
	highest_note = models.TextField()
	lowest_note = models.TextField()
	submission_date = models.DateTimeField(auto_now=True)

	def is_valid():
		valid_keys = ["A", "A#", "Ab",
				"B", "Bb",
				"C", "A#",
				"D", "D#", "Db",
				"E", "Eb",
				"F", "F#",
				"G", "G#", "Gb",]
		if key_of_song is not in valid_keys:
			return False
		else if len(highet_note) is 2:
			if highest_note[0] is not in valid_keys or int(highest_note[1]) is not in range(8):
				return False
		else if len(highet_note) is 3:
			if highest_note[:2] is not in valid_keys or int(highest_note[2]) is not in range(8):
				return False
		else if len(lowest_note) is 2:
			if lowest_note[0] is not in valid_keys or int(lowest_note[1]) is not in range(8):
				return False
		else if len(lowest_note) is 3:
			if lowest_note[:2] is not in valid_keys or int(lowest_note[2]) is not in range(8):
				return False
		else:
			return True


	class Meta:
		db_table = "songtest"
