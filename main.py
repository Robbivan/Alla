from load_from_json import *


def dfs_iterative(graph_in_algo, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex.get_name())
            visited.add(vertex)

            neighbors = graph_in_algo[vertex]

            for neighbor, weight in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)


if __name__ == "__main__":
    # maybe upload a workload from json file
    graph, microservices = loading_json_info('data.json')
    keys = list(graph.keys())

    entry_point = keys[0].set_workload(10_000)

    print(keys[0])
    dfs_iterative(graph, entry_point)  # first element of json
