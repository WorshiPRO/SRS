from django.shortcuts import render
from django.shortcuts import redirect
from .models import Song
from .forms import SongForm

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data': "Hello Django ",})

def inputsong(request):
	newsong = Song()
	success_msg = ''
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
				success_msg = '輸入成功'
			else:
				print("Invalid input!")
				error_msg = '輸入格式錯誤'
		else:
			print("Blank input!")
			error_msg = '請輸入資料'
	form = SongForm()


	arg = {'result': Song.objects.all(), 'form': form, 'error_msg': error_msg, 'success_msg': success_msg}
	return render(request, 'picksong.html', arg)

def searchsong(request):

	return render(request, 'searchsong.html', {'form': SongForm()})

def result(request):
	if request.method == 'POST':
		form = SongForm(request.POST)
	result = []
	for row in Song().objects.all():
		hit = True
		if form.cleaned_data['name'] != "":
			if form.cleaned_data['name'] not in row.name:
				hit = False
		if form.cleaned_data['owner'] != "":
			if form.cleaned_data['owner'] not in row.name:
				hit = False
		if form.cleaned_data['key'] != "":
			if form.cleaned_data['key'] != row.key_of_song:
				hit = False
		if form.cleaned_data['highest'] != "":
			if form.cleaned_data['highest'] != row.highest_note:
				hit = False
		if form.cleaned_data['lowest'] != "":
			if form.cleaned_data['lowest'] != row.lowest_note:
				hit = False

		if hit:
			result.append(row)
		# sort somehow (1. in db 2. here)

	n_info = len(result)
	arg = {'result': result, 'number_of_info': n_info}
	return render(request, 'result.html', arg)
