from django import forms

class MailForm(forms.Form):
    to = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=300, widget=forms.Textarea)

