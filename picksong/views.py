from django.shortcuts import render
from django.shortcuts import redirect
from .models import Song
from .forms import SongForm

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data': "Hello Django ",})

def inputsong(request):

	if request.method == 'POST':
		form = SongForm(request.POST)
		if form.is_valid():
			newsong = Song()
			newsong.name = form.cleaned_data['name']
			newsong.owner = form.cleaned_data['owner']
			newsong.key_of_song = form.cleaned_data['key']
			newsong.highest_note = form.cleaned_data['highest']
			newsong.lowest_note = form.cleaned_data['lowest']
			if newsong.name is not "None":
				newsong.save()
	else: # get
		form = SongForm()

	arg = {'result': Song.objects.all(), 'form': form}
	return render(request, 'picksong.html', arg)

def result(request):
	return render(request, 'result.html', {'result': Song.objects.all()})
