# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:40:59 2019

@author: aniru
"""

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')

def fuckpage(request):
    return HttpResponse('fucked up django')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    worddic={}
    for word in wordlist:
        if word in worddic:
            worddic[word]+=1
        else:
            worddic[word]=1    
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddic':worddic.items()})




