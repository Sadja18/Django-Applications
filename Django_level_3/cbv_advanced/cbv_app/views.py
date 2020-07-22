from django.shortcuts import render
from django.views.generic  import View, TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_inject'] = 'First Injection'
        return context
