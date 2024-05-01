import requests
import yaml
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
        print(self.measurement_time)

    def send_request_query(self, micro_name):
        composite_url = self.protocol + "://" + self.domain + ":" + str(self.port) + "/api/v1/query?query="
        url_formatted_prom_ql = quote(
            "sum(rate(" + micro_name + "_request_operations_total" + "[" + str(self.measurement_time[0]) \
            + self.measurement_time[1] + "]))")
        url_full = composite_url + url_formatted_prom_ql
        try:
            response = requests.get(url_full)
        except:
            print("exception(request is bad)")
            return

        print(response.json())
        return response.json()

    def set_live_workload(self, graph):
        result_jsons = {}
        print(self.micro_names)
        for micro in self.micro_names.keys():
            result_jsons[self.micro_names[micro]] = self.send_request_query(micro)
        print(result_jsons)

        try:
            for micro in graph.keys():
                if micro.tag in result_jsons.keys():
                    temp_json = result_jsons[micro.tag]['data']['result']
                    if temp_json:
                        print(temp_json[0]['value'][1])
                        micro.set_dynamic_workload(temp_json[0]['value'][1])
        except:
            print("Bad tag")
            exit()