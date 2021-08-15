from django.shortcuts import render

# Create your views here.
def index(request):
    print('blogapp')
    return render(request , 'blog/index.html')