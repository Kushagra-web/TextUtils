from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'kush', 'place': 'India'}
    return render(request, 'index.html', params)
    # return HttpResponse("hello")


def about(request):
    return HttpResponse("About Page")


def analyze(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuatins', 'analyzed_text': analyzed}
        text = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        text = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        text = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

    if removepunc != "on" and newlineremover != "on" and fullcaps != "on" and spaceremover != "on" :
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
