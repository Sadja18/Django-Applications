from django.contrib import messages
from django.contrib.auth.mixins import(LoginRequiredMixin,PermissionRequiredMixin)

from django.urls import reverse

from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render

from django.views import generic
from communities.models import Community, CommunityMember
from . import models

class CreateCommunityView(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Community

class SingleCommunity(generic.DetailView):
    model = Community

class ListCommunity(generic.ListView):
    model = Community
