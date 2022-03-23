from django.urls import path
from .views import TrainListView, TrainDetailView, TrainCreateView, TrainDeleteView, TrainUpdateView

app_name = 'app_trains'

urlpatterns = [
    path('', TrainListView.as_view(), name='list_trains'),
    path('train/<int:pk>/', TrainDetailView.as_view(), name='train'),
    path('add/', TrainCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),
]
