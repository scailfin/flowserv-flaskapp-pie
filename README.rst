============================================================================
Reproducible and Reusable Data Analysis Workflow Server - Flask App Template
============================================================================

This is a simple exmple project for running an arbitrary **flowserv** workflow as a Flask application. Use this as the starting template for creating your own application by modifying the HTML files in the templates directory.


Configuration
=============

Set the context that Flask runs in using the environment variable **FLASK_ENV**. The variable defaults to `production`. To switch to the development environment and enable debug mode:

.. code-block:: bash

    export FLASK_ENV=development


Set the **FLOWSERV_APP** environment variable (and other variables that configure **flowserv**) before running the flask server.


.. code-block:: bash

    export FLOWSERV_APP=your-application-key
    export FLASK_APP=app

    run flask
