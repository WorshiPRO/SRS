from django.shortcuts import render
from django.shortcuts import redirect
from .models import Song
from .forms import SongForm

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data': "Hello Django ",})

def inputsong(request):
	if request.method == 'POST':
		print("hi!", request.POST)
        form = SongForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
	else:
		form = SongForm()

	# newsong = Song()
	# newsong.name = request.POST.get("songname", "sad")
	# newsong.owner = request.POST.get("band", "too_sad")
	# newsong.key_of_song = request.POST.get("key", "n")
	# newsong.highest_note = request.POST.get("highest", "n")
	# newsong.lowest_note = request.POST.get("lowest", "n")

	arg = {'result': Song.objects.all(), 'form': form}
	return render(request, 'picksong.html', arg)

def result(request):
	return render(request, 'result.html', {'result': Song.objects.all()})
