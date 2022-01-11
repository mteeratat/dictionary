from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import requests

from dict.submitform.submitform import InputForm

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {}
    context['form'] = InputForm()
    return render(request, 'index.html', context)

def translate(request):
    print(request.POST.get)
    form = InputForm(request.POST)
    word = form['word'].value()
    print(word)
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    r = requests.get(url)
    print(r)
    print("code {}\n".format(r.status_code))
    print("text \n" + r.text)
    print("json \n" + json.dumps(r.json()))
    return HttpResponse(r.json())