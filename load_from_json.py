from microservice import Microservice
import json


# Create microservice from json
def create_microservices_from_json(json_data):
    microservices = {}
    for service_data in json_data:
        tag = service_data['tag']
        fullname = service_data['fullname']
        limit = service_data['limit']
        microservices[tag] = Microservice(tag, fullname, limit)
    return microservices


# Create graph from json
def create_graph_from_json(json_data, microservices):
    graph = {}
    for service_data in json_data:
        tag = service_data['tag']
        neighbors = service_data['neighbors']
        graph[microservices[tag]] = [(microservices[neighbor['tag']], neighbor['weight']) for neighbor in neighbors]

    # print(graph)
    return graph


def loading_json_info(filename):
    # Read data from json
    with open(filename) as json_file:
        data = json.load(json_file)

    microservices = create_microservices_from_json(data['services'])
    if not microservices:
        print("No data")

    print("Loading successful complete")
    return create_graph_from_json(data['services'], microservices), microservices
