from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Section
from .forms import SectionForm
from restaurants.models import Restaurant
from categories.models import Category
from categories.forms import CategoryForm
from items.forms import AddItemForm

@login_required
def section_add(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            restaurant = get_object_or_404(Restaurant, pk=request.POST.get('restaurant'))
            section = form.save(commit=False)
            section.restaurant = restaurant
            section.save()
    return redirect('restaurant_view', slug=restaurant.slug)

@login_required
def section_delete(request, pk):
    section = get_object_or_404(Section, pk=pk)
    section.delete()
    return redirect('restaurant_view', slug=section.restaurant.slug)

@login_required
def section_view(request, slug):
    item_form = AddItemForm()
    category_form = CategoryForm()
    section = get_object_or_404(Section, slug=slug)
    categories = Category.objects.filter(section=section)

    if request.method == 'POST':
        item_form = AddItemForm(request.POST)
        if item_form.is_valid():
            item_form.save(commit=True)
            return redirect('section_view', slug=section.slug)
    return render(request, 'sections/section_view.html', {'section': section, 'categories': categories, 'category_form': category_form, 'item_form': item_form})