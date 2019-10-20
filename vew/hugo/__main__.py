import logging
import sys
import argparse

from vew.util import logging_setup, PACKAGE_NAME
from vew.hugo.site import HugoSite

LOG = logging.getLogger('{}.hugo'.format(PACKAGE_NAME))


def _parse_args(argv):
    parser = argparse.ArgumentParser(description='VEW Hugo')
    parser.add_argument(
        '--root', metavar='PATH',
        help='root directory of HugoSite',
    )
    parser.add_argument(
        '--init', action='store_true',
        help='Initialize object and directory',
    )
    return parser.parse_args(argv)


def main(argv=sys.argv[1:]):
    logging_setup()
    LOG.info(argv)
    args = _parse_args(argv)

    if args.init:
        hugosite = HugoSite(args.root)
        hugosite.init()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
