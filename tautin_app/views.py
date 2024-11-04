from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from tautin_app.models import Link
from tautin_app.forms import LinkForm
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    
class DashboardView(LoginRequiredMixin, View):
    # context_object_name = 'links'
    # model = models.Link
    # template_name = 'dashboard.html'
    def get(self, request):
        form = LinkForm()
        items = Link.objects.all()
        return render(request, 'tautin_app/dashboard.html', {'form' : form, 'items' : items})
    
    def post(self, request):
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.username = request.user
            link.save()
            return redirect('dashboard')
        if not form.is_valid():
            print(form.errors)  # Ini akan menampilkan kesalahan di console

        items = Link.objects.all()
        return render(request, 'tautin_app/dashboard.html', {'form' : form, 'items': items})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = settings.REGISTER_REDIRECT_URL  

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save() 
        login(self.request, user) 
        return response
    
def redirect_to_long_link(request, short_url_link_address):
    link = get_object_or_404(Link, short_url_link_address=short_url_link_address)
    link.total_views += 1
    link.save()
    return redirect(link.long_link)