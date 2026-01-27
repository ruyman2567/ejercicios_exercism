"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    [first,second,third,*rest] = each_wagons_id
    *new, = third, *missing_wagons, *rest,first, second
    return new


def add_missing_stops(datos,**kwargs):
    stops = []
    for key, value in kwargs.items():
        stops.append(value)
    everything = {**datos}
    everything["stops"] = stops
    return everything

def extend_route_information(route, more_route_information):
    extend_info = {**route,**more_route_information}
    return extend_info


def fix_wagon_depot(wagons_rows):
    first,second,third = zip(*wagons_rows)
    lista = []
    for values in first,second,third:
        lista.append(list(values))
    return lista
