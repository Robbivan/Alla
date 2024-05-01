import yaml


class ProgramIni:
    def __init__(self, config_name="config/master-config.yml"):
        self.company_name = None
        self.project_name = None
        self.info_output = None
        self.is_check_cycle = None

        self.__upload_settings_from_master_config(config_name)

    def __upload_settings_from_master_config(self, config_name):
        with open(config_name, "r") as file:
            data = yaml.safe_load(file)
        self.company_name = data['company_name']
        self.project_name = data['project_name']
        self.info_output = data['info_output']
        self.is_check_cycle = data['is_check_cycle']
        self.round_number = 4  # default round number
        if data['round_result']['status'] is True:
            self.round_number = data['round_result']['number_of_decimal_places']

    def get_is_check_cycle(self):
        return self.is_check_cycle

    def get_round_number(self):
        return self.round_number