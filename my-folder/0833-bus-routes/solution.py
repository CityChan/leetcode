class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        seen_routes = set([])
        while bfs:
            stop, bus = bfs.pop(0)
            if stop == T: return bus
            for i in to_routes[stop]:
                if i not in seen_routes:
                    for j in routes[i]:
                        if j not in seen:
                            if j==T:
                                return bus+1
                            bfs.append((j, bus + 1))
                            seen.add(j)
                    seen_routes.add(i)
                #routes[i] = []  # seen route
        return -1
