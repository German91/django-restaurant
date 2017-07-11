from django.contrib import admin

from .models import Allergen, Item

class ItemAdmin(admin.ModelAdmin):
     model = Item,
     filter_horizontal = ('allergens',)

admin.site.register(Allergen)
admin.site.register(Item, ItemAdmin)
