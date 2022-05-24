from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .models import TrainModel
from .forms import TrainForm


def list_trains_view(request):
    trains = TrainModel.objects.all()
    paginator = Paginator(trains, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'trains/list_trains.html', context)

class TrainListView(ListView):
    paginate_by = 10
    model = TrainModel
    template_name = 'trains/list_trains.html'

class TrainDetailView(DetailView):
    queryset = TrainModel.objects.all()
    template_name = 'trains/train.html'

class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = TrainModel
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:list_trains')
    success_message = "Поезд успешно создан"

class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = TrainModel
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:list_trains')
    success_message = "Поезд успешно отредактирован"

class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = TrainModel
    success_url = reverse_lazy('trains:list_trains')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд успешно удален')
        return self.post(request, *args, **kwargs)
