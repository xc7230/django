from django.shortcuts import render
from django.http import HttpResponse
def asdf(request):
    print("test 입니다.")
    return render(request, 'test.html')

def input_page(request):
    return render(request, 'input.html')

def get_data_func(request):
    if request.method == 'GET':
        num1 = request.GET.get('num1', None)
        num2 = request.GET.get('num2', None)
    else :
        num1 = request.POST.get('num1', None)
        num2 = request.POST.get('num1', None)

    sum = int(num1) + int(num2)
    context ={"sum" : sum}

    return render(request, 'result.html', context)

def get_data_func2(request):
    title = request.POST.get('title', None)
    contents = request.POST.get('contents', None)

    context2 = {"title" : title, "contents" : contents}

    print(title)
    print(contents)
    print(context2)

    return render(request, 'result2.html', context2)

def login_input_page(request):

    return render(request, 'login.html')
def logininfo(request):

    userid = request.POST.get('userid', None)
    userpw = request.POST.get('userpw', None)
    print(userid)
    print(userpw)
    context = {"userid" : userid, "userpw" : userpw}
    print(context)

    return render(request, 'result.html', context)