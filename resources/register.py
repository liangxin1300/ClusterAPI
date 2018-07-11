from flask_restful import Resource, abort
from flask import make_response
from common.util import check_pam, create_token
import json
import os


class Register(Resource):

    def __init__(self, parser):
        self.parser = parser
        self.parser.add_argument('username')
        self.parser.add_argument('password')

    def post(self):
        args = self.parser.parse_args()
        username = args['username']
        password = args['password']
        if not check_pam(username, password):
            abort(401)

        token_data = {}
        token_data['username'] = username
        token_data['token'] = create_token(username)
        json_data = json.dumps(token_data)

        root = '/'.join(os.path.dirname(__file__).split('/')[:-1])
        with open("%s/api_token_entries.store" % root, 'w') as f:
            f.write(json_data)

        return make_response(json_data)
