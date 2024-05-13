import yaml


class ProgramIni:
    def __init__(self, config_name="config/master-config.yaml"):
        self.company_name = None
        self.project_name = None
        self.info_output = None
        self.round_number = 4  # default round number
        self.integration = None
        self.json_file = None
        self.gateway_load = None

        self.__upload_settings_from_master_config(config_name)

    def __upload_settings_from_master_config(self, config_name):
        with open(config_name, "r") as file:
            data = yaml.safe_load(file)
        self.company_name = data['company_name']
        self.project_name = data['project_name']
        self.info_output = data['info_output']
        self.integration = data['integration']
        self.json_file = data['json_file']
        self.gateway_load = data['gateway_load']
        if data['round_result']['status'] is True:
            self.round_number = data['round_result']['number_of_decimal_places']

    def get_round_number(self):
        return self.round_number