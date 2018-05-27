from django import forms

class SongForm(forms.Form):
    name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'id': 'name',
                                      'class': 'form-control',
                                      'placeholder':'輸入歌曲名, 例如: 喜樂泉源'}))
    owner = forms.CharField(max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'id': 'owner',
                                      'class': 'form-control',
                                      'placeholder':'輸入歌手/樂團/教會, 例如: 讚美之泉'}))
    key = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'id': 'key',
                                      'class': 'form-control',
                                      'placeholder':'輸入歌曲key 例如: G'}))
    highest = forms.CharField(max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'id': 'highest',
                                      'class': 'form-control',
                                      'placeholder':'輸入歌曲最高音 例如: C5(女)'}))
    lowest = forms.CharField(max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'id': 'lowest',
                                      'class': 'form-control',
                                      'placeholder':'輸入歌曲最高音 例如: D4(女)'}))
