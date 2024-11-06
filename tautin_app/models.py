from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
# Create your models here.

class Link(models.Model):
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    long_link = models.URLField(max_length=300)
    short_url_link_address = models.SlugField(max_length=255, unique=True)
    short_url_link = models.URLField(max_length=300, blank=True, unique=True)
    date_created = models.DateTimeField(default=timezone.localtime(timezone.now()))
    total_views = models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        current_site = Site.objects.get_current()
        domain = current_site.domain
        self.short_url_link = f"{domain}/{self.short_url_link_address}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_url_link