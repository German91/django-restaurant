from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm
from sections.models import Section

@login_required
def category_add(request):
    if request.method == 'POST':
        section = get_object_or_404(Section, pk=request.POST.get('section'))
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.section = section
            category.save()
            return redirect('section_view', slug=section.slug)
    return redirect('restaurant_list')