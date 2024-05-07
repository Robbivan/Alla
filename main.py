import argparse

from program_ini import ProgramIni
from load_from_json import CreatorGraph
from graph_algo import AlgoGraph
from gui import Gui

from integration.prometheus import IntegrationPrometheus


class HandlerGraph:
    def __init__(self, program):
        creator = CreatorGraph()
        self.graph = creator.loading_json(program.json_file)
        self.program = program
        self.gui = Gui()

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

    def do_hidden_work(self):

        entry_point = next((key for key in self.graph.keys() if key.tag == '*'), None)
        entry_point.set_model_workload(self.program.gateway_load)

        algo = AlgoGraph("TestAlgo", self.program.get_round_number())

        bool_result, result = algo.cycle_search(self.graph, entry_point)
        if bool_result:
            print(result[0].tag, result[1].tag, result[2])
            exit()

        sort_list_graph = self.static_analysis(self.graph, algo, entry_point)
        self.dynamic_analysis(self.graph)

        self.gui.do_gui(self.program, self.graph, sort_list_graph)


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
        handler = HandlerGraph(prog)
        handler.do_hidden_work()

    except ValueError as error:
        print("Error:", error)