from django.views.generic import ListView, DetailView
from .models import Room


class HomeView(ListView):
    model = Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = 'created'
    context_object_name = 'rooms'
    template_name = 'rooms/home.html'

class RoomDetail(DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'rooms/room_detail.html'
