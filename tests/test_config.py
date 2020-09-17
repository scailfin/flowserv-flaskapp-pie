# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB).
#
# Copyright (C) [2019-2020] NYU.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Unit tests for functions in the config module that provide access to values
in environment variables that are used to configure the Flowserv App.
"""

import os
import pytest

import flaskflow.config as config


def test_logdir():
    """Test getting the environment variable value for the logging directory
    that is used by the Flask service.
    """
    # -- Setup ----------------------------------------------------------------
    # Clear the environment variables if it is set
    if config.FLASKFLOW_LOG in os.environ:
        del os.environ[config.FLASKFLOW_LOG]
    # -- Tests ----------------------------------------------------------------
    # The default value is a subfolder in the API base dir with name 'log'
    assert os.path.basename(config.LOG_DIR()) == 'log'
    # Set the environment variable and ensure that the absolute pathname to
    # the specified directory is returned by the config LOG_DIR() function
    os.environ[config.FLASKFLOW_LOG] = '.log/api'
    assert config.LOG_DIR() == os.path.abspath('.log/api')
    # -- Cleanup --------------------------------------------------------------
    del os.environ[config.FLASKFLOW_LOG]


def test_max_upload_size():
    """Test accessing the maximum file size for file uploads."""
    # -- Setup ----------------------------------------------------------------
    # Clear the environment variables if it is set
    if config.FLASKFLOW_CONTENTLENGTH in os.environ:
        del os.environ[config.FLASKFLOW_CONTENTLENGTH]
    # -- Tests ----------------------------------------------------------------
    # The default value is equal to 16MB
    assert config.MAX_CONTENT_LENGTH() == 16 * 1024 * 1024
    # Set the environment variable and ensure that the respective value is
    # returned as an integer
    os.environ[config.FLASKFLOW_CONTENTLENGTH] = '1234'
    assert config.MAX_CONTENT_LENGTH() == 1234
    # A ValueError is raised if the environment variable is set to a value
    # than cannot be converted to integer
    os.environ[config.FLASKFLOW_CONTENTLENGTH] = 'ABC'
    with pytest.raises(ValueError):
        config.MAX_CONTENT_LENGTH()
    # -- Cleanup --------------------------------------------------------------
    del os.environ[config.FLASKFLOW_CONTENTLENGTH]
