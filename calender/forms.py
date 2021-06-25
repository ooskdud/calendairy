from django import forms

class Memo_createForm(forms.Form):
    # group = forms.
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)

    def save(self, *args, **kwargs):
        super(Memo_createForm, self).save(*args,**kwargs)
