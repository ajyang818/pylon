# Create your views here.

from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    def get(self, request):
        context = {
            'body': 'Hello Dan'
        }
        template = "home.html"
        return render(request, template, context)
