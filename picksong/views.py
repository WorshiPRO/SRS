from django.shortcuts import render
from django.shortcuts import redirect
from .models import Song

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data': "Hello Django ",})

def inputsong(request):
	if request.method == 'GET':
		#fo = open("viewslog.out", "w")
		#fo.write(str(request.POST.keys()))
		print("hi!")
		print(request.GET)
		newsong = Song()
		newsong.name = request.GET.get("songname", "sad")
		newsong.owner = request.GET.get("band", "too_sad")
		newsong.key_of_song = request.GET.get("key", "n")
		newsong.highest_note = request.GET.get("highest", "n")
		newsong.lowest_note = request.GET.get("lowest", "n")
		if newsong.name is not "sad":
			newsong.save()

	#return redirect('/')
	arg = {'result': Song.objects.all()}
	return render(request, 'picksong.html', arg)

def result(request):
	return render(request, 'result.html', {'result': Song.objects.all()})
