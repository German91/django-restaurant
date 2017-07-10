from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AddRestaurantForm
from .models import Restaurant

@login_required
def restaurant_list(request):
  restaurants = Restaurant.objects.all()
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