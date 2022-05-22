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
    qs = TrainModel.objects.all().select_related('departure_city', 'arrival_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    departure_city = data['departure_city']
    arrival_city = data['arrival_city']
    cities = data['cities']
    travel_time = data['travel_time']
    all_ways = list(dfs_paths(graph, departure_city.id, arrival_city.id))
    if not len(all_ways):
        raise ValueError('Маршрут не найден')
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Маршрут не найден')
    else:
        right_ways = all_ways
    routes = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.departure_city_id, q.arrival_city_id), [])
        all_trains[(q.departure_city_id, q.arrival_city_id)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_trains[(route[i], route[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= travel_time:
            routes.append(tmp)
    if not routes:
        raise ValueError('Время в пути больше заданного')
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['routes'] = sorted_routes
    context['cities'] = {'departure_city': departure_city, 'arrival_city': arrival_city}
    return context
