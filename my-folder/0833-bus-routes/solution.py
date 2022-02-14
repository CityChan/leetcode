class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        while bfs:
            stop, bus = bfs.pop(0)
            if stop == T: return bus
            for i in to_routes[stop]:
                while routes[i]:
                    j = routes[i].pop()
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                #routes[i] = []  # seen route
        return -1
