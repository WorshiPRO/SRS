from django.db import models

# Create your models here.

class Song(models.Model):
	name = models.TextField()
	owner = models.TextField()
	key_of_song = models.TextField()
	highest_note = models.TextField()
	lowest_note = models.TextField()
	submission_date = models.DateTimeField(auto_now=True)

	def is_empty(self):
		return True if self is Song() else False

	def is_valid(self):
		valid_keys = ["A", "A#", "Ab",
				"B", "Bb",
				"C", "A#",
				"D", "D#", "Db",
				"E", "Eb",
				"F", "F#",
				"G", "G#", "Gb",]
		if self.key_of_song not in valid_keys:
			print("[Error] models.py->Song->is_valid: undefined key")
			return False
		elif len(self.highest_note) is 2:
			print("[Status] models.py->Song->is_valid: len(highest_note)=2")
			if self.highest_note[0] not in valid_keys or int(self.highest_note[1]) not in range(8):
				print("[Error] models.py->Song->is_valid: highest_note not found")
				return False
		elif len(self.highest_note) is 3:
			print("[Status] models.py->Song->is_valid: len(highest_note)=3")
			if self.highest_note[:2] not in valid_keys or int(self.highest_note[2]) not in range(8):
				print("[Error] models.py->Song->is_valid: highest_note not found")
				return False

		if len(self.lowest_note) is 2:
			print("[Status] models.py->Song->is_valid: len(lowest_note)=2")
			if self.lowest_note[0] not in valid_keys or int(self.lowest_note[1]) not in range(8):
				print("[Error] models.py->Song->is_valid: lowest_note not found")
				return False
		elif len(self.lowest_note) is 3:
			print("[Status] models.py->Song->is_valid: len(lowest_note)=3")
			if self.lowest_note[:2] not in valid_keys or int(self.lowest_note[2]) not in range(8):
				print("[Error] models.py->Song->is_valid: lowest_note not found")
				return False
		else:
			return True


	class Meta:
		db_table = "songtest"
