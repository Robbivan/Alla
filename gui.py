import os
import webbrowser

from pyvis.network import Network


class Gui:
    def make_info_str_node(self, sort_list_graph):
        list_of_tags = [item.tag for item in sort_list_graph]
        list_of_fullnames = [item.fullname for item in sort_list_graph]
        list_of_limits = [str(item.limit) for item in sort_list_graph]
        list_of_dynamic_workload = [str(item.dynamic_workload) for item in sort_list_graph]
        list_of_model_workload = [str(item.model_workload) for item in sort_list_graph]
        list_of_rest = [str(item.rest) for item in sort_list_graph]

        modified_list = ["tag: " + tag + "\n" +
                         "fullname: " + fullname + "\n" +
                         "limit: " + limit + "\n" +
                         "model_workload: " + model_workload + "\n" +
                         "dynamic_workload: " + dynamic_workload + "\n" +
                         "rest: " + rest + "\n"
                         for tag, fullname, limit, dynamic_workload, model_workload, rest in
                         zip(list_of_tags,
                             list_of_fullnames,
                             list_of_limits,
                             list_of_dynamic_workload,
                             list_of_model_workload,
                             list_of_rest)]

        print(modified_list)
        return modified_list


    def do_gui(self, program, graph, sort_list_graph):
        net = Network(notebook=True)  # отображение в Блокноте

        color_nodes = ['#88F02E'] * len(sort_list_graph)

        title_test = ["some_text\n anpther"] * len(sort_list_graph)

        new_title = self.make_info_str_node(sort_list_graph)

        net.add_nodes([item.id for item in sort_list_graph],
                      label=[item.tag for item in sort_list_graph],
                      title=new_title,
                      color=color_nodes)

        keys = graph.keys()

        for micro in keys:
            for link in graph[micro]:
                print(link)
                net.add_edge(micro.id, link[0].id, arrows='to', color='#4596FF', label=str(link[1]), font={'size': 10})
        print(graph)

        # net.add_nodes([1, 2, 3],
        #               value=[10, 100, 400],
        #               title=['I am node 1', 'node 2 here', 'and im node 3'],
        #               x=[21.4, 54.2, 11.2],
        #               y=[100.2, 23.54, 32.1],
        #               label=['NODE 1', 'NODE 2', 'NODE 3'],
        #               color=['#00ff1e', '#162347', '#dd4b39'])
        # net.show_buttons()

        net.show("html/result_temp.html")

        self.html_info_edit()

        filename = 'file:///' + os.getcwd() + '/html/' + 'result.html'
        webbrowser.open_new_tab(filename)

    def html_info_edit(self):
        title = "Alla: ваша микросервисная сеть"
        file_temp_path = "html/result_temp.html"
        with open(file_temp_path, 'r') as f:
            html_content = f.read()

        start_index = html_content.find("<center>")
        end_index = html_content.find("</center>")
        first_html_content = (html_content[:start_index] + "<center>\n<h1>" + title +
                              "</h1>\n</center>" + html_content[end_index:])

        additional_text = "<p style='margin-left: 20px;'>Для микросервисов цвета: <br>" \
                          "<span style='margin-left: 20px;'>Зеленый - все в порядке с нагрузкой</span> <br>" \
                          "<span style='margin-left: 20px;'>Красный - проблема несоответствия в моделируемой нагрузке и лимита</span> <br>" \
                          "<span style='margin-left: 20px;'>Фиолетовый - проблема несоответствия реальной нагрузки и лимита</span></p>"

        insert_index = first_html_content.find("</body>")
        second_html_content = first_html_content[:insert_index] + additional_text + first_html_content[insert_index:]

        with open('html/result.html', 'w') as f:
            f.write(second_html_content)
        os.remove(file_temp_path)

        # print(file_path)