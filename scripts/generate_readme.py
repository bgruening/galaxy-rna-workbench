#!/usr/bin/env python

import yaml

def get_file_contents(filename):
    with file(filename) as f:
        s = f.read().strip()
    return s

def get_available_tools(tool_yaml_files):
    """
    Info needed:
    | Category   | Tools | Description | Reference |
    | RNA Structure Analysis | [tool-name](repo-url) | small description  | [Name et al. 2000](http://dx.doi.org/[doi]) |
    """
    tool_idx = {}
    for tool_yaml_file in tool_yaml_files:
        content = yaml.load(get_file_contents(tool_yaml_file))
        for topic in content:
            if topic.lower() == 'tools':
                for tool in content[topic]:
                    if 'tool_panel_section_label' in tool:
                        category = tool['tool_panel_section_label']
                    else:
                        category = ''
                    
                    if category not in tool_idx:
                        tool_idx[category] = {}
                    
                    if 'reference' not in tool['summary']:
                        tool['summary']['reference'] = '-'
                    
                    if tool['name'] in tool_idx[category]:
                        print "Warning: duplicate entry of tool: "+tool['name']
                    else:
                        tool_idx[category][tool['name']] = tool['summary']
    
    out_str = "| Category   | Tools | Description | Reference |\n| -------- | ------- | ----------- | --------- |"
    for category in sorted(tool_idx.keys()):
        for tool_id in sorted(tool_idx[category].keys()):
            summary =  tool_idx[category][tool_id]
            out_str += '| '+category + ' | [' + summary['full-name']+']('+summary['url']+') | '+summary['description'].replace('|','')+' | '+summary['reference']+" |\n"
    
    return out_str

fh = open('README.md.new', 'w')

# Header + Usage
fh.write(get_file_contents('docs/header.md') + "\n\n")

# Users & Passwords
fh.write(get_file_contents('docs/users_passwords.md') + "\n\n")

# Tours
fh.write(get_file_contents('docs/tours.md') + "\n\n")

# Available tools
#Both are used and this one: https://github.com/bgruening/docker-galaxy-ngs-preprocessing/blob/master/ngs_preprocessing.yml
#and this one: https://github.com/bgruening/galaxy-rna-seq/blob/master/rna_seq_tools.yml
fh.write(get_available_tools(['rna_workbench_2.yml']) + "\n\n")

fh.close()

