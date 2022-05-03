from django.contrib import messages
from django.shortcuts import render

from .forms import RouteForm
from .utils import get_routes


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
