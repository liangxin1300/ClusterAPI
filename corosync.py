from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('port')

class Corosync(Resource):

    def post(self):
        args = parser.parse_args()
        print({'task': args['port']})
        return '', 201
