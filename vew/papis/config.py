import logging
import os
import configparser

import papis.config


class PapisConfig(papis.config.Configuration):
    default_info_template = {
        "default": {
            'dir': '{root}/default'
        },
    }

    default_info = {
        'settings': {
            'default-library': 'default',
            'use-git': 'True',
        }
    }

    logger = logging.getLogger("{}.Configuration".format(__name__))

    def __init__(self, root):
        configparser.ConfigParser.__init__(self)
        self.data = {
            'root': os.path.abspath(root)
        }

    def _fill_default_info(self, data):
        for section in self.default_info_template:
            if section not in self.default_info:
                self.default_info[section] = {}
            for field in self.default_info_template[section]:
                self.default_info[section][field] = self.default_info_template[section][field].format(
                    **data)

    def init_global(self, config_dir=None):
        self.dir_location = config_dir
        if self.dir_location is None:
            self.dir_location = papis.config.get_config_folder()

        self._fill_default_info(data=self.data)

        self.scripts_location = os.path.join(self.dir_location, "scripts")
        self.file_location = os.path.join(self.dir_location, "config")
        self.initialize()

    def init_local(self, localdir=None):
        if localdir is None:
            localdir = self.data['root']

        localconfig = os.path.join(localdir, '.papis.config')
        if os.path.exists(localconfig):
            return
        self._fill_default_info(data={'root': './'})
        for section in self.default_info:
            self[section] = {}
            for field in self.default_info[section]:
                self[section][field] = self.default_info[section][field]
        with open(localconfig, "w") as configfile:
            self.write(configfile)
