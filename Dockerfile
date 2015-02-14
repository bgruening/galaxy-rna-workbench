# Galaxy - RNA workbench
#
# VERSION       0.1

FROM bgruening/galaxy-rna-workbench-animalia

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND RNA workbench

RUN curl -sL https://github.com/bgruening/galaxytools/archive/master.tar.gz | tar xz && cp -r galaxytools-master/visualisations/* config/plugins/visualizations/ && rm -rf ./galaxytools-master
