[![Build Status](https://travis-ci.org/bgruening/galaxy-rna-workbench.svg?branch=master)](https://travis-ci.org/bgruening/galaxy-rna-workbench)
[![Docker Repository on Quay](https://quay.io/repository/bgruening/galaxy-rna-workbench/status "Docker Repository on Quay")](https://quay.io/repository/bgruening/galaxy-rna-workbench)

RNA Galaxy Workbench
====================

The RNA analyses workbench is developed by the RNA Bioinformatics
Center (RBC). This center is one of the eight service units of the
[German Network for Bioinformatics Infrastructure](http://www.denbi.de), running the German [ELIXIR Node](https://www.elixir-europe.org/).

[<img src="assets/img/deNBI_logo.jpg" height="35px" alt="de.NBI"
valign="middle">](http://www.denbi.de)
[<img src="assets/img/elixir_germany.png" height="55px" alt="ELIXIR Germany"
valign="middle">](https://www.elixir-europe.org)

This webserver is based on the [Galaxy Docker](https://github.com/bgruening/docker-galaxy-stable) for advanced local deploymentes we recommend the upstream [documentation](http://bgruening.github.io/docker-galaxy-stable).

# Usage

The Galaxy RNA workbench is based on a dedicated Galaxy instance wrapped into a Docker container. It is based on the [Galaxy Docker Image](http://bgruening.github.io/docker-galaxy-stable/)

## Requirement

To use the Galaxy RNA workbench, you will need [Docker](https://www.docker.com/products/overview#h_installation).

Non-Linux users are encouraged to use [Kitematic](https://kitematic.com) for [OSX](https://github.com/bgruening/galaxy-rna-workbench/blob/master/howto_kitematic_osx.md) or [Windows](https://github.com/bgruening/galaxy-rna-workbench/blob/master/howto_kitematic_win.md), a graphical User-Interface for managing Docker containers.

Linux users and people familiar with the command line can follow the instruction on installing Docker from [Docker website](https://docs.docker.com/installation).

## Docker configuration

The RNA workbench docker container is rather large and expected to grow when further tools and workflows are contributed. So for users new to docker, we list here some tweaks that can help to work around issues when first using docker.
After successful installation of docker, it is recommended to configure some settings, dealing for example with the storage space required by containers. You can find more information [here](howtodocker.md).

## RNA workbench launch

Kitematic users can launch the RNA workbench directly from its interface, browsing all publicly available images from the Docker Hub.

The following video shows the launch of the RNA workbench from Kitematic:

[![Galaxy RNA workbench launch through Kitematic](https://i.imgur.com/qjQlRxJ.png)](https://www.youtube.com/watch?v=fYer4Xdw_h4 "Kitematic galaxy-rna-workbench launch")


For non-Kitematic users, starting the RNA workbench is analogous to start the generic Galaxy Docker image:

```
$ docker run -d -p 8080:80 bgruening/galaxy-rna-workbench
```

A detailed discussion of Docker's parameters is given in the [Docker manual](http://docs.docker.io/). It is really worth reading.

Nevertheless, here is a quick rundown:

- `docker run` starts the Image/Container

   In case the Container is not already stored locally, docker downloads it automatically

- The argument `-p 8080:80` makes the port 80 (inside of the container) available on port 8080 on your host

    Inside the container a Apache web server is running on port 80 and that port can be bound to a local port on your host computer.
    With this parameter you can access your Galaxy instance via `http://localhost:8080` immediately after executing the command above

- `bgruening/galaxy-rna-workbench` is the Image/Container name, that directs docker to the correct path in the [docker index](https://index.docker.io/u/bgruening/galaxy-rna-workbench/)
- `-d` will start the docker container in Daemon mode.

  For an interactive session, one executes:

  ```
  $ docker run -i -t -p 8080:80 bgruening/galaxy-rna-workbench /bin/bash
  ```

  and manually invokes the `startup` script to start PostgreSQL, Apache and Galaxy.

Docker images are "read-only". All changes during one session are lost after restart. This mode is useful to present Galaxy to your colleagues or to run workshops with it.

To install Tool Shed repositories or to save your data, you need to export the calculated data to the host computer. Fortunately, this is as easy as:

```
$ docker run -d -p 8080:80 -v /home/user/galaxy_storage/:/export/ bgruening/galaxy-rna-workbench
```

Given the additional `-v /home/user/galaxy_storage/:/export/` parameter, docker will mount the folder `/home/user/galaxy_storage` into the Container under `/export/`. A `startup.sh` script, that is usually starting Apache, PostgreSQL and Galaxy, will recognize the export directory with one of the following outcomes:

  - In case of an empty `/export/` directory, it will move the [PostgreSQL](http://www.postgresql.org/) database, the Galaxy database directory, Shed Tools and Tool Dependencies and various configure scripts to /export/ and symlink back to the original location.
  - In case of a non-empty `/export/`, for example if you continue a previous session within the same folder, nothing will be moved, but the symlinks will be created.

This enables you to have different export folders for different sessions - meaning real separation of your different projects.

It will start the Galaxy RNA workbench with the configuration and launch of a Galaxy instance and its population with the needed tools. The instance will be accessible at [http://localhost:8080](http://localhost:8080).

For a more specific configuration, you can have a look at the [documentation of the Galaxy Docker Image](http://bgruening.github.io/docker-galaxy-stable/).

## Users & Passwords

The Galaxy Admin User has the username `admin@galaxy.org` and the password `admin`.

The PostgreSQL username is `galaxy`, the password `galaxy` and the database name `galaxy`.
If you want to create new users, please make sure to use the `/export/` volume. Otherwise your user will be removed after your docker session is finished.

## Tours

The RNA workbench provides interactive tours that illustrate how the main interface works in relation to real-life user tasks.

These show many common operations, such as searching, parametrizing, and running tools, or saving a history of operations in a sharable workflow.

The following video demonstrates the main elements that compose the Galaxy user interface:

[![Galaxy RNA workbench UI tour](https://i.imgur.com/c06O3I0.png)](https://www.youtube.com/watch?v=rP59wYIxWcI "Kitematic galaxy-rna-workbench launch")

# Available Tools

| Category   | Tools | Description | Reference |
| -------- | ------- | ----------- | --------- |
| RNA Structure Analysis| [ViennaRNA](http://www.tbi.univie.ac.at/RNA/) | A tool compilation for prediction and comparison of RNA secondary structures | [Lorenz et al. 2011](http://dx.doi.org/10.1186/1748-7188-6-26) |
|                       | [Kinwalker](http://www.bioinf.uni-leipzig.de/Software/Kinwalker/) | Algorithm for cotranscriptional folding of RNAs to obtain the min. free energy structure | - |
|                       | [MEA](http://www.bioinf.uni-leipzig.de/Software/mea/) | Prediction of maximum expected accuracy RNA secondary structures | [Amman et al. 2013](http://link.springer.com/chapter/10.1007/978-3-319-02624-4_1) |
|                       | [RNAz](http://www.tbi.univie.ac.at/~wash/RNAz/) | Predicts structurally conserved and therm. stable RNA secondary structures in mult. seq. alignments | [Washietl et al. 2005](http://www.pnas.org/cgi/content/abstract/0409169102v1) |
|                       | [Cofold](http://www.e-rna.org/cofold/) | A thermodynamics-based RNA secondary structure folding algorithm | [Proctor and Meyer, 2015](https://academic.oup.com/nar/article-lookup/doi/10.1093/nar/gkt174) |
|                       | [RNAshapes](https://bibiserv2.cebitec.uni-bielefeld.de/rnashapes) | Structures to a tree-like domain of shapes, retaining adjacency and nesting of structural features | [Janssen and Giergerich, 2014](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btu649) |
|                       | [antaRNA](http://www.bioinf.uni-freiburg.de/Software/antaRNA/) | Possibility of inverse RNA structure folding and a specification of a GC value constraint | [Kleinkauf et al. 2015](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv319) |
|                       | [segmentation-fold](https://github.com/yhoogstrate/segmentation-fold)| An application that predicts RNA 2D-structure with an extended version of the Zuker algorithm | - |
| RNA Alignment | [Compalignp](http://www.biophys.uni-duesseldorf.de/bralibase/) | An RNA counterpart of the protein specific "Benchmark Alignment Database" | [Wilm et al. 2006](http://almob.biomedcentral.com/articles/10.1186/1748-7188-1-19) |
|               | [MAFFT](http://mafft.cbrc.jp/alignment/software/) | A multiple sequence alignment program for unix-like operating systems | [Katoh and Standley, 2016](https://academic.oup.com/bioinformatics/article/32/13/1933/1743504/A-simple-method-to-control-over-alignment-in-the) |
|               | [LocARNA](http://rna.informatik.uni-freiburg.de/LocARNA/Input.jsp) | A tool for multiple alignment of RNA molecules | [Will et al. 2012](http://rnajournal.cshlp.org/content/18/5/900) |
| RNA Annotation | [GotohScan](http://www.bioinf.uni-leipzig.de/Software/GotohScan/) | A search tool that finds shorter sequences in large database sequences | [Hertel, 2009](http://www.bioinf.uni-leipzig.de/Software/GotohScan/README) |
|                | [RNAcode](http://wash.github.io/rnacode/) | Predicts protein coding regions in a a set of homologous nucleotide sequences | [Washietl et al. 2011](http://rnajournal.cshlp.org/content/17/4/578.long) |
|                | [INFERNAL](http://eddylab.org/infernal/) | A tool searching DNA sequence databases for RNA structure and sequence similarities | [Nawrocki et al. 2015](https://academic.oup.com/nar/article/43/D1/D130/2437148/Rfam-12-0-updates-to-the-RNA-families-database) |
|                | [RNAmmer](http://www.cbs.dtu.dk/services/RNAmmer/) | Predicts 5s/8s, 16s/18s, and 23s/28s ribosomal RNA in full genome sequences | [Lagesen et al. 2007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1888812/) |
|                | [ARAGORN](http://mbio-serv2.mbioekol.lu.se/ARAGORN/) | A tool to identify tRNA and tmRNA genes | [Laslett and Canback, 2004](https://academic.oup.com/nar/article/32/1/11/1194008/ARAGORN-a-program-to-detect-tRNA-genes-and-tmRNA) |
|                | [tRNAscan](http://lowelab.ucsc.edu/tRNAscan-SE/) | Searches for tRNA genes in genomic sequences | [Lowe and Eddy, 1997](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC146525/) |
|                | [RNABOB](http://eddylab.org/software.html) | A tool for fast pattern searching for RNA secondary structures | - |
|                | [Fusion Matcher](https://github.com/yhoogstrate/fuma) | A tool that reports identical fusion genes based on gene-name annotations | [Hoogstrate et al. 2016](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btv721) |
| RNA-protein Interaction | [AREsite2](http://rna.tbi.univie.ac.at/AREsite2) | A database for AU-/GU-/U-rich elements in human and model organisms | [Fallmann et al. 2016](http://dx.doi.org/10.1093/nar/gkv1238) |
|                         | [DoRiNA](http://dorina.mdc-berlin.de/) | A database of RNA interactions in post-transcriptional regulation | [Blin et al. 2014](http://www.ncbi.nlm.nih.gov/pubmed/25416797) |
|                         | [Piranha](https://github.com/smithlabcode/piranha) | A peak-caller for CLIP- and RIP-seq data | - |
|                         | [RNAcommender](https://github.com/gianlucacorrado/RNAcommender) | A tool for genome-wide recommendation of RNA-protein interactions | [Corrado et al. 2016](https://doi.org/10.1093/bioinformatics/btw517) |
|                         | [PARalyzer](https://ohlerlab.mdc-berlin.de/software/PARalyzer_85/)| An algorithm to generate a map of interacting RNA-binding proteins and their targets | [Corcoran et al. 2011](http://dx.doi.org/10.1186/gb-2011-12-8-r79) |
| Ribosome Profiling | [RiboTaper](https://ohlerlab.mdc-berlin.de/software/RiboTaper_126/) | An analysis pipeline for Ribo-Seq experiments | [Calviello et al. 2016](http://www.nature.com/nmeth/journal/vaop/ncurrent/full/nmeth.3688.html) |
| RNA-Seq | [SortMeRNA](http://bioinfo.lifl.fr/RNA/sortmerna/) | A tool for filtering, mapping and OTU-picking NGS reads in metatranscriptomic and -genomic data | [Kopylov et al. 2011](https://dx.doi.org/10.1093/bioinformatics/bts611) |
|         | [BlockClust](http://www.bioinf.uni-freiburg.de/Software/) | Non-coding RNA clustering from deep sequencing read profiles | - |
|         | [MiRDeep2](https://www.mdc-berlin.de/8551903/en/) | Discovers microRNA genes by analyzing sequenced RNAs | [Friedlaender et al. 2008](https://dx.doi.org/10.1038/nbt1394) |
|         | [FlaiMapper](https://github.com/yhoogstrate/flaimapper) | A tool for computational annotation of small ncRNA-derived fragments using RNA-seq data | [Hoogstrate et al. 2015](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btu696) |
|         | [PIPmiR](https://ohlerlab.mdc-berlin.de/software/Pipeline_for_the_Identification_of_Plant_miRNAs_84/) | An algorithm to identify novel plant miRNA genes from a combination of deep sequencing data and genomic features | [Breakfield et al. 2011](https://dx.doi.org/10.1101/gr.123547.111)|
|         | [NASTIseq](https://ohlerlab.mdc-berlin.de/software/NASTIseq_104/)| A method that incorporates the inherent variable efficiency of generating perfectly strand-specific libraries | [Song et al. 2013](http://genome.cshlp.org/content/23/10/1730.long) |
| RNA Target Prediction | [TargetFinder](https://github.com/carringtonlab/TargetFinder) | A tool to predict small RNA binding sites on target transcripts from a sequence database | - |

# Contributors

 - Andrea Bagnacani
 - Bérénice Batut
 - Joerg Fallmann
 - Bjoern Gruening
 - Torsten Houwaart
 - Cameron Smith
 - Sebastian Will
 - Markus Wolfien
 - Dilmurat Yusuf
 - Youri Hoogstrate


# Support & Bug Reports

For support, questions, or feature requests fill bug reports at https://github.com/bgruening/galaxy-rna-workbench/issues.

# License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
