##!/usr/bin/env python
## much from scripts/api/data_manager_example_execute.py
import time
import argparse
import urlparse
import ConfigParser
from bioblend.galaxy import GalaxyInstance
from bioblend.galaxy.client import ConnectionError

if __name__ == '__main__':
    print "booting up..."
    parser = argparse.ArgumentParser(description='Fetching and Indexing genomes.')
    parser.add_argument("--config", required=True, help="Path to config file.")

    options = parser.parse_args()

    # read from config
    config = ConfigParser.ConfigParser()
    config.read(options.config)

    fetch_tool = config.get('main', 'genome_fetch_tool')
    url = config.get('main', 'galaxy_base_url')
    sleep_time = float(config.get('main', 'sleep_time'))

    admin_email = config.get('admin', 'email')
    admin_pass = config.get('admin', 'password')
    
    genomes = config.get('genomes', 'ids').strip().split('\n')
    index_tools = config.get('build_indexers', 'ids').strip().split('\n')

    # should test for valid config options
    
    # establish connection to galaxy instance
    gi = GalaxyInstance(url=url, email=admin_email, password=admin_pass)

    # should test valid connection
    print gi.histories.get_histories()

    # fetch genomes
    dbkeys = {}
    for dbkey in genomes:
        if dbkey not in dbkeys:
            tool_inputs={'dbkey':dbkey, 'reference_source|reference_source_selector': 'ucsc', 'reference_source|requested_dbkey': dbkey }
            print "fetching: ", dbkey, "..."
            
            try:                         
                dbkeys[ dbkey ] = gi.tools.run_tool(history_id=None, tool_id=fetch_tool, tool_inputs=tool_inputs)

            except ConnectionError as inst:
                if '\"dbkey\": \"An invalid option was selected' in inst.body:
                    print "Galaxy instance does not recognize genome key: ", dbkey, "..aborting"
                    raise
                else:
                    raise

        else:
            "dbkey (%s) was specified more than once, skipping additional specification." % ( dbkey )

    # start indexers
    print "waiting to index"
    indexing_tools = []
    while dbkeys:
        for dbkey, value in dbkeys.items():
            print dbkey,": ",gi.datasets.show_dataset( value['outputs'][0]['id'] )['state']
            if gi.datasets.show_dataset( value['outputs'][0]['id'] )['state'] in ['ok', 'error']:
                
                # refresh the tool data tables
                print gi.make_get_request(urlparse.urljoin(url,'api/tool_data/all_fasta/reload')).text
                time.sleep(5)
                print gi.make_get_request(urlparse.urljoin(url,'api/tool_data/all_fasta/reload')).text
                
                for tool_id in index_tools:
                    print "indexing",dbkey, "with", tool_id
                    
                    try:
                        print "dbkey: ",dbkey
                        blah = gi.tools.run_tool(history_id=None, tool_id=tool_id, tool_inputs={ 'all_fasta_source':dbkey })
                        print "===========================\n",blah,"\n==========================="
                        indexing_tools.append(blah)

                    except ConnectionError as inst:
                        if '\"text\": \"no tool\",' in inst.body:
                            print "The tool [", tool_id, "] cannot be located. Please check it is installed in your galaxy instance."
                        else:
                            raise
                del dbkeys[ dbkey ]
        if dbkeys:
            time.sleep(sleep_time)
            print ".",

    #Wait for indexers to finish
    while indexing_tools:
        for i, indexing_tool_value in enumerate( indexing_tools ):
            if gi.datasets.show_dataset( indexing_tool_value['outputs'][0]['id'] )['state'] in ['ok', 'error']:
                print 'Finished:', indexing_tool_value
                del indexing_tools[i]
                break
        if indexing_tools:
            time.sleep(sleep_time)
                
    print 'All indexers have been run, please check results.'
