from django.shortcuts import render

def base(request):
    return render(request,'base.html')

def header(request):
    return render(request,'header.html')

def sidebar(request):
    return render(request,'sidebar.html')

def dashboard(request):
    return render(request,'dash.html')

def event(request):
    return render(request,'event.html')

def project(request):
    return render(request,'project.html')

def task(request):
    return render(request,'task.html')

def note(request):
    return render(request,'note.html')

def team(request):
    return render(request,'team.html')

def report(request):
    return render(request,'report.html')

def help_support(request):
    return render(request,'help_support.html')

def todo(request):
    return render(request,'todo.html')

def colab(request):
    return render(request,"collapsible_side.html")

def icons(request):
    return render(request,"icons.html")

def trial(request):
    return render(request,"trial.html")

def temp(request):
    return render(request,"temp.html")

def add(request):
    return render(request,"add.html")