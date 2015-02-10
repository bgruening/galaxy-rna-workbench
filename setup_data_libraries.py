import os
import time
import ConfigParser
from bioblend import galaxy
import subprocess
from subprocess import CalledProcessError

if __name__ == '__main__':
    
    print "-- importing data libraries --"

    # read from config
    config = ConfigParser.ConfigParser()
    config.read('setup_data_libraries.ini')

    url = config.get('main', 'galaxy_base_url')

    admin_email = config.get('admin', 'email')
    admin_pass = config.get('admin', 'password')
    print "config read"
    # establish connection to galaxy instance
    gi = galaxy.GalaxyInstance(url=url, email=admin_email, password=admin_pass)
    
    shed_tools_root = '/shed_tools'
    
    print "finding tools with test data"
    tests = {}
    for path,dirs,files in os.walk(shed_tools_root):
        first = os.path.basename(os.path.normpath(path))
        if first == 'test-data' and '.hg' not in path:
            second = os.path.dirname(path)
            tests[os.path.basename(second)] = path
    
    if tests:
        print "creating test data library"
        # create test data library
        testlib = gi.libraries.create_library('Test Data', 'Data pulled from tool test folders')
        
        for fname, fpath in tests.items():
            print "building",fname,"folder"
            if not 'msa' in fname:
                folder = gi.libraries.create_folder(testlib['id'], fname)
                files = '\n'.join(os.path.join(fpath, f) for f in os.listdir(fpath) if not 'result' in f)
                gi.libraries.upload_from_galaxy_filesystem(testlib['id'], files, folder_id=folder[0]['id'], link_data_only='link_to_files')
        
        # wait for uploads to complete
        print "uploading files",
        n = 1
        while n > 0:
            try:
                r = subprocess.check_output(["qstat"])
                n = len(r.split('\n'))
                time.sleep(3)
            except CalledProcessError as inst:
                if inst.returncode == 153: #queue is empty
                    n = 0
                else:
                    raise        
        
        time.sleep(10)
        print "-- finished importing test data --" 

