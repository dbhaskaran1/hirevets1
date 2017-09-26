# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Job, Company

def index(request):
    return render(request, 'index.html', context={})

def viewjobs(request):
    return render(request, 'jobs.html', {'jobs': Job.objects.all()})

def addjobs(request):
    return HttpResponse("Hello world, you can add jobs")
