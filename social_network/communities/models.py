# Communities models.py
from django.db import models
from django.utils.text import slugify

import misaka

from django.urls import reverse
from django.contrib.auth import get_user_model
from django import template

User = get_user_model()

register = template.Library()

class Community(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='CommunityMember')

    def __str__(self):
        return self.name

    """
    method to save the community object created
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('communities:single', kwargs={'slug':self.slug})

    class Meta():
        ordering = ['name']

class CommunityMember(models.Model):
    community = models.ForeignKey(Community, related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_communities', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('community', 'user')
