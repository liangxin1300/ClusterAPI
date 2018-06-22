from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('port')
parser.add_argument('bindnetaddr')
parser.add_argument('ucastaddr')
parser.add_argument('mcastaddr')


class Corosync(Resource):

    def post(self):
        args = parser.parse_args()
        #print({'port': args['port']})
        #print({'bindnetaddr': args['bindnetaddr']})
        #print({'mcastaddr': args['mcastaddr']})
        return '', 201
