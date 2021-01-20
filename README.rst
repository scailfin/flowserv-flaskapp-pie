===================================================
Flowserv Flask App - Processing Images Easily (PIE)
===================================================

This repository demonstrates the use of the `Flask App Template <https://github.com/scailfin/flowserv-flaskapp>`_ for running custom applications based on **flowserv** workflows. This project uses the HTML templates from the `pie-flask <https://github.com/CoraJung/pie-flask>`_ repository to expose the Colony Recognition Analysis workflow from the `Processing Images Easily (PIE) project  <https://github.com/Siegallab/PIE>`_ via a web interface.


Installation & Configuration
============================

Install Project Sources and Dependencies
----------------------------------------

We recommend using a virtual environment for the installation (e.g., ``conda create -n pieflask python=3.8 pip`` if using Anaconda). At the time of writing, the following commands would not work with Python 3.9 (but only 3.7 or 3.8). After activating the virtual environment (e.g., ``conda activate pieflask``) first clone the repository and then install the project requirements:

.. code-block:: bash

    git clone git@github.com:scailfin/flowserv-flaskapp-pie.git
    cd flowserv-flaskapp-pie
    pip install -r requirements.txt


Configure and Setup Flowserv
----------------------------

The next step is to setup your local **flowserv** instance. The following will maintain all files in a subfolder ``.flowsev`` within the cloned repository. Start by setting the environment variables that configure **flowserv**.

.. code-block:: bash

    export FLOWSERV_API_DIR=$PWD/.flowserv
    export FLOWSERV_DATABASE=sqlite:///$FLOWSERV_API_DIR/flowserv.db


The next step is to initialize the **flowserv** database and install the PIE workflow template.

.. code-block:: bash

    flowserv init -f
    flowserv app install piesingle -k piesingle


Run The Web Server
==================

After finishing the setup, make sure to set the following environment variables:

.. code-block:: bash

    # Set the workflow identifier.
    export FLOWSERV_APP=piesingle
    # Context that Flask runs in. Defaults to `production` but here it is
    # recommended to switch to the development environment.
    export FLASK_ENV=development
    export FLASK_APP=app

    run flask

If you open the URL `http://127.0.0.1:5000/ <http://127.0.0.1:5000/>`_ in your browser you should see the following screen:

.. figure:: https://raw.githubusercontent.com/scailfin/flowserv-flaskapp-pie/master/app/static/img/screenshots/home.png
  :align: center
  :alt: Application Home Screen

To upload a colony image and run the analysis workflow go to `http://127.0.0.1:5000/runs <http://127.0.0.1:5000/runs>`_:

.. figure:: https://raw.githubusercontent.com/scailfin/flowserv-flaskapp-pie/master/app/static/img/screenshots/run.png
  :align: center
  :alt: Workflow Run Submission Screen
  
The PIE repository contains `sample images <https://github.com/Siegallab/PIE/tree/master/PIE_test_data/IN>`_ that can be uploaded when submitting a workflow run.
