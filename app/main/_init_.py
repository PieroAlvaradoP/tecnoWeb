from flask import Blueprint

main = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

from app.main import views
from app.main import api