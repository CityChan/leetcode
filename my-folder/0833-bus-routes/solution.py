class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        # route_bool = [False]*len(routes)
        bfs = [S]
        # seen = set([S])
        seen_routes = set([])
        step = 0
        while bfs:
            # print(bfs)
            sz = len(bfs)
            for i in range(sz):
                now = bfs.pop(0)
               
                if now==T:
                  
                    return step
                else:
     
                    for j in to_routes[now]:
                        if j not in seen_routes:
                            for nxt in routes[j]:
                                # if nxt not in seen:
                                    bfs.append(nxt)
                                    # seen.add(nxt)
                        seen_routes.add(j)
            step+=1

        return -1
