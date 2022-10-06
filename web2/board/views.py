from django.shortcuts import render

# Create your views here.
def create(request):
    title = request.POST.get('title', None)
    contents = request.POST.get('contents', None)
    print(title)
    print(contents)
    return render(request, 'board/result.html')

def read(request):
    num = request.GET.get('num', None)

    print("read 입니다.")
    return render(request, 'board/read.html')

def update(request):
    if request.method == 'GET':
        num = request.GET.get('num', None)
        print(num)
    else:
        title = request.POST.get('title', None)
        contents = request.POST.get('contents', None)
        print(title)
        print(contents)

    print("update 입니다.")
    return render(request, 'board/result.html')

def delete(request):
    num = request.GET.get('num', None)
    print(num)
    print("delete 입니다.")
    return render(request, 'board/result.html')

def list(request):
    print("list 입니다.")
    return render(request, 'board/list.html')