import requests
import yaml
import json
from urllib.parse import quote


class IntegrationPrometheus:
    def __init__(self, config_name="integration/prom.yaml"):
        self.protocol = None
        self.domain = None
        self.port = None
        self.micro_names = None
        self.measurement_time = None

        self.__upload_settings_from_master_config(config_name)

    def __upload_settings_from_master_config(self, config_name):
        with open(config_name, "r") as file:
            data = yaml.safe_load(file)

        self.protocol = data['protocol']
        self.domain = data['domain']
        self.port = data['port']
        self.micro_names = data['micro_names']
        self.measurement_time = data['measurement_time']


    def send_request_query(self, micro_name):
        composite_url = self.protocol + "://" + self.domain + ":" + str(self.port) + "/api/v1/query?query="
        url_formatted_prom_ql = quote(
            "sum(rate(" + micro_name + "_request_operations_total" + "[" + str(self.measurement_time[0]) \
            + self.measurement_time[1] + "]))")
        url_full = composite_url + url_formatted_prom_ql

        response = requests.get(url_full)

        print(response.json())
        return response.json()

    def set_live_workload(self, graph):
        metrics_json = {}
        print("microservices:\n", self.micro_names)
        try:
            print("\nmetrics:")
            for micro in self.micro_names.keys():
                metrics_json[self.micro_names[micro]] = self.send_request_query(micro)
        except:
            print("Can't find connection")
            return
        self.parse_metric_json(graph, metrics_json)

    def set_emulate_live_workload(self, graph, filename):
        path_to_file = "emulate_dynamic/" + filename
        with open(path_to_file) as json_file:
            metrics_json = json.load(json_file)

        self.parse_metric_json(graph,metrics_json)

    def parse_metric_json(self, graph, metrics_json):
        try:
            print("---------------------------------\n")
            for micro in graph.keys():
                if micro.tag in metrics_json.keys():
                    temp_json = metrics_json[micro.tag]['data']['result']
                    if temp_json:
                        print("tag: ", micro.tag)
                        print("dynamic_emulate_workload: ", temp_json[0]['value'][1], "\n")
                        micro.set_dynamic_workload(temp_json[0]['value'][1])
        except:
            print("Bad tag")
            exit()