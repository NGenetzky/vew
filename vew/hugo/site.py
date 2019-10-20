import pkg_resources
import os
import logging
import shutil

from vew.util import PACKAGE_REQUIREMENT

LOG = logging.getLogger(__name__)
DATA_FILES = {
    'hugo_config': 'share/vew/hugo_config'
}


class HugoSite(object):
    def __init__(self, root=None):
        self.path = {
            'root': root,
        }

    def init(self):
        if not os.path.isdir(self.path['root']):
            raise ValueError('root not isdir({})'.format(self.path['root']))

        configdir = os.path.join(self.path['root'], 'config', '_default')
        if not os.path.isdir(configdir):
            os.makedirs(configdir)
            self.path['hugo_config'] = pkg_resources.resource_filename(
                PACKAGE_REQUIREMENT, DATA_FILES['hugo_config']
            )
            for filename in os.listdir(self.path['hugo_config']):
                shutil.copy2(os.path.join(
                    self.path['hugo_config'], filename), configdir)
