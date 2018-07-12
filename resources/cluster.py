from flask import make_response, Blueprint
#from common.util import get_cib_data


bp = Blueprint('cluster', __name__)

@bp.route('/cluster')
def cluster():
    return make_response('hello cluster')

