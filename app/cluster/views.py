
from flask import Blueprint, make_response
from flask.views import MethodView
from app.common.helper import get_cib_data
from app.auth.helper import token_required

cluster = Blueprint('cluster', __name__)


class Cluster(MethodView):
    @token_required
    @get_cib_data("crm_config")
    def get(self):
        return make_response(cib_data)

    def post(self):
        return 'post cluster'


# Cluster class as view
cluster_view = Cluster.as_view('cluster')
# Add rule for the api Endpoints
cluster.add_url_rule('/cluster', view_func=cluster_view, methods=['GET', 'POST'])