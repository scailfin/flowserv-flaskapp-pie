"""Global variable that provides access to the application workflow. Maintains
the workflow engine and database connection.
"""

from flowserv.client.app.base import open_app

"""Create an instance of the workflow application."""
flowapp = open_app()
