from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, F
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

from . import urls


def get_main_context(context):
    return context



class IndexView(TemplateView):
    # context_object_name = 'index'    
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context = get_main_context(context)
        return context

class AboutView(TemplateView):
    # context_object_name = 'about'    
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context = get_main_context(context)
        context['title']  = "About"
        return context




class DevView(TemplateView):
    # context_object_name = 'dev'    
    template_name = 'dev.html'


    def get_context_data(self, **kwargs):
        context = super(DevView, self).get_context_data(**kwargs)
        context = get_main_context(context)
        context['title']  = "DEV"
        return context
    


