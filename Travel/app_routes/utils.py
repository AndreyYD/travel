from app_trains.models import TrainModel

def dfs_paths(graph, start,goal):
    """
    Функция поиска всех возможных маршрутов из одного города в другой.
    Вариант посещения одного и того же города более одного раза не рассматривается.
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))

def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.departure_city_id, set())
        graph[q.departure_city_id].add(q.arrival_city_id)
    return graph

def get_routes(request, form) -> dict:
    context = {
        'form': form
    }
    qs = TrainModel.objects.all()
    graph = get_graph(qs)
    data = form.cleaned_data
    departure_city = data['departure_city']
    arrival_city = data['arrival_city']
    travel_time = data['travel_time']
    all_ways = dfs_paths(graph, departure_city.id, arrival_city.id)
    if not len(list(all_ways)):
        raise ValueError('Маршрут не найден')
    return context
