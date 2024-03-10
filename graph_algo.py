class Algo:
    def __init__(self, name):
        self.name = name


class AlgoGraph(Algo):
    def top_sort(self, graph_in_algo, start):
        WHITE = 0
        GRAY = 1
        BLACK = 2

        visited = set()
        stack = [(start, WHITE)]
        topological_queue = []

        while stack:
            vertex, color = stack.pop()
            if vertex not in visited:
                print(vertex.get_name(), "- Color:", color)
                visited.add(vertex)

                neighbors = graph_in_algo.get(vertex, [])

                for neighbor, _ in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append((neighbor, GRAY))
                stack.append((vertex, BLACK))
                topological_queue.append(vertex)
        return topological_queue

    def cycle_search(self):
        pass
