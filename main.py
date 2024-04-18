from program_ini import ProgramIni
from load_from_json import *
from graph_algo import AlgoGraph


def do_magic_work():
    # maybe upload a workload from json file
    # TODO добавить ввод файла и нагрузку
    graph, microservices = loading_json_info('data_examples/data_full_example.json')
    keys = list(graph.keys())

    entry_point = next((microservice for microservice in
                        list(graph.keys()) if microservice.tag == "*"), None)
    # print(found_microservices)
    # print(keys)

    entry_point.set_workload(10_000)  # added for each check if in master-config.yml
    # TODO do set_workload after top_sort

    algo_graph = AlgoGraph("TestAlgo")
    # algo_graph.dfs_iterative(graph, entry_point)
    test_queue = algo_graph.top_sort(graph, entry_point)
    print(test_queue)
    for item in test_queue:
        print(item.tag)

    # for item in test_queue:
    #     print(item.get_name())


if __name__ == "__main__":
    try:
        prog = ProgramIni()  # exec
        do_magic_work()
    except ValueError as error:
        print("Error:", error)
