""" vew.papis.joplin

papis-short-help: joplin help
"""
import logging
import json
import os
from datetime import datetime
from enum import Enum

import click

import papis.cli
import papis.config
import papis.api
import papis.commands.add

from vew.util import logging_setup, PACKAGE_NAME

LOG = logging.getLogger(__name__)


class JoplinType(Enum):
    note = 1
    folder = 2
    _unknown = 3 # TODO
    resource = 4
    tag = 5
    notetag = 6


def _joplin_default_settings(prefix):
    default_settings = {
        prefix: {
            'dir': './.vew/joplin',
            'add-name': '{doc[uuid]}',
            'file-name': '{doc[uuid]}',
        }
    }
    return default_settings

# TODO: This doesn't seem to be working
papis.config.register_default_settings(
    _joplin_default_settings(__name__)
)

def _papis_add_dryrun(**kwargs):
    LOG.info('papis add ({})'.format(kwargs))


def _joplin_time_to_date(joplin_time):
    time_in_s = int(joplin_time) / 1000
    return datetime.fromtimestamp(time_in_s).strftime('%Y-%m-%d')


def joplin_data_filter(data_out, data_in):
    # required:
    data_out['uuid'] = data_in['id']

    data_out['title'] = data_in['title']
    author = data_in.get('author', '')
    if author != '':
        data_out['author'] = author

    data_out['date'] = _joplin_time_to_date(
        data_in['user_created_time']
    )

    prefix = 'joplin_'
    joplin_type = JoplinType(data_in['type_'])
    data_out['{}type_str'.format(prefix)] = joplin_type.name
    for key in ['id', 'parent_id', 'type_', 'user_created_time', 'user_updated_time']:
        if key not in data_in:
            continue
        data_out[prefix + key] = data_in[key]

class JoplinData(object):
    def __init__(self, path):
        self._path = path
        self._data = {}
        self._jdata = {}
        self._files = [path]
        self._type = None

    def load(self):
        with open(self._path) as file_ptr:
            self._jdata = json.load(file_ptr)
        self._type = JoplinType(self._jdata['type_'])

        joplin_data_filter(self._data, self._jdata)

        if self._type == JoplinType.resource:
            self._files = [self._path_to_resource(self._jdata), self._path]

    @property
    def data(self):
        LOG.info('{} -> {}'.format(self._path, self._data))
        return self._data

    @property
    def files(self):
        return self._files

    def _path_to_resource(self, resource_data):
        root = os.path.dirname(self._path)
        resource_name = '{id}.{file_extension}'.format(**resource_data)
        return os.path.join( root, 'resources', resource_name)


@click.group()
@click.help_option('--help', '-h')
def joplin():
    """ VEW Papis Joplin
    """
    logging_setup()
    # LOG.info('joplin')
    LOG.info('get_lib() -> {}'.format(papis.api.get_libraries()))
    papis.config.set_lib(__name__)


@papis.cli.bypass(joplin, papis.commands.add.cli, "add")
def add(
    files,
    set_list,
    **kwargs
):
    logging_setup()
    # LOG.info(kwargs)

    dryrun = False
    papis_add = papis.commands.add.cli.bypassed
    if dryrun:
        papis_add = _papis_add_dryrun

    # these 3 lines are from papis:
    data = dict()
    for data_set in set_list:
        data[data_set[0]] = data_set[1]

    for doc_file in files:
        doc_args = dict(kwargs)
        doc_data = dict(data)

        joplin_data = JoplinData(doc_file)
        joplin_data.load()

        doc_data.update(joplin_data.data)
        doc_args['set_list'] = []
        for key in doc_data:
            doc_args['set_list'].append((key, doc_data[key]))

        doc_args['files'] = joplin_data.files
        doc_args['directory'] = doc_data['joplin_type_str']

        papis_add(**doc_args)


def _main():
    import papis.commands.default
    papis.commands.default.run()


if __name__ == "__main__":
    _main()
