import os
import yaml
import logging.config
import logging

PACKAGE_NAME = 'vew'
DEFAULT_LOG_CFG = '~/.config/{}/logging.yaml'.format(PACKAGE_NAME)


def logging_setup(default_path=DEFAULT_LOG_CFG, default_level=logging.INFO, env_key='LOG_CFG'):
    """Set up logging using YAML configuration file

    Reference: kingspp/logging.py
        https://gist.github.com/kingspp/9451566a5555fb022215ca2b7b802f19
    """
    path = os.getenv(env_key, default_path)
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        logging.basicConfig(level=default_level)
        print('Failed to load configuration file. Using default configs')
        return

    with open(path, 'rt') as f:
        try:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        except Exception as e:
            print(e)
            print('Error in Logging Configuration. Using default configs')
            logging.basicConfig(level=default_level)
