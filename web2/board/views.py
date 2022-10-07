from django.shortcuts import render
from board.forms import BoardForm
from django.shortcuts import redirect
from board.models import Board
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/user/login')
def create(request):
    if request.method == "GET":
        boardForm = BoardForm()
        return render(request, 'board/create.html', {'boardForm' : boardForm})
    else:
        boardForm = BoardForm(request.POST)

        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.writer = request.user
            board.save()
            return redirect('/board/list')

def read(request, num):
    post = Board.objects.get(Q(id=num))

    return render(request, 'board/read.html', {'post':post})
@login_required(login_url='/user/login')
def update(request, num):
    post = Board.objects.get(Q(id=num))

    if request.user != post.writer:
        return redirect('/board/list/')

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
@login_required(login_url='/user/login')
def delete(request, num):
    post = Board.objects.get(Q(id=num))
    post.delete()
    return redirect('/board/list/')

def list(request):
    posts = Board.objects.all().order_by('-id')

    return render(request, 'board/list.html', {'posts': posts})