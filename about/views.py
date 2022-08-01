from django.shortcuts import render

def about(request):
    return render(request, 'tasks/about.html')
