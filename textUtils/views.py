# This file create by Ritul singh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name': 'Ritul Singh', 'place': 'Mars'}
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djText = (request.POST.get('text', 'default'))
    # check button is on or off
    removepunc = (request.POST.get('removepunc', 'off'))
    cap = (request.POST.get('cap', 'off'))
    removeSpace = (request.POST.get('removeSpace', 'off'))
    extralineremove = (request.POST.get('extralineremove', 'off'))
    numberremover = (request.POST.get('numberremover', 'off'))

    # Removed Punctuations
    if removepunc == 'on':
        punctuation ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    # Capital Letter
    elif cap == "on":
        analyzed = ""
        for char in djText:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capital Letter', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    # Remove Extra Space
    elif removeSpace == "on":
        analyzed = ""
        for index, char in enumerate(djText):
            if not (djText[index] == " " and djText[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    # Extra Line Remove
    elif extralineremove == "on":
        analyzed = ""
        for char in djText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Extra Line Remove', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    # Number remover in the text
    elif numberremover == "on":
        number = '''123456789'''
        analyzed = ""
        for char in djText:
            if char not in number:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    else:
        params = {'purpose': 'You Not Choose Any Option', 'analyzed_text': "Error"}
        # analyze the text
        return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
