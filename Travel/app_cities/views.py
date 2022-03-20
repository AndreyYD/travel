from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .models import CityModel
from .forms import CityForm, CityModelForm


def list_cities_view(request):
    if request.method == 'POST':
        form = CityModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityModelForm()
    cities = CityModel.objects.all()
    paginator = Paginator(cities, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'cities': cities,
        'form': form,
        'page_obj': page_obj,
    }
    return render(request, 'cities/list_cities.html', context)

class CityDetailView(DetailView):
    queryset = CityModel.objects.all()
    template_name = 'cities/city.html'

class CityCreateView(SuccessMessageMixin, CreateView):
    model = CityModel
    form_class = CityModelForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('list_cities')
    success_message = "Город успешно создан"

class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = CityModel
    form_class = CityModelForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('list_cities')
    success_message = "Город успешно отредактирован"

class CityDeleteView(DeleteView):
    model = CityModel
    success_url = reverse_lazy('list_cities')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город успешно удален')
        return self.post(request, *args, **kwargs)

class CityListView(ListView):
    paginate_by = 10
    model = CityModel
    template_name = 'cities/list_cities.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityModelForm()
        context['form'] = form
        return context
