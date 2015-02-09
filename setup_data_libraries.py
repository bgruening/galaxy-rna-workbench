import os
import ConfigParser
from bioblend import galaxy

if __name__ == '__main__':
    
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
            third = os.path.dirname(second)
            tests['%s-%s' % (os.path.basename(second),os.path.basename(third))] = path
    
    if tests:
        print "creating test data library"
        # create test data library
        testlib = gi.libraries.create_library('Test Data', 'Data pulled from tool test folders')
        
        for fname, fpath in tests.items():
            print "building",fname,"folder"
            folder = gi.libraries.create_folder(testlib['id'], fname)
            files = '\n'.join(os.path.join(fpath, f) for f in os.listdir(fpath))
            gi.libraries.upload_from_galaxy_filesystem(testlib['id'], files, folder_id=folder[0]['id'], link_data_only='link_to_files')
        
        print "-- finished importing test data --" 

