from collections import defaultdict

class CriticalLinks:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.timer = 0

        self.disc = [-1] * n
        self.low = [-1] * n
        self.parent = [-1] * n

        self.bridges = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def _dfs(self, u):
        self.disc[u] = self.low[u] = self.timer
        self.timer += 1

        for v in self.graph[u]:
            # Tree edge
            if self.disc[v] == -1:
                self.parent[v] = u
                self._dfs(v)

                self.low[u] = min(self.low[u], self.low[v])

                # BRIDGE CONDITION
                if self.low[v] > self.disc[u]:
                    self.bridges.append((u, v))

            # Back edge (ignore parent)
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])

    def find_bridges(self):
        for i in range(self.n):
            if self.disc[i] == -1:
                self._dfs(i)

        return self.bridges


# ---------------- Example ----------------

if __name__ == "__main__":
    # Number of nodes
    n = 5

    cl = CriticalLinks(n)

    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (1, 3),
        (3, 4)
    ]

    for u, v in edges:
        cl.add_edge(u, v)

    print("Critical Links (Bridges):")
    print(cl.find_bridges())