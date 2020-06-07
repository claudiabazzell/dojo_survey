# add redirect fn, render ui with no form data (hello world)
# store form data in session
# enhance redirect fn to render ui w form data from session
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def answer(request):
    return render(request, 'redirect.html')


def send(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        if 'part_time' in request.POST and request.POST['part_time'] == 'on':
          request.session['part_time'] = 'Yes'
        else:
          request.session['part_time'] = 'No'
        if 'full_time' in request.POST and request.POST['full_time'] == 'on':
          request.session['full_time'] = 'Yes'
        else:
          request.session['full_time'] = 'No'
        request.session['comment'] = request.POST['comment']
    return redirect('/answer')

