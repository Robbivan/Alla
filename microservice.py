
class Microservice:
    def __init__(self, tag, fullname, limit, workload=0):
        self.tag = tag
        self.fullname = fullname
        self.workload = workload
        self.limit = limit

    def set_workload(self, workload):
        self.workload = workload
        return self

    def get_workload(self):
        return self.workload

    def get_name(self):
        return self.tag