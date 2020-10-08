from math import ceil
from django.shortcuts import render
from .models import Room


def all_rooms(request):
    page = request.GET.get('page', 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    rooms = Room.objects.all()[offset:limit]
    page_count = ceil(Room.objects.count() / page_size)
    context = {
        'rooms': rooms, 
        'page_count': page_count, 
        'page': page,
        'page_range': range(0, page_count)
    }
    return render(request, 'rooms/home.html', context)
