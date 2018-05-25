from django.shortcuts import render
from django.shortcuts import redirect
from .models import Song
from .forms import SongForm

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data': "Hello Django ",})

def inputsong(request):
	newsong = Song()
	error_msg = ''
	if request.method == 'POST':
		form = SongForm(request.POST)
		if form.is_valid():
			newsong.name = form.cleaned_data['name']
			newsong.owner = form.cleaned_data['owner']
			newsong.key_of_song = form.cleaned_data['key']
			newsong.highest_note = form.cleaned_data['highest']
			newsong.lowest_note = form.cleaned_data['lowest']
			if newsong.is_valid():
				print("Valid Information!")
				newsong.save()
			else:
				print("Invalid input!")
				error_msg = '輸入格式錯誤'
	form = SongForm()



	arg = {'result': Song.objects.all(), 'form': form, 'error_msg': error_msg}
	return render(request, 'picksong.html', arg)

def result(request):
	return render(request, 'result.html', {'result': Song.objects.all()})
