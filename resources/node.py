
from flask_restful import Resource
from flask import make_response
import json
from common.util import get_cib_data, json_find


class Node(Resource):
    @get_cib_data("nodes")
    def get(self, node_id=None):
        if node_id:
            for item in json_find(cib_data, "nodes/node"):
                if node_id in [item["@uname"], item["@id"]]:
                    return make_response(json.dumps(item))
        else:
            return make_response(cib_data)
