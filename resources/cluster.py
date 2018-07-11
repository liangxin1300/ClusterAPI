from flask_restful import Resource
from flask import make_response
from common.util import get_cib_data

class Cluster(Resource):
    @get_cib_data("crm_config")
    def get(self):
        return make_response(cib_data)
