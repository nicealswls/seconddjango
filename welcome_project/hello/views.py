from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def name(request):
    userName = request.GET['user']
    return render(request, 'name.html', {'userName': userName})  
