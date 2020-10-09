from django.urls import path
from .views import RoomDetail, search

app_name = 'rooms'

urlpatterns = [
    path('<int:pk>/', RoomDetail.as_view(), name='detail'),
    path('search/', search, name='search'),
]