from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app,db)
    from . import models
    from .views import main_views, list_views, comments_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(list_views.bp)
    app.register_blueprint(comments_views.bp)

    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    # mark down
    Markdown(app, extensions=['nl2br','fenced_code'])
    return app
