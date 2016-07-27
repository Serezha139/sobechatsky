# -*- coding: utf-8 -*-
from django.shortcuts import  render, HttpResponse

def getWordsOfWisdom(text):
    leshaAnswers = text + u' и че'
    return leshaAnswers

def index(request):
    text = request.GET.get('text', None)
    if text is None:
        return render(request, 'chat.html', {})
    else:
        wordsOfWisdom = getWordsOfWisdom(text)
        response =  HttpResponse(wordsOfWisdom)
        return response


