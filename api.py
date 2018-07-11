from flask import Flask
from flask_restful import Api, reqparse

from resources.cluster import Cluster
from resources.node import Node
from resources.resource import Resource
from resources.register import Register
from common.util import check_login


app = Flask(__name__)
api = Api(app, prefix="/api/v1", decorators=[check_login])

parser = reqparse.RequestParser()

api.add_resource(Register, '/register', resource_class_args=(parser,))
api.add_resource(Cluster, '/cluster')
api.add_resource(Node, '/nodes', '/nodes/<node_id>')
api.add_resource(Resource, '/resources')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
