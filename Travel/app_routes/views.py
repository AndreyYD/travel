from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import RouteForm, RouteModelForm
from .models import RouteModel
from .utils import get_routes
from app_trains.models import TrainModel
from app_cities.models import CityModel


def route_view(request):
    form = RouteForm()
    context = {
        'form': form
    }
    return render(request, 'routes/list_routes.html', context)

def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/list_routes.html', {'form': form})
            return render(request, 'routes/list_routes.html', context)
        return render(request, 'routes/list_routes.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        context = {
            'form': form
        }
        return render(request, 'routes/list_routes.html', context)

def add_route(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            departure_city_id = int(data['departure_city'])
            arrival_city_id = int(data['arrival_city'])
            trains = data['trains'].split(',')
            trains_list = [int(t) for t in trains if t.isdigit()]
            qs = TrainModel.objects.filter(id__in=trains_list).select_related('departure_city', 'arrival_city')
            cities = CityModel.objects.filter(id__in=[departure_city_id, arrival_city_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'departure_city': cities[departure_city_id],
                    'arrival_city': cities[arrival_city_id],
                    'travel_time': total_time,
                    'trains': qs,
                }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'Невозможно сохранить маршрут')
        return redirect('/')

def save_route(request):
    if request.method == "POST":
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Маршрут успешно сохранен')
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'Невозможно сохранить маршрут')
        return redirect('/')

class RouteListView(ListView):
    paginate_by = 10
    model = RouteModel
    template_name = 'routes/list.html'

class RouteDetailView(DetailView):
    queryset = RouteModel.objects.all()
    template_name = 'routes/route.html'
