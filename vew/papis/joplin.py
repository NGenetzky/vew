""" vew.papis.joplin

papis-short-help: joplin help
"""
import logging
import json
from datetime import datetime

import click

import papis.cli
# import papis.config
import papis.commands.add

from vew.util import logging_setup, PACKAGE_NAME

LOG = logging.getLogger(__name__)

_TYPE_NOTE = 1
_TYPE_TO_STR = {
    _TYPE_NOTE: 'note',
}


def _papis_config_from_data(data):
    config = {}
    joplin_type = data.get('joplin_type_', None)
    if joplin_type in _TYPE_TO_STR:
        config['file-name'] = '{}'.format(
            _TYPE_TO_STR[joplin_type]
        )
    if 'uuid' in data:
        config['add-name'] = '{doc[uuid]}'
    return config


def _papis_add_dryrun(**kwargs):
    LOG.info('papis add ({})'.format(kwargs))


def _joplin_time_to_date(joplin_time):
    time_in_s = int(joplin_time) / 1000
    return datetime.fromtimestamp(time_in_s).strftime('%Y-%m-%d')


def joplin_data_filter(data_out, data_in):
    data_out['title'] = data_in['title']
    author = data_in.get('author', '')
    if author != '':
        data_out['author'] = author

    data_out['date'] = _joplin_time_to_date(
        data_in['user_created_time']
    )
    data_out['uuid'] = data_in['id']

    joplin_type = int(data_in['type_'])
    if joplin_type in _TYPE_TO_STR:
        data_out['joplin_type_str'] = _TYPE_TO_STR[joplin_type]

    prefix = 'joplin_'
    for key in ['id', 'parent_id', 'type_', 'user_created_time', 'user_updated_time']:
        data_out[prefix + key] = data_in[key]


def joplin_data(data_in, filename):
    data_out = dict(data_in)

    jdata = {}
    with open(filename) as file_ptr:
        jdata = json.load(file_ptr)
    joplin_data_filter(data_out, jdata)

    LOG.info('{} -> {}'.format(filename, data_out))
    return data_out


@click.group()
@click.help_option('--help', '-h')
def joplin():
    """ VEW Papis Joplin
    """
    logging_setup()
    # LOG.info('joplin')


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
        doc_args['files'] = [doc_file]
        doc_data = joplin_data(data, doc_file)

        doc_args['set_list'] = []
        for key in doc_data:
            doc_args['set_list'].append((key, doc_data[key]))

        doc_config = _papis_config_from_data(doc_data)
        config_to_arg = {
            'file-name': 'file_name',
            'add-name': 'name',
        }
        for c, a in config_to_arg.items():
            if c in doc_config:
                doc_args[a] = doc_config[c]

        papis_add(**doc_args)


def _main():
    import papis.commands.default
    papis.commands.default.run()


if __name__ == "__main__":
    _main()
