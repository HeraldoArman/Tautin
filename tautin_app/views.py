from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
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
    

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = settings.REGISTER_REDIRECT_URL  

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save() 
        login(self.request, user) 
        return response