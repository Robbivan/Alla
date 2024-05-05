import argparse

from program_ini import ProgramIni
from load_from_json import *
from graph_algo import AlgoGraph
from gui import do_gui

from integration.prometheus import IntegrationPrometheus

# class MainProgram
class HandlerGraph:
    def static_analysis(self, graph, algo, entry_point):
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

    def dynamic_analysis(self, graph):
        prom = IntegrationPrometheus()
        if args.emulate_dynamic:
            prom.set_emulate_live_workload(graph, args.emulate_dynamic)
        else:
            prom.set_live_workload(graph)

    def do_hidden_work(self, program):
        graph = loading_json_info(program.json_file)

        entry_point = next((key for key in graph.keys() if key.tag == '*'), None)
        entry_point.set_model_workload(program.gateway_load)

        algo = AlgoGraph("TestAlgo", program.get_round_number())

        bool_result, result = algo.cycle_search(graph, entry_point)
        if bool_result:
            print(result[0].tag, result[1].tag, result[2])
            exit()

        sort_list_graph = self.static_analysis(graph, algo, entry_point)
        self.dynamic_analysis(graph)

        do_gui(program, graph, sort_list_graph)


        # some value for class diagram


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='keys')
    parser.add_argument('-emulate_dynamic', '--emulate_dynamic',
                        help='Parameter for emulate dynamic workload with custom metric '
                             'from directory emulate_dynamic/{your_directory}. ' 
                             'Accept a name of directory where custom metrics save')
    args = parser.parse_args()
    if args.emulate_dynamic:
        print("got", args.emulate_dynamic)

    try:
        prog = ProgramIni()  # exec
        handler = HandlerGraph()
        handler.do_hidden_work(prog)

    except ValueError as error:
        print("Error:", error)