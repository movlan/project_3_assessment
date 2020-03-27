from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish

class WishCreate(CreateView):
    model = Wish
    fields = ['text']

class WishDelete(DeleteView):
    model = Wish
    success_url = '/'

def index(request):
    item_list = Wish.objects.all()
    return render(request, 'index.html', { 'item_list': item_list,})