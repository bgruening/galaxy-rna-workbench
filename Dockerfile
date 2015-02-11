# Galaxy - RNA workbench
#
# VERSION       0.1

FROM bgruening/galaxy-stable:dev

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND RNA workbench

WORKDIR /galaxy-central

# TODO: rnashapes is currently not in the ToolShed install it via PPA
RUN apt-get -qq update && apt-get install --no-install-recommends -y apt-transport-https software-properties-common && \
    apt-add-repository -y ppa:bibi-help/bibitools && \
    apt-get -qq update && \
    apt-get install --no-install-recommends -y rnashapes && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    . /home/galaxy/venv/bin/activate && pip install bioblend

RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name rnabob --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name text_processing --panel-section-id textutil" \
    '--url https://toolshed.g2.bx.psu.edu/ -o iuc --name bedtools --panel-section-name BED-Tools' \
    "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name emboss_5 --panel-section-name EMBOSS" \
    '--url https://toolshed.g2.bx.psu.edu/ -o iuc --name package_perl_pdf_api2_2_023' \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name trna_prediction --panel-section-name RNATools"

RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name blockclust --panel-section-name RNATools" \
    "--url https://testtoolshed.g2.bx.psu.edu/ -o rnateam --name cofold --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name infernal --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o lionelguy --name rnammer --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name rnaz --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o iuc --name package_vienna_rna_1_8" \
    "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name package_bowtie_0_12_7" \
    "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name vienna_rna --panel-section-name RNATools"

RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o iuc --name package_squid_1_9g " \
    "--url https://toolshed.g2.bx.psu.edu/ -o iuc --name package_randfold_2_0 " \
    "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name mirdeep2_mapper --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name mirdeep2_quantifier --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name mirdeep2 --panel-section-name RNATools" \
    "--url https://testtoolshed.g2.bx.psu.edu/ -o rnateam --name rnashapes --panel-section-name RNATools"

RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name suite_mirdeep_2_0"

RUN curl -sL https://github.com/bgruening/galaxytools/archive/master.tar.gz | tar xz && cp -r galaxytools-master/visualisations/* config/plugins/visualizations/ && rm -rf ./galaxytools-master

# data managers supporting fetch and index of genomes
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name data_manager_fetch_genome_all_fasta" \
    "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name data_manager_bwa_index_builder" \
    "--url https://testtoolshed.g2.bx.psu.edu/ -o rnateam --name data_manager_bowtie"

# modified supervisor conf file
ADD galaxy_build.conf /etc/galaxy/

# starts a galaxy instance for build process
ADD start_galaxy_for_build /usr/bin/
RUN chmod +x /usr/bin/start_galaxy_for_build

# specifies files to include as data libraries
ADD setup_data_libraries.py /galaxy-central/

# download and index genomes
ADD fetch_and_index_genomes.ini /galaxy-central/
ADD fetch_and_index_genomes.py /galaxy-central/

# necessary for galaxy server path upload - possible security problems ?? environment var for this ??
RUN sed -i 's|#allow_library_path_paste = False|allow_library_path_paste = True|' /etc/galaxy/galaxy.ini

ENV GALAXY_CONFIG_JOB_WORKING_DIRECTORY=/galaxy-central/database/job_working_directory \
    GALAXY_CONFIG_FILE_PATH=/galaxy-central/database/files \
    GALAXY_CONFIG_NEW_FILE_PATH=/galaxy-central/database/files \
    GALAXY_CONFIG_TEMPLATE_CACHE_PATH=/galaxy-central/database/compiled_templates \
    GALAXY_CONFIG_CITATION_CACHE_DATA_DIR=/galaxy-central/database/citations/data \
    GALAXY_CONFIG_CLUSTER_FILES_DIRECTORY=/galaxy-central/database/pbs \
    GALAXY_CONFIG_FTP_UPLOAD_DIR=/galaxy-central/database/ftp \
    GALAXY_CONFIG_INTEGRATED_TOOL_PANEL_CONFIG=/galaxy-central/integrated_tool_panel.xml \
    GALAXY_CONFIG_ALLOW_LIBRARY_PATH_PASTE=True

ADD build_job_conf.xml /etc/galaxy/
ENV GALAXY_CONFIG_JOB_CONFIG_FILE /etc/galaxy/build_job_conf.xml

RUN start_galaxy_for_build && . $GALAXY_VIRTUALENV/bin/activate && python -u setup_data_libraries.py --verbose && supervisorctl stop all

RUN start_galaxy_for_build && . $GALAXY_VIRTUALENV/bin/activate \
    && python -u fetch_and_index_genomes.py --config fetch_and_index_genomes.ini && supervisorctl stop all

ENV GALAXY_CONFIG_JOB_CONFIG_FILE $GALAXY_CONFIG_DIR/job_conf.xml

ENV GALAXY_CONFIG_JOB_WORKING_DIRECTORY=/export/galaxy-central/database/job_working_directory \
    GALAXY_CONFIG_FILE_PATH=/export/galaxy-central/database/files \
    GALAXY_CONFIG_NEW_FILE_PATH=/export/galaxy-central/database/files \
    GALAXY_CONFIG_TEMPLATE_CACHE_PATH=/export/galaxy-central/database/compiled_templates \
    GALAXY_CONFIG_CITATION_CACHE_DATA_DIR=/export/galaxy-central/database/citations/data \
    GALAXY_CONFIG_CLUSTER_FILES_DIRECTORY=/export/galaxy-central/database/pbs \
    GALAXY_CONFIG_FTP_UPLOAD_DIR=/export/galaxy-central/database/ftp \
    GALAXY_CONFIG_INTEGRATED_TOOL_PANEL_CONFIG=/export/galaxy-central/integrated_tool_panel.xml

# Volumes and CMD are defined by the parent container
#VOLUME ["/export/", "/data/", "/var/lib/docker"]
#CMD ["/usr/bin/startup"]
