import os
import webbrowser

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