
from flask import Flask
from flask_bootstrap import Bootstrap



# Initialize Flask Application
app = Flask(__name__)
# Initialize Flask-Bootstrap
Bootstrap(app)


def init_app():
  """ Configure app """
  app.config['DEBUG'] = True

  return app;


""" Circular Import """
import routes
