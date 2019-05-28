from . import focus, course, usr, comment, completeness

def init_app(app):
    app.register_blueprint(focus.bp)
    app.register_blueprint(course.bp)
    app.register_blueprint(usr.bp)
    app.register_blueprint(comment.bp)
    app.register_blueprint(completeness.bp)
