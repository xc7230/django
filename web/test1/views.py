from django.shortcuts import render
from django.http import HttpResponse
def asdf(request):
    print("test 입니다.")
    return render(request, 'test.html')
