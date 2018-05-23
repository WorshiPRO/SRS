from django.shortcuts import render
from django.shortcuts import redirect
from .models import Song

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data': "Hello Django ",})

def inputsong(request):
	if request.method == 'POST':
		fo = open("viewslog.out", "w")
		fo.write(str(request.POST.keys()))
		newsong = Song()
		newsong.name = request.POST.get("songname", "null")
		newsong.owner = request.POST.get("band", "null")
		newsong.key_of_song = request.POST.get("key", "n")
		newsong.highest_note = request.POST.get("highest", "n")
		newsong.lowest_note = request.POST.get("lowest", "n")
		if(songname is not "null")
			newsong.save()

	#return redirect('/')
	return render(request, 'picksong.html', {'result': Song.objects.all()})

def result(request):
	return render(request, 'result.html', {'result': Song.objects.all()})
