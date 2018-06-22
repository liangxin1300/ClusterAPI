from flask import Flask
from flask_restful import Api, Resource

from cluster import Cluster
from node import Node
from corosync import Corosync

import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True
api = Api(app)

class Root(Resource):
    def get(self):
        return {'hello': 'ClusterAPI'}

api.add_resource(Root, '/')
api.add_resource(Cluster, '/cluster')
api.add_resource(Node, '/node/<node_id>', '/node')
api.add_resource(Corosync, '/corosync')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
