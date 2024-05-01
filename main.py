import argparse

from program_ini import ProgramIni
from load_from_json import *
from graph_algo import AlgoGraph
from gui import do_gui

from integration.prometheus import IntegrationPrometheus


def static_analysis(graph, algo, entry_point):
    sort_list_graph = algo.top_sort(graph, entry_point)
    print(sort_list_graph)
    for item in sort_list_graph:
        print(item.tag)
        # print(item.limit, "\n")

    algo.find_workload(graph, sort_list_graph)
    for item in sort_list_graph:
        print(item.tag)
        print(item.get_model_workload(), "\n")
        print(item.id)
    return sort_list_graph


def dynamic_analysis(graph):
    prom = IntegrationPrometheus()
    prom.set_live_workload(graph)


def do_hidden_work(program):
    # maybe upload a workload from json file
    # TODO добавить ввод файла и нагрузку
    graph = loading_json_info('data_examples/data_full_example.json')
    # graph = loading_json_info('data_examples/data_with_cycle.json')

    entry_point = next((key for key in graph.keys() if key.tag == '*'), None)
    entry_point.set_model_workload(10_000)  # added for each check if in master-config.yml
    # TODO do set_workload after top_sort

    algo = AlgoGraph("TestAlgo", program.get_round_number())

    bool_result, result = algo.cycle_search(graph, entry_point)
    if bool_result:
        print(result[0].tag, result[1].tag, result[2])
        exit()

    sort_list_graph = static_analysis(graph, algo, entry_point)
    dynamic_analysis(graph)

    # bo,val = algo_graph.cycle_search(graph, entry_point)
    # print(bo)
    # print(val)

    do_gui(program, graph, sort_list_graph)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='keys')
    parser.add_argument('-a', '--arg1', help='desc1')
    args = parser.parse_args()
    if args.arg1:
        print("got", args.arg1)

    try:
        prog = ProgramIni()  # exec
        do_hidden_work(prog)
        # prog.foo([])



        # prom.micro_names
    except ValueError as error:
        print("Error:", error)

