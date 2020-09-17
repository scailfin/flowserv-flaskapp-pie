# This file is part of the Reproducible and Reusable Data Analysis Workflow
# Server (flowServ).
#
# Copyright (C) 2019-2020 NYU.
#
# flowServ is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Errors that are raised by the web service (in addition to those that are
already defined and raised by API service components of flowServ).
"""


class InvalidRequestError(Exception):
    """Error that is raised when a user request does not contain a valid
    request body.
    """
    def __init__(self, message: str):
        """Initialize error message.

        Parameters
        ----------
        message : string
            Error message.
        """
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        """Get printable representation of the exception.

        Returns
        -------
        string
        """
        return self.message
