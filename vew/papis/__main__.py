import papis
import click
import logging

from vew.util import logging_setup, PACKAGE_NAME
from vew.papis.config import PapisConfig

LOG = logging.getLogger('{}.papis'.format(PACKAGE_NAME))


@click.command("cli", help="Add a document into a given library")
@click.help_option('--help', '-h')
@click.option("--root", type=click.Path(exists=True), nargs=1)
@click.option("--init", default=False, is_flag=True)
def cli(root, init):
    LOG.info(root)

    if init:
        papisconfig = PapisConfig(root)
        papisconfig.init_local()
        papisconfig.init_global()


if __name__ == "__main__":
    cli()
