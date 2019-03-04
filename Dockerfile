# Galaxy - RNA workbench

FROM bgruening/galaxy-rna-structural-analysis:19.01

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND="RNA workbench"

# Install tools
ADD rna_workbench.yml $GALAXY_ROOT/tools.yaml
ADD rna_workbench_2.yml $GALAXY_ROOT/tools_2.yaml

RUN install-tools $GALAXY_ROOT/tools.yaml && \
    /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null && \
    rm /export/galaxy-central/ -rf

# Split into multiple layers, it seems that there is a max-layer size.
RUN install-tools $GALAXY_ROOT/tools_2.yaml && \
    /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null && \
    rm /export/galaxy-central/ -rf && \
    mkdir -p $GALAXY_HOME/workflows

# Add Galaxy interactive tours
ADD ./rna-workbench-tours/* $GALAXY_ROOT/config/plugins/tours/

# Add data library definition file
ADD library_data.yaml $GALAXY_ROOT/library_data.yaml

# Add workflows to the Docker image
ADD ./rna-workbench-workflow/* $GALAXY_HOME/workflows/

ENV GALAXY_CONFIG_TOOL_PATH=/galaxy-central/tools/

# Download training data and populate the data library
#RUN startup_lite && \
#    galaxy-wait && \
    #workflow-install --workflow_path $GALAXY_HOME/workflows/ -g http://localhost:8080 -u $GALAXY_DEFAULT_ADMIN_USER -p $GALAXY_DEFAULT_ADMIN_PASSWORD && \
    #setup-data-libraries -i $GALAXY_ROOT/library_data.yaml -g http://localhost:8080 -u $GALAXY_DEFAULT_ADMIN_USER -p $GALAXY_DEFAULT_ADMIN_PASSWORD

# Add visualisations
RUN curl -sL https://github.com/bgruening/galaxytools/archive/master.tar.gz > master.tar.gz && \
    tar -xf master.tar.gz galaxytools-master/visualisations && \
    cp -r galaxytools-master/visualisations/dotplot/ config/plugins/visualizations/ && \
    cp -r galaxytools-master/visualisations/dbgraph/ config/plugins/visualizations/ && \
    rm -rf master.tar.gz rm galaxytools-master

# Container Style
ADD assets/img/full_logo.png $GALAXY_CONFIG_DIR/web/welcome_image.png
ADD welcome.html $GALAXY_CONFIG_DIR/web/welcome.html
