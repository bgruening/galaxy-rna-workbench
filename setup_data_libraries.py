#!/usr/bin/env python

import os
import time
import argparse
import subprocess
import logging as log
from bioblend import galaxy
from subprocess import CalledProcessError


def main( args, shed_tools_root = '/shed_tools' ):
    """
    Load files into a Galaxy data library.
    By default all test-data tools from all installed tools
    will be linked into a data library.
    """

    log.info("Importing data libraries.")

    url = "http://localhost"
    # The environment variables are set by the parent container
    admin_email = os.environ.get('GALAXY_DEFAULT_ADMIN_USER', 'admin@galaxy.org')
    admin_pass = os.environ.get('GALAXY_DEFAULT_ADMIN_PASSWORD', 'admin')

    # Establish connection to galaxy instance
    gi = galaxy.GalaxyInstance(url=url, email=admin_email, password=admin_pass)

    log.info("Finding tools with test data")
    test_folders = dict()
    # Iterate over all installed tools

    for root, dirs, files in os.walk( shed_tools_root ):
        first = os.path.basename(os.path.normpath( root ))
        if first == 'test-data' and '.hg' not in root:
            second = os.path.dirname( root )
            file_list = '\n'.join( [ os.path.join(root, filename) for filename in files if not 'result' in filename] )
            test_folders[ os.path.basename(second) ] = file_list

    if test_folders:
        log.info("Create 'Test Data' library.")
        test_lib = gi.libraries.create_library('Test Data', 'Data pulled from tool test folders')
        test_lib_id = test_lib['id']

        for fname, files in test_folders.items():
            log.info("Creating folder: %s" % fname)
            # blacklist MSA datatype library
            if not 'msa' in fname:
                log.info("Creating folder: %s" % files)
                folder = gi.libraries.create_folder( test_lib_id, fname )
                gi.libraries.upload_from_galaxy_filesystem(
                    test_lib_id,
                    files,
                    folder_id = folder[0]['id'],
                    link_data_only = 'link_to_files'
                )
                time.sleep(1)

        # Wait for uploads to complete
        while True:
            try:
                ret = subprocess.check_output(["qstat"])
                if not len( ret.split('\n') ):
                    break
                time.sleep(3)
            except CalledProcessError as inst:
                if inst.returncode == 153: #queue is empty
                    break
                else:
                    raise

        time.sleep(10)
        log.info("Finished importing test data.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Populate the Galaxy data library with test files.'
    )
    parser.add_argument("-v", "--verbose", help="Increase output verbosity.",
                    action="store_true")

    #TODO:  Add options to override the admin_user and admin_password + specify 
    #       files to upload via command line interface.

    args = parser.parse_args()
    if args.verbose:
        log.basicConfig(level=log.DEBUG)

    main( args )
