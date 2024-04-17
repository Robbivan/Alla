class Algo:
    def __init__(self, name):
        self.name = name


class AlgoGraph(Algo):
    def top_sort(self, graph_in_algo, start):

        visited = set()
        stack = [start]
        stack_calls = []
        order = []
        topological_queue = []

        print(graph_in_algo)
        while stack:
            vertex = stack.pop()
            if vertex not in visited: # если vertex уже в visited, то это цикл
                print(vertex.get_name())
                visited.add(vertex)

                neighbors = graph_in_algo.get(vertex, [])

                for neighbor, _ in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
                # stack.append((vertex, BLACK))
                topological_queue.append(vertex)
        return topological_queue

    def cycle_search(self):
        pass
