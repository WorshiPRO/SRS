from django.db import models
import datetime
# Create your models here.

class Song(models.Model):
	name = models.TextField(default='none')
	owner = models.TextField(default='none')
	key_of_song = models.TextField(default='none')
	highest_note = models.TextField(default='none')
	lowest_note = models.TextField(default='none')
	submission_date = models.DateTimeField(auto_now=True)

	def is_empty(self):
		return True if self is Song() else False

	def is_valid(self):
		valid_keys = ["A", "A#", "Ab",
				"B", "Bb",
				"C", "C#",
				"D", "D#", "Db",
				"E", "Eb",
				"F", "F#",
				"G", "G#", "Gb",]
		if self.key_of_song not in valid_keys:
			print("[Error] models.py: undefined key")
			return False
		elif len(self.highest_note) is 2:
			print("[Status] models.py: len(highest_note)=2")
			if self.highest_note[0] not in valid_keys:
				print("[Error] models.py: highest_note not found")
				return False
		elif len(self.highest_note) is 3:
			print("[Status] models.py: len(highest_note)=3")
			if self.highest_note[:2] not in valid_keys:
				print("[Error] models.py: highest_note not found")
				return False

		if len(self.lowest_note) is 2:
			print("[Status] models.py: len(lowest_note)=2")
			if self.lowest_note[0] not in valid_keys:
				print("[Error] models.py: lowest_note not found")
				return False
		elif len(self.lowest_note) is 3:
			print("[Status] models.py: len(lowest_note)=3")
			if self.lowest_note[:2] not in valid_keys:
				print("[Error] models.py: lowest_note not found")
				return False

		print("[Status] models.py: validation okay")
		return True


	class Meta:
		db_table = "songtest"
