##!/usr/bin/env python
## much from scripts/api/data_manager_example_execute.py
import os
import time
import argparse
import urlparse
import ConfigParser
import logging as log
from bioblend.galaxy import GalaxyInstance
from bioblend.galaxy.client import ConnectionError

def main( options ):

    # read from config
    config = ConfigParser.ConfigParser()
    config.read(options.config)

    fetch_tool = config.get('main', 'genome_fetch_tool')
    url = "http://localhost"
    sleep_time = float(config.get('main', 'sleep_time'))

    # The environment variables are set by the parent container
    admin_email = os.environ.get('GALAXY_DEFAULT_ADMIN_USER', 'admin@galaxy.org')
    admin_pass = os.environ.get('GALAXY_DEFAULT_ADMIN_PASSWORD', 'admin')
    
    genomes = config.get('genomes', 'ids').strip().split('\n')
    index_tools = config.get('build_indexers', 'ids').strip().split('\n')

    # should test for valid config options
    # establish connection to galaxy instance
    gi = GalaxyInstance(url=url, email=admin_email, password=admin_pass)

    # should test valid connection
    log.info("List of valid histories: %s" % gi.histories.get_histories())

    # fetch genomes
    dbkeys = dict()
    for dbkey in genomes:
        if dbkey not in dbkeys:
            tool_inputs={'dbkey':dbkey, 'reference_source|reference_source_selector': 'ucsc', 'reference_source|requested_dbkey': dbkey }
            log.info("Fetching dbkey: %s" % dbkey)

            try:
                dbkeys[ dbkey ] = gi.tools.run_tool(history_id=None, tool_id=fetch_tool, tool_inputs=tool_inputs)

            except ConnectionError as inst:
                if '\"dbkey\": \"An invalid option was selected' in inst.body:
                    log.error("Galaxy instance does not recognize genome key: %s" % dbkey)
                raise
        else:
            log.info("The dbkey (%s) was specified more than once, skipping additional specification." % ( dbkey ))

    gi.make_get_request(urlparse.urljoin(url,'api/tool_data/all_fasta/reload'))

    # start indexers
    log.info("Start building genome indices.")
    indexing_tools = []
    while dbkeys:
        for dbkey, value in dbkeys.items():
            if gi.datasets.show_dataset( value['outputs'][0]['id'] )['state'] in ['ok', 'error']:

                # refresh the tool data tables
                log.info("Refreshing tool-data tables.")
                log.info( gi.make_get_request(urlparse.urljoin(url,'api/tool_data/all_fasta/reload')).text )
                time.sleep(2)
                for tool_id in index_tools:
                    log.info("Indexing %s with %s." % (dbkey, tool_id) )
                    try:
                        indexing_tools.append(gi.tools.run_tool(history_id=None, tool_id=tool_id, tool_inputs={ 'all_fasta_source':dbkey }))

                    except ConnectionError as inst:
                        if '\"text\": \"no tool\",' in inst.body:
                            log.info("The tool %s cannot be located. Please check it is installed in your galaxy instance." % (tool_id) )
                        else:
                            raise

                del dbkeys[ dbkey ]
        if dbkeys:
            time.sleep(sleep_time)
            log.info(".")

    # Wait for indexers to finish
    while indexing_tools:
        for i, indexing_tool_value in enumerate( indexing_tools ):
            if gi.datasets.show_dataset( indexing_tool_value['outputs'][0]['id'] )['state'] in ['ok', 'error']:
                log.info('Finished %s.' % indexing_tool_value)
                del indexing_tools[i]
                break
        if indexing_tools:
            time.sleep(sleep_time)

    log.info('All indexers have been run, please check results.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Fetching and Indexing genomes.'
    )
    parser.add_argument("-v", "--verbose", help="Increase output verbosity.",
                    action="store_true")
    parser.add_argument("--config", required=True, help="Path to config file.")

    #TODO:  Add options to override the admin_user and admin_password + specify 
    #       files to upload via command line interface.

    args = parser.parse_args()
    if args.verbose:
        log.basicConfig(level=log.DEBUG)

    log.info("Fetch and Index genomes ...")
    main( args )


