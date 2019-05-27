from flask import Flask, render_template
from flask_cors import CORS
import config

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.' + config_name)

    @app.route('/')
    def hello():
        return render_template('index.html')

    CORS(app, supports_credentials=True)

    from . import db, auth, api

    db.init_app(app)
    api.init_app(app)
    app.register_blueprint(auth.bp)

    return app
