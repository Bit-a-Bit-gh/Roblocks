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

from os.path import dirname, realpath, join


ORG_NAME = 'Bit-a-Bit'


def _default_orgdirs():
    """Get the default org's directories"""
    return open(join(dirname(realpath(__file__)),'assets', 'orgdirs.yaml'))


def _default_prjdirs():
    """Get the default project's directories"""
    return open(join(dirname(realpath(__file__)),'assets', 'prjdirs.yaml'))