from collections import deque


class Graph:
    def __init__(self):
        self.graph = {
            "U": ["I", "B", "N"],
            "I": ["U", "B", "A1"],
            "B": ["U", "I", "N", "A1", "A2"],
            "N": ["U", "B", "A2"],
            "A1": ["I", "B", "A2"],
            "A2": ["B", "N", "A1"]
        }


    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("BFS Traversal:")

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        print()

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
            print("DFS Traversal:")

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)



graph = Graph()

graph.bfs("U")
graph.dfs("U")
print()
