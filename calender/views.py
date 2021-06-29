
from django.shortcuts import render, redirect
from .models import Diary


# Create your views here.

def index(request):
    diarys = Diary.objects
    return render(request,'index.html', {'diarys':diarys})
    
def memo_create(request):
    if request.method == 'POST':
        form = Memo_createForm(request.POST)
        if form.is_valid():
            Memo = form.save(commit=False)
        return redirect('/Memo_detail/'+str(Memo.id))
    else:
        form = Memo_createForm()
    return render(request, 'memo_create.html', {'form':form})

def diary_create(request):
    if request.method == 'POST':
        form = Diary_createForm(request.POST)
        if form.is_valid():
            Diary = form.save(commit=False)
        return redirect('/Diary_detail/'+str(Diary.id))
    else:
        form = Diary_createForm()
    return render(request,'diary_create.html', {'diarys':diarys})

