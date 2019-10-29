""" vew.papis.joplin

papis-short-help: joplin help
"""
import logging

import click

import papis.cli
# import papis.config
import papis.commands.add

from vew.util import logging_setup, PACKAGE_NAME

LOG = logging.getLogger('{}.papis.joplin'.format(PACKAGE_NAME))


@click.group()
@click.help_option('--help', '-h')
def joplin():
    """ VEW Papis Joplin 
    """
    logging_setup()
    LOG.info('joplin')


@papis.cli.bypass(joplin, papis.commands.add.cli, "add")
def add(**kwargs):
    logging_setup()
    LOG.info(kwargs)

    papis.commands.add.cli.bypassed(**kwargs)


def _main():
    import papis.commands.default
    papis.commands.default.run()


if __name__ == "__main__":
    _main()
