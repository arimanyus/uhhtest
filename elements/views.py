from django.shortcuts import render
from .models import Element


def elements(request):
    elements = Element.objects.all()
    context = {'elements': elements}
    return render(request, 'elements/elements.html', context)
