#!/usr/bin/python3
from django.shortcuts import render, get_object_or_404
from .models import Theme


def theme_list(request):
    themes = Theme.objects.all()
    return render(request, 'themes/theme_list.html', {'themes': themes})

def theme_detail(request, theme_id):
    theme = get_object_or_404(Theme, pk=theme_id)
    return render(request, 'themes/theme_detail.html', {'theme': theme})
