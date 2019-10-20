import pkg_resources
import os
import logging
import shutil

from vew.util import PACKAGE_REQUIREMENT

LOG = logging.getLogger(__name__)
DATA_FILES = {
    'hugo_config': 'share/vew/hugo_config'
}

CONTENT_TEMPLATE = {
    'home/index.md': '''\
---
type: "widget_page"
headless: true
---
'''
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

        contenthomedir = os.path.join(self.path['root'], 'content', 'home')
        if not os.path.isdir(contenthomedir):
            os.makedirs(contenthomedir)

        contenthomefiles = ['home/index.md']
        for path in contenthomefiles:
            if os.path.isfile(contenthomedir):
                continue
            cpath = os.path.join(self.path['root'], 'content', path)
            with open(cpath, 'w+') as cfile:
                cfile.write(CONTENT_TEMPLATE[path])
