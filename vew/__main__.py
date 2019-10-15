import logging
import sys

from vew.util import logging_setup, PACKAGE_NAME

LOG = logging.getLogger(PACKAGE_NAME)

def stub(argv=sys.argv[1:]):
    logging_setup()
    LOG.info(argv)

def main(argv=sys.argv[0:]):
    logging_setup()
    LOG.info(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[0:]))
