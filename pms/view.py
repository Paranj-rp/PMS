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
    context={
            'id': 1,
            'title': 'Design New Website',
            'client': 'Jane Smith',
            'startDate': '2025-03-01',
            'deadline': '2025-03-15',
            'progress': '60%',
            'status': 'In Progress'
            }
    return render(request,'project.html',context)

def task(request):
    return render(request,'task.html')

def note(request):
    return render(request,'note.html')

def team(request):
    return render(request,'team.html')

def report(request):
    return render(request,'report.html')

def help_sup_help(request):
    return render(request,"help_support_help.html")

def help_sup_article(request):
    return render(request,'help_support_article.html')

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

def timesheet(request):
    return render(request,'timesheets.html')

def team_members(request):
    return render(request,'team_members.html')

def announcement(request):
    return render(request,'announcement.html')

def time_card(request):
    return render(request,'time_card.html')

def leave(request):
    return render(request,'leave.html')

def timeline(request):
    return render(request,'timeline.html')