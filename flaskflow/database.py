# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB).
#
# Copyright (C) [2019-2020] NYU.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Global variable for the flowServ database instance that is to be (re-)used
by all requests to the web app and API.
"""

from flowserv.model.database import DB


"""Global database instance for all requests."""
flowdb = DB(web_app=True)
