from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers

from .models import Item, Allergen
from .forms import AllergenForm
from categories.models import Category

@login_required
def allergen_list(request):
    allergens = Allergen.objects.all()
    form = AllergenForm()
    if request.method == 'POST':
        form = AllergenForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('allergen_list')
    return render(request, 'items/allergen_list.html', {'form': form, 'allergens': allergens})

@login_required
def allergen_delete(request, pk):
    allergen = get_object_or_404(Allergen, pk=pk)
    allergen.delete()
    messages.add_message(request, messages.SUCCESS, 'Allergen successfully removed')
    return redirect('allergen_list')

@login_required
def item_list(request):
    if request.method == 'POST':
        category = Category.objects.filter(pk=request.POST.get('pk'))

        if not category:
            return json.dumps('Category not found')
        items = Item.objects.filter(category=category)
        data = serializers.serialize('json', items)
        return HttpResponse(data, content_type='application/json')