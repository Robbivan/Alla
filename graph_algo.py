class Algo:
    def __init__(self, name):
        self.name = name


class AlgoGraph(Algo):
    # def top_sort(self, graph_in_algo, start):
    #
    #     visited = set()
    #     stack = [start]
    #     stack_calls = []
    #     order = []
    #     topological_queue = []
    #
    #     while stack:
    #         vertex = stack.pop()
    #         if vertex not in visited:  # если vertex уже в visited, то это цикл
    #             # print(vertex.get_name())
    #
    #             visited.add(vertex)
    #
    #             neighbors = graph_in_algo.get(vertex, [])
    #             stack_calls.append(vertex)
    #             len_stack = len(stack)
    #             # if neighbors.empty()
    #
    #             for neighbor, _ in reversed(neighbors):
    #                 if neighbor not in visited:
    #                     stack.append(neighbor)
    #                 if len_stack == len(stack):
    #                     stack_calls.append(stack.pop())
    #
    #             # stack.append((vertex, BLACK))
    #             topological_queue.append(vertex)
    #     return topological_queue
    def top_sort(self, graph_in_algo, start):

        visited = set()
        stack = [start]
        stack_calls = []
        order = []

        # vertex = stack.pop()
        # first_elements = [item[0] for item in graph_in_algo[vertex]]
        # print(first_elements)

        while stack:
            vertex = stack.pop()
            if vertex not in visited:  # если vertex уже в visited, то это цикл

                visited.add(vertex)

                neighbors = [item[0] for item in graph_in_algo[vertex]]
                # neighbors = graph_in_algo.get(vertex, [])
                stack.extend(neighbors)


                while stack_calls and vertex not in [item[0] for item in graph_in_algo[stack_calls[-1]]]:
                    order.append(stack_calls.pop())
                stack_calls.append(vertex)
        return stack_calls + order[::-1]  # new return value

    def cycle_search(self):
        pass
