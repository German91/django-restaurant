from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AddRestaurantForm
from .models import Restaurant
from sections.models import Section
from sections.forms import SectionForm

@login_required
def restaurant_list(request):
    restaurants = Restaurant.objects.filter(archived=False)
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})

@login_required
def restaurant_add(request):
    form = AddRestaurantForm()
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(request, messages.SUCCESS, 'Restaurant successfully added')
            return redirect('restaurant_list')
    return render(request, 'restaurants/restaurant_add.html', {'form': form})

@login_required
def restaurant_view(request, slug):
    section_form = SectionForm()
    restaurant = get_object_or_404(Restaurant, slug=slug)
    sections = Section.objects.filter(restaurant=restaurant)
    form = AddRestaurantForm(instance=restaurant)
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(request, messages.SUCCESS, 'Restaurant successfully updated')
    return render(request, 'restaurants/restaurant_view.html', {'restaurant': restaurant, 'form': form, 'section_form': section_form, 'sections': sections})

@login_required
def restaurant_archive(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.archived = True
    restaurant.save()
    return redirect('restaurant_list')