from django.shortcuts import render
from .models import Template


def template_list(request):
    templates = Template.objects.all()
    context = {'templates': templates}
    return render(request, 'templates/template_list.html', context)


def template_detail(request, pk):
    template = Template.objects.get(pk=pk)
    context = {'template': template}
    return render(request, 'templates/template_detail.html', context)
