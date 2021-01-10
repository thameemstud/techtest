import csv, io

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.forms import ValidationError
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Teacher,Subject
from .forms import TeacherForm


class Home(ListView):
  model = Teacher
  template_name = 'directory/home.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["filter_lastname"] = self.request.GET.get('filter_lastname', "")
    context["filter_subject"] = self.request.GET.get('filter_subject', "")
    return context

  def get_queryset(self):
    qs = self.model.objects.all()
    filter_lastname = self.request.GET.get('filter_lastname', "")
    filter_subject = self.request.GET.get('filter_subject', "")
    if filter_lastname:
        qs = qs.filter(lastName__istartswith=filter_lastname.strip()[:2])
    if filter_subject:
        qs = qs.filter(subject__title__istartswith=filter_subject.strip()[:2])
    
    print (qs.query)
    return qs

class TeacherDetailView(DetailView):
  model = Teacher
  template_name = 'directory/detail.html'