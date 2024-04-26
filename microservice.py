
class Microservice:
    id_counter = 0

    def __init__(self, tag, fullname, limit, rest, workload=0):
        Microservice.id_counter += 1
        self.id = Microservice.id_counter  # Присваиваем ID текущему экземпляру
        self.tag = tag
        self.fullname = fullname
        self.workload = workload
        self.limit = limit
        self.rest = rest

    def set_workload(self, workload):
        self.workload = workload
        return self

    def get_workload(self):
        return self.workload

    def get_rest(self):
        return self.rest

    def get_name(self):
        return self.tag

