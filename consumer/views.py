# -*- coding: utf-8 -*-
from django.shortcuts import  render, HttpResponse
import os
from models import Reaction
import random
import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def myrand(length):
    return datetime.datetime.now().microsecond / 1000 % length

class Gustav(object):
    pass

class Richard(Gustav):
    pass

class Igor(Richard):
    pass

class AlexeySabiashchanski(Igor):
    def __init__(self):
        self.categories = {}

        self.initWords = {}
        self.loadDictionary()
        self.loadDictionaryFromBase()

    def loadDictionary(self):
        fileList = os.listdir('consumer/cats')

        for cat in fileList:
            values = []
            with open('consumer/cats/%s' % cat) as f:
                lines = f.readlines()
                values = [u'%s' % line.strip() for line in lines]
            if cat.endswith('_ini'):
                self.initWords[cat[:-4]] = {value.lower() for value in values}
            else:
                self.categories[cat] = values

    def loadDictionaryFromBase(self):
        reactions = Reaction.objects.all()
        for reaction in reactions:
            cat = reaction.ini.lower()
            if cat not in self.initWords.keys():
                self.initWords[cat] = set([cat,])
                self.categories[cat] = [reaction.ans,]
            else:
                self.initWords[cat].add(cat)
                self.categories[cat].append(reaction.ans)

    def getWordsOfWisdom(self, text):
        words = {u'%s' % word.strip().lower().replace('?', '') for word in text.split(' ')}
        catsMatched = 0
        catsForAnswer = []
        for cat in self.initWords.keys():
            if self.initWords[cat] & words:
                catsForAnswer.append(cat)
                catsMatched += 1
            if catsMatched == 2:
                break
        if not catsForAnswer: catsForAnswer.append('whatever')

        responses = []
        for cat in catsForAnswer:
            answerList = self.categories[cat]
            ansIndex = myrand(len(answerList))
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


