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

        print(f"Visiting node {u} with current distance {du}")

        for v, w in graph[u]:
            #relaxation
            if dist[v] > dist[u] + w:
                old_dist = dist[u]
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(Q, (dist[v], v))
                print(f"    Updated distance[{v}] from {old_dist} to {dist[v]}, parent[{v}] = {u}")

    return dist, parent

def show_path(parent, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reserve()
    return path

if __name__ == "__main__":
    graph = {
        1: [(2,1), (3,4)],
        2: [(1,1), (3,2), (4,5)],
        3: [(1,4), (2,2), (4,1)],
        4: [(2,5), (3,1)]
    }

    source = 1
    targets = [2,3,4]
    dist, parent = dijkstra(graph, source)

    #print distances and path

    print("\nFinal distances and parents:")
    print("Vertex\tDistance\tParent")
    for v in sorted(graph):
        print(f"{v}\t{dist[v]}\t{parent[v]}")

    print("\nPaths to targets:")
    for t in targets:
        path = show_path(parent, t)
        print(f"Path to {t}: {path} with distance {dist[t]}")