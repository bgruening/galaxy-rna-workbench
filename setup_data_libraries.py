#!/usr/bin/env python

import argparse
import logging as log
import sys
import time

import yaml
from bioblend import galaxy


def setup_data_libraries(gi, data):
    """
    Load files into a Galaxy data library.
    By default all test-data tools from all installed tools
    will be linked into a data library.
    """

    log.info("Importing data libraries.")
    jc = galaxy.jobs.JobsClient(gi)

    folders = dict()

    libraries = yaml.load(data)
    for lib in libraries['libraries']:
        folders[lib['name']] = lib['files']

    if folders:
        log.info("Create 'Test Data' library.")
        lib = gi.libraries.create_library('Training Data', 'Data pulled from online archives.')
        lib_id = lib['id']

        for fname, urls in folders.items():
            log.info("Creating folder: %s" % fname)
            folder = gi.libraries.create_folder(lib_id, fname)
            for url in urls:
                gi.libraries.upload_file_from_url(
                    lib_id,
                    url['url'],
                    folder_id=folder[0]['id'],
                    file_type=url['file_type']
                )

        no_break = True
        while True:
            no_break = False
            for job in jc.get_jobs():
                if job['state'] != 'ok':
                    no_break = True
            if not no_break:
                break
            time.sleep(3)

        time.sleep(20)
        log.info("Finished importing test data.")


def main():
    parser = argparse.ArgumentParser(
        description='Populate the Galaxy data library with test data.'
    )
    parser.add_argument("-v", "--verbose", help="Increase output verbosity.",
                        action="store_true")
    parser.add_argument('-i', '--infile', type=argparse.FileType('r'))
    parser.add_argument("-g", "--galaxy",
                        help="Target Galaxy instance URL/IP address.")
    parser.add_argument("-u", "--user",
                        help="Galaxy user name")
    parser.add_argument("-p", "--password",
                        help="Password for the Galaxy user")
    parser.add_argument("-a", "--api_key",
                        dest="api_key",
                        help="Galaxy admin user API key (required if not defined in the tools list file)")

    args = parser.parse_args()

    if args.user and args.password:
        gi = galaxy.GalaxyInstance(url=args.galaxy, email=args.user, password=args.password)
    elif args.api_key:
        gi = galaxy.GalaxyInstance(url=args.galaxy, key=args.api_key)
    else:
        sys.exit('Please specify either a valid Galaxy username/password or an API key.')

    if args.verbose:
        log.basicConfig(level=log.DEBUG)

    setup_data_libraries(gi, args.infile)


if __name__ == '__main__':
    main()
