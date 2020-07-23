from django.shortcuts import render
from django.views.generic  import (View, TemplateView, ListView,
                                   DetailView, CreateView, DeleteView, UpdateView)
from django.urls import reverse_lazy
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_inject'] = 'Injection'
        return context

class SchoolListView(ListView):
    """
    by default, context object name returned by ListView is lowercase(School_list)
    """
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    """
    by default, context object name returned by DetailView is lowercase(School)
    """
    context_object_name = 'school_details'
    model = models.School
    template_name = 'lv_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("lv_app:list")
