from flask import Flask
from flask_restful import Api

from resources.demo import HelloWorld
#from resource/cluster import Cluster
#from resource/node import Node
#from resource/corosync import Corosync


app = Flask(__name__)
api = Api(app, prefix="/api/v1")

api.add_resource(HelloWorld, '/')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
