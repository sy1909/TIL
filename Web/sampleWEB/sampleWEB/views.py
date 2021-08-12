from django.shortcuts import render
from django.http.response import HttpResponse

# 앞서 views에서 index 를 찾앗으므로 index이름으로 함수를 만들고 httpResponse는 장고 내부 함수
def index(request):

    return HttpResponse('<div align=center>장고를<font color = red> 사용해보자 web application</font><div align=center>')

# render() 함수를 이용해서 template 을 통한 응답이 가능하게 된다.
def loginForm(request):
    
    return render(request , 'login.html')

def test(request):
    pass

def index(request):
    print('web index')
    return render(request , 'index.html')