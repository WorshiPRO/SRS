from django.db import models

# Create your models here.

class Song(models.Model):
	name = models.TextField()
	owner = models.TextField()
	key_of_song = models.TextField()
	highest_note = models.TextField()
	lowest_note = models.TextField()
	submission_date = models.DateTimeField(auto_now=True)

	def is_valid(self):
		valid_keys = ["A", "A#", "Ab",
				"B", "Bb",
				"C", "A#",
				"D", "D#", "Db",
				"E", "Eb",
				"F", "F#",
				"G", "G#", "Gb",]
		if self.key_of_song not in valid_keys:
			return False
		elif len(self.highet_note) is 2:
			if self.highest_note[0] not in valid_keys or int(self.highest_note[1]) not in range(8):
				return False
		elif len(highet_note) is 3:
			if self.highest_note[:2] not in valid_keys or int(self.highest_note[2]) not in range(8):
				return False
		elif len(self.lowest_note) is 2:
			if self.lowest_note[0] not in valid_keys or int(self.lowest_note[1]) not in range(8):
				return False
		elif len(self.lowest_note) is 3:
			if self.lowest_note[:2] not in valid_keys or int(self.lowest_note[2]) not in range(8):
				return False
		else:
			return True


	class Meta:
		db_table = "songtest"
