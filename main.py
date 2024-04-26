import os
import webbrowser

from program_ini import ProgramIni
from load_from_json import *
from graph_algo import AlgoGraph
from pyvis.network import Network


def do_gui(program, graph, sort_list_graph):
    net = Network(notebook=True)  # отображение в Блокноте

    net.add_nodes([item.id for item in sort_list_graph],
                  label=[item.tag for item in sort_list_graph])

    keys = graph.keys()

    for micro in keys:
        for link in graph[micro]:
            net.add_edge(micro.id, link[0].id)
    print(graph)


    # net.add_nodes([1, 2, 3],
    #               value=[10, 100, 400],
    #               title=['I am node 1', 'node 2 here', 'and im node 3'],
    #               x=[21.4, 54.2, 11.2],
    #               y=[100.2, 23.54, 32.1],
    #               label=['NODE 1', 'NODE 2', 'NODE 3'],
    #               color=['#00ff1e', '#162347', '#dd4b39'])

    net.show("html/result.html")

    current_directory = os.path.dirname(__file__)

    html_directory = os.path.join(current_directory, 'html')
    file_path = os.path.join(html_directory, 'result.html')
    webbrowser.open(file_path, new=2)  # open in new tab


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

