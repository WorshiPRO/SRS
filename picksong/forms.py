from django import forms

class SongForm(forms.Form):
    song = forms.CharField(max_length=30)
	owner = forms.CharField(max_length=30)
	key_of_song = forms.CharField(max_length=10)
	highest_note = forms.CharField(max_length=10)
	lowest_note = forms.CharField(max_length=10)
