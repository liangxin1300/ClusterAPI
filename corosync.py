from flask import send_from_directory
from flask_restful import Resource, reqparse
from string import Template

parser = reqparse.RequestParser()
parser.add_argument('port')
parser.add_argument('bindnetaddr')
parser.add_argument('ucastaddr')
parser.add_argument('mcastaddr')


class Corosync(Resource):

    def get(self, path):
        return send_from_directory("/etc/corosync", path)

    def post(self):
        args = parser.parse_args()
        with open('config/corosync.conf.template', 'r') as f:
            s = Template(f.read())
            data = s.substitute(bindnetaddr = args['bindnetaddr'],
                                mcastaddr = args['mcastaddr'],
                                port = args['port'],
                                expected_votes = 1,
                                two_node = 0)
        with open('corosync.conf', 'w') as f:
            f.write(data)
        return '', 201
