from flask import Flask
from flask_restful import Api

from resources.cluster import Cluster
from resources.node import Node
from resources.resource import Resource


app = Flask(__name__)
api = Api(app, prefix="/api/v1")

api.add_resource(Cluster, '/cluster')
api.add_resource(Node, '/nodes', '/nodes/<node_id>')
api.add_resource(Resource, '/resources')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
