from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.rout('/')
def home_index():
    return 'sisisibal'