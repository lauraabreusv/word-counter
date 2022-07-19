from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import TextForm 
from .count_words import count_words


def index(request):
    count = 0
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            count = count_words(form.cleaned_data['text'])

    else:
        form = TextForm()

    return render(request, 'polls/polls.html', {'form': form, 'count': count})
