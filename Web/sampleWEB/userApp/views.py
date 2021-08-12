from django.shortcuts import render

# Create your views here.
def index(request):
    print('user App')
    return render(request , 'user/index.html')