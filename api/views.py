from django.shortcuts import render

from .models import Item



def get_item(request, id):
    item = Item.objects.get(id=id)
    return item

