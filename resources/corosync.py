from flask import send_from_directory, request
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

    def post(self, path):
        file = request.files['file']
        if file.filename == "corosync.conf":
            file.save("/etc/corosync/corosync.conf")
        return '', 201
