# Galaxy - RNA workbench

FROM bgruening/rna-workbench-build-01

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

# Install tools
ADD rna_workbench_2.yml $GALAXY_ROOT/tools_2.yaml

RUN install-tools $GALAXY_ROOT/tools_2.yaml && \
    /tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null && \
    rm /export/galaxy-central/ -rf
