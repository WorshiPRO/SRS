from django.shortcuts import render

# Create your views here.
def hello_view(request):
	return render(request, 'hello.html', {'data', "Hello Django ",})
