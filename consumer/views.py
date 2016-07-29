# -*- coding: utf-8 -*-
from django.shortcuts import  render, HttpResponse
import os
import random

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Genrikh(object):
    pass

class Richard(Genrikh):
    pass

class Igor(Richard):
    pass

class AlexeySabiashchanski(Igor):
    def __init__(self):
        self.categories = {}

        self.initWords = {}
        self.loadDictionary()

    def loadDictionary(self):
        fileList = os.listdir('consumer/cats')

        for cat in fileList:
            values = []
            with open('consumer/cats/%s' % cat) as f:
                lines = f.readlines()
                values = [u'%s' % line.strip() for line in lines]
            if cat.endswith('_ini'):
                self.initWords[cat[:-4]] = set(values)
            else:
                self.categories[cat] = values

    def getWordsOfWisdom(self, text):

        words = {u'%s' % word.strip() for word in text.split(' ')}
        catsMatched = 0
        catsForAnswer = []
        for cat in self.initWords.keys():
            if self.initWords[cat].intersection(words):
                catsForAnswer.append(cat)
                catsMatched += 1
            if catsMatched == 2:
                break
        if not catsForAnswer: catsForAnswer.append('whatever')

        responses = []
        for cat in catsForAnswer:
            answerList = self.categories[cat]
            ansIndex = random.randint(0, len(answerList) - 1)
            responses.append(answerList[ansIndex])

        wordsOfWisdom = '. '.join(responses)
        return wordsOfWisdom

# while True:
#     line = raw_input()
#     print a.getWordsOfWisdom(line)

AlexeyHimself = AlexeySabiashchanski()

def index(request):
    text = request.GET.get('text', None)
    if text is None:
        return render(request, 'chat.html', {})
    else:
        wordsOfWisdom = AlexeyHimself.getWordsOfWisdom(text)
        response =  HttpResponse(wordsOfWisdom)
        return response


