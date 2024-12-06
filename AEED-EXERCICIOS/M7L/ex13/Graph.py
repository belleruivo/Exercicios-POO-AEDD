import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.adj[src].append((dest, weight))
        self.adj[dest].append((src, weight))

    def dijkstra(self, src, dest):
        dist = [float("inf")] * self.V
        dist[src] = 0
        pq = [(0, src)]
        heapq.heapify(pq)
        pred = [-1] * self.V

        while pq:
            current_dist, u = heapq.heappop(pq)
            if current_dist > dist[u]:
                continue

            for neighbor, weight in self.adj[u]:
                if dist[neighbor] > dist[u] + weight:
                    dist[neighbor] = dist[u] + weight
                    pred[neighbor] = u
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        return dist[dest], pred

    def print_shortest_path(self, src, dest, vertex_names):
        dist, pred = self.dijkstra(src, dest)
        if dist == float("inf"):
            print("Given source and destination are not connected")
            return

        # Reconstruct the path
        path = []
        crawl = dest
        while crawl != -1:
            path.append(crawl)
            crawl = pred[crawl]

        path.reverse()
        print(f"Shortest path length is: {dist}")
        print("Path is:", ' -> '.join(vertex_names[p] for p in path))
