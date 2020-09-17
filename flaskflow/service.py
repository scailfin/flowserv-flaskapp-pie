# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB).
#
# Copyright (C) [2019-2020] NYU.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Helper classes method to create instances of the flowServ API. All instances
use the same underlying database connection. The connection object is under the
control of of a context manager to ensure that the connection is closed
properly after every API request has been handled.
"""

from contextlib import contextmanager

from flowserv.service.api import API


@contextmanager
def service():
    """The local service function is a context manager for an open database
    connection that is used to instantiate the service class for the flaskflow
    API. The context manager ensures that the database conneciton in closed
    after a API request has been processed.

    Returns
    -------
    flaskflow.service.API
    """
    from flaskflow.database import flowdb
    with flowdb.session() as session:
        yield API(session=session)
