import heapq

def dijkstra(graph, source):
    dist  = {u: float('inf') for u in graph}
    parent = {u: None for u in graph}
    dist[source] = 0
    #implement here
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