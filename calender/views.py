from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

# def memo_create(request):
#     if request.method == 'POST':
#         form = Memo_createForm(request.POST)
#         if form.is_valid():
            