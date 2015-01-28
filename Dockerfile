# Galaxy - RNA workbench
#
# VERSION       0.1

FROM bgruening/galaxy-stable

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND Galaxy for RNA Research (de.NBI project)

WORKDIR /galaxy-central

RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name rnabob --panel-section-name RNATools"
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name trna_prediction --panel-section-name RNATools"
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name blockclust --panel-section-name RNATools"
RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o rnateam --name cofold --panel-section-name RNATools"
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name infernal --panel-section-name RNATools"
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o lionelguy --name rnammer --panel-section-name RNATools"
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name rnaz --panel-section-name RNATools"
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name suite_mirdeep_2_0 --panel-section-name RNATools"
RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o rnateam --name rnashapes --panel-section-name RNATools"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
