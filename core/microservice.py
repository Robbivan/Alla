class Microservice:
    id_counter = 0

    def __init__(self, tag, fullname, limit, instance, rest, workload=0):
        Microservice.id_counter += 1
        self.id = Microservice.id_counter  # Присваиваем ID текущему экземпляру
        self.tag = tag
        self.fullname = fullname
        self.model_workload = workload
        self.dynamic_workload = workload
        self.instance = instance
        self.limit = limit
        self.rest = rest

    def set_model_workload(self, workload):
        self.model_workload = workload

    def set_dynamic_workload(self, workload):
        self.dynamic_workload = workload

    def get_model_workload(self):
        return self.model_workload

    def get_dynamic_workload(self, workload):
        return self.dynamic_workload

    def get_rest(self):
        return self.rest

    def get_name(self):
        return self.tag

