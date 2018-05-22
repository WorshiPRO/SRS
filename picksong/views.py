from django.shortcuts import render
from .models import Song

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data': "Hello Django ",})

def picksong(request):
	return render(request, 'picksong.html')

def result(request):
	return render(request, 'result.html', {'data': Song.objects.all()})
