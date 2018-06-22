from flask_restful import Resource

class Cluster(Resource):
    def get(self):
        return {"cluster": "cluster_name"}
