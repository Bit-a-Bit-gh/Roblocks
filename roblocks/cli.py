#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the entry point for the command-line interface (CLI) application.

It can be used as a handy facility for running the task from a command line.

.. note::

    To learn more about Click visit the
    `project website <http://click.pocoo.org/5/>`_.  There is also a very
    helpful `tutorial video <https://www.youtube.com/watch?v=kNke39OZ2k0>`_.

    To learn more about running Luigi, visit the Luigi project's
    `Read-The-Docs <http://luigi.readthedocs.io/en/stable/>`_ page.

.. currentmodule:: roblocks.cli
.. moduleauthor:: Bit-a-Bit <github@bit-a-bit.info>
"""
import logging
import os
import click
from yamldirs.filemaker import Filemaker
from . import defaults
from .__init__ import __version__


LOGGING_LEVELS = {
    0: logging.NOTSET,
    1: logging.ERROR,
    2: logging.WARN,
    3: logging.INFO,
    4: logging.DEBUG,
}  #: a mapping of `verbose` option counts to logging levels


class Info(object):
    """An information object to pass data between CLI functions."""

    def __init__(self):  # Note: This object must have an empty constructor.
        """Create a new instance."""
        self.verbose: int = 0


# pass_info is a decorator for functions that pass 'Info' objects.
#: pylint: disable=invalid-name
pass_info = click.make_pass_decorator(Info, ensure=True)


# Change the options to below to suit the actual options for your task (or
# tasks).
@click.group()
@click.option("--verbose", "-v", count=True, help="Enable verbose output.")
@pass_info
def cli(info: Info, verbose: int):
    """Run roblocks."""
    # Use the verbosity count to determine the logging level...
    if verbose > 0:
        logging.basicConfig(
            level=LOGGING_LEVELS[verbose]
            if verbose in LOGGING_LEVELS
            else logging.DEBUG
        )
        click.echo(
            click.style(
                f"Verbose logging is enabled. "
                f"(LEVEL={logging.getLogger().getEffectiveLevel()})",
                fg="yellow",
            )
        )
    info.verbose = verbose


@cli.command()
@pass_info
def hello(_: Info):
    """Say 'hello' to the nice people."""
    click.echo("roblocks says 'hello'")


@cli.command()
def version():
    """Get the library version."""
    click.echo(click.style(f"{__version__}", bold=True))


@click.group()
def createdirs():
    """Creates directories."""
    pass

@createdirs.command()
@click.argument('org_root', required=False)
@click.argument('fdef', required=False)
@pass_info
def org(_: Info, org_root='default', fdef='default'):
    """Create org's directories."""
    if org_root=='default':
        org_root = os.path.expanduser('~')
    if fdef=='default':
        fdef = defaults._default_orgdirs()
    Filemaker(org_root, fdef)

@createdirs.command()
@click.argument('org_root')
@click.argument('fdef', required=False, default='default')
@pass_info
def project(_: Info, org_root, fdef='default'):
    """Create a project's directories."""
    if fdef=='default':
        fdef = defaults._default_prjdirs()
    Filemaker(org_root, fdef)

cli.add_command(createdirs)
