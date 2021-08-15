from django.shortcuts import render

# Create your views here.
def index(request):
    print('bbs App')
    return render(request , 'bbs/index.html')