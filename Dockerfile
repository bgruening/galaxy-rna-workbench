# Galaxy - RNA workbench

FROM bgruening/galaxy-rna-seq:17.01

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

# Enable Conda dependency resolution
ENV GALAXY_CONFIG_CONDA_AUTO_INSTALL=True \
    GALAXY_CONFIG_CONDA_AUTO_INIT=True \
    GALAXY_CONFIG_USE_CACHED_DEPENDENCY_MANAGER=True \
    GALAXY_CONFIG_BRAND="RNA workbench"

# Install tools
ADD rna_workbench.yml $GALAXY_ROOT/tools.yaml
ADD rna_workbench_2.yml $GALAXY_ROOT/tools_2.yaml

RUN install-tools $GALAXY_ROOT/tools.yaml && \
    /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null && \
    rm /export/galaxy-central/ -rf
# Split into two layers, it seems that there is a max-layer size.
RUN install-tools $GALAXY_ROOT/tools_2.yaml && \
    /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null && \
    rm /export/galaxy-central/ -rf

ADD ./rna-workbench-tours/* $GALAXY_ROOT/config/plugins/tours/

# Data libraries
#ADD setup_data_libraries.py $GALAXY_ROOT/setup_data_libraries.py
ADD library_data.yaml $GALAXY_ROOT/library_data.yaml

ADD ./rna-workbench-workflow/Galaxy-Workflow-trimming_mapping-treatment_untreatment-SE_PE.ga $GALAXY_HOME/rnateam.workflow.trimming_mapping.ga
ADD ./rna-workbench-workflow/Galaxy-Workflow-Analyse_unaligned_ncRNAs.ga $GALAXY_HOME/rnateam.workflow.analyse_unaligned_ncrnas.ga
ADD ./rna-workbench-workflow/Galaxy-Workflow-PAR-CLIP_analysis.ga $GALAXY_HOME/rnateam.workflow.analyse_PAR-CLIP.ga
ADD ./rna-workbench-workflow/Galaxy-Workflow-AREsite2_CLIP_analysis.ga $GALAXY_HOME/rnateam.workflow.aresite2_CLIP.ga
ADD ./rna-workbench-workflow/Galaxy-Workflow-RNA_family_model_construction.ga $GALAXY_HOME/rnateam.workflow.RNA_family_model_construction.ga

ADD import_workflows.py $GALAXY_ROOT/import_workflows.py

# Download training data and populate the data library
RUN startup_lite && \
    sleep 100 && \
    python $GALAXY_ROOT/import_workflows.py --workflow_path /home/galaxy/ -g http://localhost:8080 -u $GALAXY_DEFAULT_ADMIN_USER -p $GALAXY_DEFAULT_ADMIN_PASSWORD

RUN startup_lite && \
    sleep 100 && \
    . $GALAXY_VIRTUAL_ENV/bin/activate && \
    python $GALAXY_ROOT/setup_data_libraries.py -i $GALAXY_ROOT/library_data.yaml

# Add visualisations
RUN curl -sL https://github.com/bgruening/galaxytools/archive/master.tar.gz > master.tar.gz && \
    tar -xf master.tar.gz galaxytools-master/visualisations && \
    cp -r galaxytools-master/visualisations/dotplot/ config/plugins/visualizations/ && \
    cp -r galaxytools-master/visualisations/dbgraph/ config/plugins/visualizations/ && \
    rm -rf master.tar.gz rm galaxytools-master

# Container Style
ADD assets/img/logo.png $GALAXY_CONFIG_DIR/web/welcome_image.png
ADD welcome.html $GALAXY_CONFIG_DIR/web/welcome.html
