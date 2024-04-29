from flask import Flask  # Importing the Flask class from the Flask framework
from . import data_sync
import threading
def run_data_sync():
    """
        Function to run the data synchronization process.

        This function initiates the data synchronization process defined in the data_sync module.
    """
    data_sync.data_synchronization()


def create_app():
    """
    Creates and configures a Flask application instance.

    This function initializes a Flask application, registers blueprints,
    and returns the configured application instance.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)  # Creating a Flask application instance

    # Importing views module and registering the blueprint
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app  # Returning the configured Flask application instance

