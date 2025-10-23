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

    path.reverse()
    return path

if __name__ == "__main__":
    graph = {
    1: [(2, 1), (11, 1)],
    2: [(1, 1), (3, 1), (21, 1)],
    3: [(2, 1), (4, 1), (8, 2)],
    4: [(3, 1), (5, 1)],
    5: [(4, 1), (6, 2), (7, 1), (22, 1)],
    6: [(5, 2), (7, 1)],
    7: [(5, 1), (6, 1), (8, 1)],
    8: [(3, 2), (7, 1), (9, 1)],
    9: [(8, 1), (10, 1), (19, 1)],
    10: [(9, 1), (11, 1), (18, 2)],
    11: [(1, 1), (12, 2), (10, 1), (17, 1)],
    12: [(11, 2), (13, 2)],
    13: [(12, 2), (14, 2), (21, 1)],
    14: [(13, 2), (15, 1), (16, 1), (20, 1)],
    15: [(14, 1)],
    16: [(14, 1), (17, 2)],
    17: [(11, 1), (16, 2), (18, 2)],
    18: [(10, 2), (17, 2), (19, 2)],
    19: [(9, 1), (18, 2)],
    20: [(14, 1), (21, 2), (22, 1)],
    21: [(2, 1), (13, 1), (20, 2), (22, 2)],
    22: [(5, 1), (20, 1), (21, 2)]
}


    source = 1
    targets = [6,8,9,15,16,22]
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