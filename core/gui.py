import os
import webbrowser

from pyvis.network import Network


class Gui:
    def do_gui(self, program, graph, sort_list_graph):
        print("----------\n\nGui turn ON\n")
        net = Network(notebook=True)  # отображение в Блокноте

        color_nodes = ['#88F02E'] * len(sort_list_graph)

        for item in sort_list_graph:
            if item.limit is not None:
                if item.model_workload > item.limit:
                    index = sort_list_graph.index(item)
                    color_nodes[index] = "#F53D56"
                if item.dynamic_workload is not None:
                    if float(item.dynamic_workload) > item.limit:
                            index = sort_list_graph.index(item)
                            color_nodes[index] = "#C278EB"

        title = self.make_str_to_title_node(sort_list_graph, color_nodes)

        for index, color in enumerate(color_nodes):
            if color == "#F53D56" or color == "#C278EB":
                if not sort_list_graph[index].instance:
                    title[index] = title[index] + "\nРекомендация: Необходимо увеличить количество ресурсов для данного микросервиса"
                else:
                    title[index] = title[index] + "\nРекомендация: Необходимо инстанцировать данный микроссервис\n" \
                                              " через Load Balancer, например Nginx"

        net.add_nodes([item.id for item in sort_list_graph],
                      label=[item.tag for item in sort_list_graph],
                      title=title,
                      color=color_nodes)

        keys = graph.keys()

        for micro in keys:
            for link in graph[micro]:
                net.add_edge(micro.id, link[0].id, arrows='to', color='#4596FF', label=str(link[1]), font={'size': 10})
        ###
        # net.show_buttons() # for setting gui in pyvis
        ###
        net.show("html/result_temp.html")

        self.html_info_edit()

        filename = 'file:///' + os.getcwd() + '/html/' + 'result.html'
        webbrowser.open_new_tab(filename)

    def make_str_to_title_node(self, sort_list_graph, color_nodes):
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

        return modified_list

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