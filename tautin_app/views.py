from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from tautin_app import models

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    
class DashboardView(LoginRequiredMixin, ListView):
    context_object_name = 'links'
    model = models.Link
    template_name = 'dashboard.html'