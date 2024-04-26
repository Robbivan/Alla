from program_ini import ProgramIni
from load_from_json import *
from graph_algo import AlgoGraph
from gui import do_gui





def do_hidden_work(program):
    # maybe upload a workload from json file
    # TODO добавить ввод файла и нагрузку
    graph = loading_json_info('data_examples/data_full_example.json')

    entry_point = next((key for key in graph.keys() if key.tag == '*'), None)
    entry_point.set_workload(10_000)  # added for each check if in master-config.yml
    # TODO do set_workload after top_sort

    algo_graph = AlgoGraph("TestAlgo", program.get_round_number())

    sort_list_graph = algo_graph.top_sort(graph, entry_point)
    print(sort_list_graph)
    for item in sort_list_graph:
        print(item.tag)
        # print(item.limit, "\n")

    algo_graph.find_workload(graph, sort_list_graph)
    for item in sort_list_graph:
        print(item.tag)
        print(item.get_workload(), "\n")
        print(item.id)

    do_gui(program, graph, sort_list_graph)


if __name__ == "__main__":
    try:
        prog = ProgramIni()  # exec
        do_hidden_work(prog)
    except ValueError as error:
        print("Error:", error)

