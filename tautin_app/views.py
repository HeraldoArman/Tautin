from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import FileResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from tautin_app.models import Link
from tautin_app.forms import LinkForm

import qrcode
from io import BytesIO
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    
    
class DashboardView(LoginRequiredMixin, View):
    # context_object_name = 'links'
    # model = models.Link
    # template_name = 'dashboard.html'
    def get(self, request):
        form = LinkForm()
        items = Link.objects.filter(username=self.request.user).order_by('-date_created')
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

        items = Link.objects.filter(username=request.user).order_by('-date_created')
        return render(request, 'tautin_app/dashboard.html', {'form' : form, 'items': items})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = settings.REGISTER_REDIRECT_URL  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        # return super().form_valid(form)
        # user.save()
        return redirect('dashboard')
    
class LinkEditView(LoginRequiredMixin, UpdateView):
    model = Link
    form_class = LinkForm
    template_name = 'tautin_app/edit.html'
    success_url = reverse_lazy('dashboard')
    slug_field = 'short_url_link_address'       # Field di model yang digunakan sebagai slug
    slug_url_kwarg = 'short_url_link_address'
    def get_queryset(self):
        return Link.objects.filter(username=self.request.user)
    
    
    
def redirect_to_long_link(request, short_url_link_address):
    link = get_object_or_404(Link, short_url_link_address=short_url_link_address)
    link.total_views += 1
    link.save()
    return redirect(link.long_link)

@login_required
def download_qr_code(request, short_url_link_address):
    model_link = get_object_or_404(Link, short_url_link_address=short_url_link_address)
    qrcode_image = qrcode.make(model_link.short_url_link, box_size=40)
    
    image_stream = BytesIO()
    qrcode_image.save(image_stream, 'PNG')
    image_stream.seek(0)
    
    response = FileResponse(image_stream, as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{model_link.short_url_link_address}_qr.png"'
    return response