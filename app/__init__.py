from flask import Flask, render_template
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=False)

    app.config.from_mapping(
        SECRET_KEY='dev', # Should be random in production
        DATABASE='mongodb://localhost:27017/'
    )

    if test_config is not None:
        app.config.from_mapping(test_config)

    @app.route('/')
    def hello():
        return render_template('index.html')

    CORS(app, supports_credentials=True)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import usr
    app.register_blueprint(usr.bp)

    from . import course
    app.register_blueprint(course.bp)

    from . import comment
    app.register_blueprint(comment.bp)

    from . import focus
    app.register_blueprint(focus.bp)

    from . import collection
    app.register_blueprint(collection.bp)

    return app
