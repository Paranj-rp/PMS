"""
URL configuration for pms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.base,name='base'),
    path('header/',view.header,name='header'),
    path('sidebar/',view.sidebar,name='sidebar'),
    path('dash/',view.dashboard,name='dash'),
    path('event/',view.event,name='event'),
    path('project/',view.project,name='project'),
    path('task/',view.task,name='task'),
    path('note/',view.note,name='note'),
    path('team/',view.team,name='team'),
    path('report/',view.report,name='report'),
    path('help_support/',view.help_support,name='help_support'),
    path('collapsible_side/',view.colab,name='colab'),
    path('icons/',view.icons,name='icons'),
    path('trial/',view.trial,name='trial'),
    path('temp/',view.temp,name='temp'),
    path('add/',view.add,name='add')
]
