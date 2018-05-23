from django import forms

class SongForm(forms.Form):
    song = forms.CharField(max_length=30)
    owner = forms.CharField(max_length=30)
