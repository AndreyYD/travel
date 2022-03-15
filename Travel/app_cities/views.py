from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

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
    context = {
        'cities': cities,
        'form': form,
    }
    return render(request, 'cities/list_cities.html', context)

class CityDetailView(DetailView):
    queryset = CityModel.objects.all()
    template_name = 'cities/city.html'

class CityCreateView(CreateView):
    model = CityModel
    form_class = CityModelForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('list_cities')

class CityUpdateView(UpdateView):
    model = CityModel
    form_class = CityModelForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('list_cities')

class CityDeleteView(DeleteView):
    model = CityModel
    success_url = reverse_lazy('list_cities')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
