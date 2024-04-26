class Algo:
    def __init__(self, name, round_number):
        self.name = name
        self.round_number = round_number


class AlgoGraph(Algo):
    def top_sort(self, graph_in_algo, start):

        visited = set()
        stack_vertex = [start]
        stack_calls = []
        order = []

        while stack_vertex:
            vertex = stack_vertex.pop()
            if vertex not in visited:  # если vertex уже в visited, то это цикл
                visited.add(vertex)
                stack_vertex.extend([item[0] for item in graph_in_algo[vertex]])

                while stack_calls and vertex not in [item[0] for item in graph_in_algo[stack_calls[-1]]]:
                    order.append(stack_calls.pop())
                stack_calls.append(vertex)
        return stack_calls + order[::-1]  # new return value

    def find_workload(self, graph, sequence):
        for micro in sequence:
            for link in graph[micro]:
                current_workload_to_other = micro.get_workload()*(1-micro.get_rest())
                # print(self.round_number)
                link[0].set_workload(round(link[0].get_workload()+current_workload_to_other*link[1], self.round_number))


    def cycle_search(self):
        pass


