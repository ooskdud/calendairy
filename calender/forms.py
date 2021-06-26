from django import forms
from .models import Memo

class Memo_createForm(forms.Form):
    class Meta:
        model = Memo 
        fields = ['title', 'body']