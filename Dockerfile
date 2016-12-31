# Galaxy - RNA workbench

FROM bgruening/galaxy-rna-seq:16.10

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

# Enable Conda dependency resolution
ENV GALAXY_CONFIG_CONDA_AUTO_INSTALL=True \
    GALAXY_CONFIG_CONDA_AUTO_INIT=True \
    GALAXY_CONFIG_USE_CACHED_DEPENDENCY_MANAGER=True \
    GALAXY_CONFIG_BRAND="RNA workbench"

# Install tools
ADD rna_workbench.yml $GALAXY_ROOT/tools.yaml
RUN install-tools $GALAXY_ROOT/tools.yaml && \
    /tool_deps/_conda/bin/conda clean --tarballs

ADD ./rna-workbench-tours/viennarna_tour.yaml $GALAXY_ROOT/config/plugins/tours/rnateam.viennarna.yaml
ADD ./rna-workbench-tours/rnaseq-tour.yaml $GALAXY_ROOT/config/plugins/tours/rnateam.rnaseq.yaml

# Data libraries
ADD setup_data_libraries.py $GALAXY_ROOT/setup_data_libraries.py
ADD library_data.yaml $GALAXY_ROOT/library_data.yaml

ADD ./rna-workbench-workflow/Galaxy-Workflow-trimming_mapping-treatment_untreatment-SE_PE.ga $GALAXY_HOME/rnateam.workflow.trimming_mapping.ga
ADD import_workflows.py $GALAXY_ROOT/import_workflows.py

# Download training data and populate the data library
RUN startup_lite && \
    sleep 30 && \
    . $GALAXY_VIRTUAL_ENV/bin/activate && \
    python $GALAXY_ROOT/setup_data_libraries.py -i $GALAXY_ROOT/library_data.yaml && \
    python $GALAXY_ROOT/import_workflows.py

# Add visualisations
RUN curl -sL https://github.com/bgruening/galaxytools/archive/master.tar.gz > master.tar.gz && \
    tar -xf master.tar.gz galaxytools-master/visualisations && \
    cp -r galaxytools-master/visualisations/dotplot/ config/plugins/visualizations/ && \
    cp -r galaxytools-master/visualisations/dbgraph/ config/plugins/visualizations/ && \
    rm -rf master.tar.gz rm galaxytools-master

# Container Style
ADD assets/img/logo.png $GALAXY_CONFIG_DIR/web/welcome_image.png
ADD welcome.html $GALAXY_CONFIG_DIR/web/welcome.html
