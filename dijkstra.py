import heapq

def dijkstra(graph, source):
    dist  = {u: float('inf') for u in graph}
    parent = {u: None for u in graph}
    dist[source] = 0
    #implement here

    #min prio q
    Q = [(0, source)]
    visited = set ()

    while Q:
        du, u = heapq.heappop(Q)

        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u]:
            #relaxation
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(Q, (dist[v], v))

    return dist, parent

def show_path(parent, target):
    path = []
    #implement path reconstruction
    return path

if __name__ == "__main__":
    graph = {
        #add edges
    }

    source = 'A'
    dist, parent = dijkstra(graph, source)
    target = 'D'
    #print distances and path