from django.shortcuts import render
from .forms import MailForm
from django.core.mail import send_mail

def handle_send(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'], 'anonymous.email369531@gmail.com', [cd['to']])
    else:
        form = MailForm()
    return render(request, 'index.html',  {'form': form})
