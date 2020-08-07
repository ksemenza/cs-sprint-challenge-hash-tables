#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

cache = {}

def reconstruct_trip(tickets, length):
    # empty route
    route = []

    # add the ticket sue source as ke
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # initial setup, original flight source of NONE
    route.append(cache['NONE'])

    # iterate over tickets array,
    for index in range(length):
        # if the value from route is in the cache
        if route[index] in cache:
            # check for existing value 
            if cache[route[index]] == route[0]:
                continue
            # add the remaining stops to the route array
            route.append(cache[route[index]])

    # when we get to this point, we have a full route
    return route

