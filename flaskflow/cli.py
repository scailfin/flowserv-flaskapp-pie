# This file is part of the Reproducible and Reusable Data Analysis Workflow
# Server (flowServ).
#
# Copyright (C) 2019-2020 NYU.
#
# flowServ is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Command line interface for the administrative tasks to configure the
environment, intialize the underlying database, and to install and delete
workflow templates
"""

import click

from flowserv.app import install_app, list_apps, uninstall_app
from flowserv.cli.admin import init
from flowserv.cli.config import get_configuration
from flowserv.cli.repository import list_repository

import flaskflow.config as config


@click.group()
def cli():
    """Command line interface for administrative tasks to manage a flaskflow
    instance.
    """
    pass


@cli.command(name='config')
def configuration():
    """Print configuration variables for flaskflow and flowServ."""
    comment = '\n#\n# {}\n#\n'
    envvar = 'export {}={}'
    click.echo(comment.format('Flaskflow'))
    click.echo(envvar.format(config.FLASKFLOW_LOG, config.LOG_DIR()))
    click.echo(envvar.format(
        config.FLASKFLOW_CONTENTLENGTH,
        config.MAX_CONTENT_LENGTH()
    ))
    click.echo('\n\n\nConfiguration for flowServ\n==========================')
    for title, envs in get_configuration().items():
        click.echo(comment.format(title))
        for var, val in envs.items():
            click.echo(envvar.format(var, val))
    click.echo()


@cli.command(name='install')
@click.option(
    '-i', '--id',
    required=False,
    help='Workflow identifier.'
)
@click.option(
    '-n', '--name',
    required=False,
    help='Workflow title.'
)
@click.option(
    '-d', '--description',
    required=False,
    help='Workflow sub-title.'
)
@click.option(
    '-i', '--instructions',
    type=click.Path(exists=False),
    required=False,
    help='File containing detailed instructions.'
)
@click.option(
    '-t', '--specfile',
    type=click.Path(exists=True, dir_okay=False, readable=True),
    required=False,
    help='Optional path to workflow specification file.'
)
@click.option(
    '-m', '--manifest',
    type=click.Path(exists=True, dir_okay=False, readable=True),
    required=False,
    help='Optional path to workflow manifest file.'
)
@click.argument('template')
def install_workflow(
    id, name, description, instructions, specfile, manifest, template
):
    """Install workflow from local folder or repository."""
    # Install the application from the given workflow template.
    app_key = install_app(
        source=template,
        identifier=id,
        name=name,
        description=description,
        instructions=instructions,
        specfile=specfile,
        manifestfile=manifest
    )
    click.echo('installed workflow {}'.format(app_key))


@cli.command(name='list')
def list_workflows():
    """Listing of installed workflows."""
    for name, key in list_apps():
        click.echo('{}\t{}'.format(key, name))


@cli.command('uninstall')
@click.argument('identifier')
def uninstall_workflow(identifier):
    """Uninstall wirkflow with given identifier."""
    uninstall_app(app_key=identifier)


cli.add_command(init)
cli.add_command(configuration)
cli.add_command(install_workflow)
cli.add_command(list_workflows)
cli.add_command(list_repository, name='repository')
cli.add_command(uninstall_workflow)
