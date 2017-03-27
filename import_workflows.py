#!/usr/bin/env python
import argparse
import json
import os

from bioblend import galaxy


def import_workflow(gi, path):
    with open(path, 'r') as wf_file:
        import_uuid = json.load(wf_file).get('uuid')
    existing_uuids = [d.get('latest_workflow_uuid') for d in gi.workflows.get_workflows()]
    if import_uuid not in existing_uuids:
        gi.workflows.import_workflow_from_local_path(path)


def main():
    """
        This script uses bioblend to import .ga workflow files into a running instance of Galaxy
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--workflow_path",
                        help='Path to workflow file or a directory with multiple workflow files ending with ".ga"')
    parser.add_argument("-g", "--galaxy",
                        dest="galaxy_url",
                        help="Target Galaxy instance URL/IP address (required "
                             "if not defined in the tools list file)",)
    parser.add_argument("-a", "--apikey",
                        dest="api_key",
                        help="Galaxy admin user API key (required if not "
                             "defined in the tools list file)",)
    args = parser.parse_args()

    gi = galaxy.GalaxyInstance(url=args.galaxy_url, key=args.api_key)

    if os.path.isdir(args.workflow_path):
        for file_path in os.listdir(args.workflow_path):
            if file_path.endswith('.ga'):
                import_workflow(gi, os.path.join(args.workflow_path, file_path))
    else:
        import_workflow(gi, args.workflow_path)


if __name__ == '__main__':
    main()
