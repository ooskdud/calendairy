from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request,'home.html')

def memo_create(request):
    if request.method == 'POST':
        form = Memo_createForm(request.POST)
        if form.is_valid():
            Memo = form.save(commit=False)
        return redirect('/Memo_detail/'+str(Memo.id))
    else:
        form = Memo_createForm()
    return render(request, 'memo_create.html', {'form':form})
            