from core.microservice import Microservice
import json


# class CreaterGraph

# Create microservice from json


class CreatorGraph:
    def create_microservices_from_json(self, json_data):
        microservices = {}
        for service_data in json_data:
            tag = service_data['tag']
            fullname = service_data['fullname']
            limit = None
            instance = True
            if 'limit' in service_data:
                limit = service_data['limit']
            rest = 0  # default value for flow
            if 'rest' in service_data:
                rest = service_data['rest']
                if rest < 0 or rest > 1:
                    raise ValueError("Weight must be between 0 and 1 in rest", rest)
            if 'instance' in service_data:
                instance = service_data['instance']

            microservices[tag] = Microservice(tag, fullname, limit, instance, rest)
        return microservices


    # Create graph from json
    def create_graph_from_json(self, json_data, microservices):
        graph = {}
        for service_data in json_data:
            tag = service_data['tag']
            neighbors = service_data['neighbors']
            correct_neighbors = []
            for neighbor in neighbors:
                weight = neighbor['weight']
                if weight < 0 or weight > 1:
                    raise ValueError("Weight must be between 0 and 1", neighbor)
                try:
                    correct_neighbors.append((microservices[neighbor['tag']], weight))
                except KeyError as error:
                    raise ValueError("No exist microservice in *.json with name:", error)
            graph[microservices[tag]] = correct_neighbors
        return graph

    def loading_json(self, filename):
        # Read data from json
        with open(filename) as json_file:
            data = json.load(json_file)

        microservices = self.create_microservices_from_json(data['services'])
        if not microservices:
            print("No data")

        print("Loading struct from file complete successful")
        return self.create_graph_from_json(data['services'], microservices)