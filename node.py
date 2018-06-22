from flask_restful import Resource

class Node(Resource):
    def get(self, node_id=None):
        if node_id:
            return {"nodes": node_id}
        else:
            return {"nodes": ["node1", "node2"]}
