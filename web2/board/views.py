from django.shortcuts import render
from board.forms import BoardForm
from django.shortcuts import redirect
from board.models import Board
from django.db.models import Q

# Create your views here.
def create(request):
    if request.method == "GET":
        boardForm = BoardForm()
        return render(request, 'board/create.html', {'boardForm' : boardForm})
    else:
        boardForm = BoardForm(request.POST)

        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.save()
            return redirect('/board/list')

def read(request, num):
    post = Board.objects.get(Q(id=num))

    return render(request, 'board/read.html', {'post':post})

def update(request, num):
    post = Board.objects.get(Q(id=num))
    if request.method == 'GET':
        boardForm = BoardForm(instance = post)
        return render(request, 'board/update.html', {"boardForm":boardForm})
    else:
        boardForm = BoardForm(request.POST)

        if boardForm.is_valid():
            post.title = boardForm.cleaned_data['title']
            post.contents = boardForm.cleaned_data['contents']
            post.save()
            return redirect("/board/read/"+str(post.id))
def delete(request, num):
    post = Board.objects.get(Q(id=num))
    post.delete()
    return redirect('/board/list/')

def list(request):
    posts = Board.objects.all().order_by('-id')

    return render(request, 'board/list.html', {'posts': posts})