class Algo:
    def __init__(self, name, round_number):
        self.name = name
        self.round_number = round_number


class AlgoGraph(Algo):
    def top_sort(self, graph, start):

        visited = set()
        stack_vertex = [start]
        stack_calls = []
        order = []

        while stack_vertex:
            vertex = stack_vertex.pop()
            if vertex not in visited:  # если vertex уже в visited, то это цикл
                visited.add(vertex)
                stack_vertex.extend([item[0] for item in graph[vertex]])

                while stack_calls and vertex not in [item[0] for item in graph[stack_calls[-1]]]:
                    order.append(stack_calls.pop())
                stack_calls.append(vertex)
        return stack_calls + order[::-1]  # new return value

    def find_workload(self, graph, sequence):
        for micro in sequence:
            for link in graph[micro]:
                current_workload_to_other = micro.get_model_workload() * (1 - micro.get_rest())
                # print(self.round_number)
                link[0].set_model_workload(
                    round(link[0].get_model_workload() + current_workload_to_other * link[1], self.round_number))

    def cycle_search(self, graph, start):
        stack = [start]
        visited = dict.fromkeys(graph.keys(), "white")

        while stack:
            vertex = self.__peek_stack(stack)
            if visited[vertex] != "grey":
                visited[vertex] = "grey"
                for neighbour_vertex in [item[0] for item in graph[vertex]]:
                    if visited[neighbour_vertex] == "white":
                        stack.append(neighbour_vertex)
                    elif visited[neighbour_vertex] == "grey":
                        result = [vertex, neighbour_vertex, visited]
                        print("Find cycle")
                        return True, result
            elif visited[vertex] == "grey":
                stack.pop()
                visited[vertex] = "black"
        print("No cycle")
        return False, None

    def __peek_stack(self, stack):
        if stack:
            return stack[-1]  # this will get the last element of stack
        else:
            return None
