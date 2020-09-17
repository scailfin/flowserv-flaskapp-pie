# This file is part of the Reproducible and Reusable Data Analysis Workflow
# Server (flowServ).
#
# Copyright (C) 2019-2020 NYU.
#
# flowServ is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Blueprint for benchmark resources and benchmark leader boards."""

from flask import Blueprint, jsonify, make_response

from flaskflow.service import service

import flowserv.config.api as config


bp = Blueprint('benchmarks', __name__, url_prefix=config.API_PATH())


@bp.route('/workflows/<string:workflow_id>', methods=['GET'])
def get_workflow(workflow_id):
    """Get handle for given a workflow. This endpoint does not require the user
    to be authenticated.

    Parameters
    ----------
    workflow_id: string
        Unique workflow identifier

    Returns
    -------
    flask.response_class

    Raises
    ------
    flowserv.error.UnknownWorkflowError
    """
    with service() as api:
        r = api.workflows().get_workflow(workflow_id=workflow_id)
    return make_response(jsonify(r), 200)
