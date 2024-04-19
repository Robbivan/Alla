from program_ini import ProgramIni
from load_from_json import *
from graph_algo import AlgoGraph


def do_hidden_work():
    # maybe upload a workload from json file
    # TODO добавить ввод файла и нагрузку
    graph = loading_json_info('data_examples/data_full_example.json')

    entry_point = next((key for key in graph.keys() if key.tag == '*'), None)
    entry_point.set_workload(10_000)  # added for each check if in master-config.yml
    # TODO do set_workload after top_sort

    algo_graph = AlgoGraph("TestAlgo")

    test_queue = algo_graph.top_sort(graph, entry_point)
    print(test_queue)
    for item in test_queue:
        print(item.tag)
        # print(item.limit, "\n")

    algo_graph.find_workload(graph, entry_point, test_queue)
    for item in test_queue:
        print(item.tag)
        print(item.get_workload(), "\n")

    # for item in test_queue:
    #     print(item.get_name())


if __name__ == "__main__":
    try:
        prog = ProgramIni()  # exec
        do_hidden_work()
    except ValueError as error:
        print("Error:", error)
