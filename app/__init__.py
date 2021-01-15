import logging

from flask import Flask, jsonify, make_response, render_template

import flowserv.error as err


"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)


def create_app(test_config=None):
    """Initialize the Flask application follwoing the app factory pattern."""
    app = Flask(__name__, instance_relative_config=True)
    # Load the default configuration.
    app.config.from_object('app.config.Config')
    # Override configuration depending on the application environment. Place
    # configuration files into the instance/ folder in the project directory.
    if app.env == 'production':
        app.config.from_pyfile('production.py', silent=True)
    else:
        app.config.from_pyfile('development.py', silent=True)
    # Override configuration with optional test configuration settings.
    if test_config is not None:
        app.config.update(test_config)

    # -------------------------------------------------------------------------
    # Define error handlers
    # -------------------------------------------------------------------------
    @app.errorhandler(err.FlowservError)
    def flowserv_error(error):
        """JSON response handler for requests that raise an error in one of the
        flowserv components.
        """
        app.logger.error(error)
        return make_response(jsonify({'message': str(error)}), 400)

    @app.errorhandler(404)
    def page_not_found(error):
        """Custom 'File Not Found' error handler."""
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Error handler that logs internal server errors."""
        app.logger.error(error)
        return make_response(jsonify({'error': str(error)}), 500)

    # --------------------------------------------------------------------------
    # Import blueprints for App components
    # --------------------------------------------------------------------------
    # Main view.
    from app import view
    app.register_blueprint(view.bp)

    # -------------------------------------------------------------------------
    # Return the app
    # -------------------------------------------------------------------------
    return app
