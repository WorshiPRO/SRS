from django import forms

class SongForm(forms.Form):
    song = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'id': 'songname',
                                        'class': 'form-control',
                                        'placeholder':'輸入歌曲名'}))
    #owner = forms.CharField(max_length=30)
    #key = forms.CharField(max_length=30)
