from flask import Flask, Blueprint, request, jsonify

__version__ = '0.0.1'

client = Blueprint('client', __name__, url_prefix='/client')


@client.route("/info")
def client_user_info():
    return jsonify({"user_agent": request.headers.get("User-Agent", "")})


def init_app():
    app = Flask(__name__)
    app.register_blueprint(client)
    return app
