
from flask_restful import Resource
from common.util import get_cib_data

class Node(Resource):
    @get_cib_data("nodes")
    def get(self, node_id=None):
        if node_id:
            return {"nodes": cib_data}
        else:
            return {"nodes": cib_data}
