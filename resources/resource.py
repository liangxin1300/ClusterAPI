from flask_restful import Resource
from flask import make_response
from common.util import get_cib_data


class Resource(Resource):
    @get_cib_data("resources")
    def get(self):
        return make_response(cib_data)
