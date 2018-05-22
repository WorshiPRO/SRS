from django.shortcuts import render
from .models import Song

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data': "Hello Django ",})

def picksong(request):
	return render(request, 'picksong.html', {'result': Song.objects.all()})

def inputsong(request):
	if request.method == 'POST':
		newsong = Song()
		newsong.name = request.POST['songname']
		newsong.owner = request.POST['band']
		if request.POST['key'] is not None:
			newsong.key_of_song = request.POST['key']
		if request.POST['highest'] is not None:
			newsong.highest_note = request.POST['highest']
		if request.POST['lowest'] is not None:
			newsong.lowest_note = request.POST['lowest']
		newsong.save()

	return render(request, 'picksong.html', {'result': Song.objects.all()})

def result(request):
	return render(request, 'result.html', {'result': Song.objects.all()})
