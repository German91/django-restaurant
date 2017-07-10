from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AddCuisineForm
from .models import Cuisine

@login_required
def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    form = AddCuisineForm()
    if request.method == 'POST':
        form = AddCuisineForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(request, messages.SUCCESS, 'Cuisine successfuly added')
            return redirect('cuisine_list')
    return render(request, 'cuisines/cuisine_list.html', {'form': form, 'cuisines': cuisines})

@login_required
def cuisine_delete(request, pk):
    cuisine = get_object_or_404(Cuisine, pk=pk)
    cuisine.delete()
    return redirect('cuisine_list')