from flask import Flask
from flask_restful import Api, Resource
from cluster import Cluster
from node import Node

app = Flask(__name__)
api = Api(app)

class Root(Resource):
    def get(self):
        return {'hello': 'ClusterAPI'}

api.add_resource(Root, '/')
api.add_resource(Cluster, '/cluster')
api.add_resource(Node, '/node/<node_id>', '/node')

if __name__ == '__main__':
    app.run(debug=True)
