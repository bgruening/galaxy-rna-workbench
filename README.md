[![Build Status](https://travis-ci.org/bgruening/galaxy-rna-workbench.svg?branch=master)](https://travis-ci.org/bgruening/galaxy-rna-workbench)
[![Docker Repository on Quay](https://quay.io/repository/bgruening/galaxy-rna-workbench/status "Docker Repository on Quay")](https://quay.io/repository/bgruening/galaxy-rna-workbench)

<div id="top"></div>

RNA Galaxy Workbench
====================

The RNA Galaxy workbench is a comprehensive set of analysis tools and consolidated workflows. The workbench is based on the Galaxy framework, which guarantees simple access, easy extension, flexible adaption to personal and security needs, and sophisticated analyses independent of command-line knowledge.

The current implementation comprises more than 50 bioinformatics tools dedicated to different research areas of RNA biology, including RNA structure analysis, RNA alignment, RNA annotation, RNA-protein interaction, ribosome profiling, RNA-Seq analysis, and RNA target prediction.

The workbench is developed by the RNA Bioinformatics Center (RBC). This center is one of the eight service units of the [German Network for Bioinformatics Infrastructure](http://www.denbi.de), running the German [ELIXIR Node](https://www.elixir-europe.org/).

[<img align="left" src="assets/img/deNBI_logo.jpg" height="35px" alt="de.NBI" valign="middle">](http://www.denbi.de)
[<img align="center" src="assets/img/elixir_germany.png" height="55px" alt="ELIXIR Germany" valign="middle">](https://www.elixir-europe.org)

- [Usage](#usage)
  - [Requirement](#requirement)
  - [Docker configuration](#docker-configuration)
  - [RNA workbench launch](#rna-workbench-launch)
  - [Users and passwords](#users-and-passwords)
  - [Tours](#tours)
- [Available tools](#available-tools)
  - [RNA structure prediction and analysis](#rna-structure-prediction-and-analysis)
  - [RNA alignment](#rna-alignment)
  - [RNA annotation](#rna-annotation)
  - [RNA-protein interaction](#rna-protein-interaction)
  - [RNA target prediction](#rna-target-prediction)
  - [RNA Seq and HTS analysis](#rna-seq-and-hts-analysis)
  - [Ribosome profiling](#ribosome-profiling)
- [Training](#training)
- [Contributors](#contributors)
- [How to contribute](#how-to-contribute)
- [Support and bug reports](#support-and-bug-reports)
- [MIT license](#mit-license)

# Usage

The RNA analyses workbench implements a webserver based on the [Galaxy Docker](https://github.com/bgruening/docker-galaxy-stable) platform: a dedicated Galaxy instance wrapped in a Docker container. For advanced local deployments, we recommend to check out the upstream [documentation](http://bgruening.github.io/docker-galaxy-stable).
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## Requirement

To use the Galaxy RNA workbench, you only need [Docker](https://www.docker.com/products/overview#h_installation), which can be installed in different ways, depending on the type of system you're running:
- non-linux users are encouraged to use [Kitematic](https://kitematic.com), which provides a Docker installation for [OSX](https://github.com/bgruening/galaxy-rna-workbench/blob/master/howto_kitematic_osx.md) or [Windows](https://github.com/bgruening/galaxy-rna-workbench/blob/master/howto_kitematic_win.md), coupled with a user friendly interface to run Docker containers;
- linux users and people familiar with the command line can follow the instruction on installing Docker from its [website](https://docs.docker.com/installation).
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## Docker configuration

The RNA workbench docker container is rather large and expected to grow when further tools and workflows are contributed. So for users new to docker, we list here some tweaks that can help to work around issues when first using docker.
After successful installation of docker, it is recommended to configure some settings, dealing for example with the storage space required by containers. You can find more information [here](howtodocker.md).
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## RNA workbench launch

Whether you run Docker images using Kitematic or the command line interface, the procedure to launch the RNA workbench varies:

- Kitematic users can launch the RNA workbench directly from its interface. The following video shows how to load the docker container that is necessary to use the workbench:

  [![Galaxy RNA workbench launch through Kitematic](https://i.imgur.com/qjQlRxJ.png)](https://www.youtube.com/watch?v=fYer4Xdw_h4 "Kitematic galaxy-rna-workbench launch")


- For non-Kitematic users, starting the RNA workbench is analogous to start the generic Galaxy Docker image:

  ```
  $ docker run -d -p 8080:80 quay.io/bgruening/galaxy-rna-workbench
  ```

  A detailed discussion of Docker's parameters is given in the [Docker manual](http://docs.docker.io/). It is really worth reading. Nevertheless, here is a quick rundown:

  - `docker run` starts the Image/Container

     In case the Container is not already stored locally, docker downloads it automatically

  - The argument `-p 8080:80` makes the port 80 (inside of the container) available on port 8080 on your host

      Inside the container a Apache web server is running on port 80 and that port can be bound to a local port on your host computer.
      With this parameter you can access your Galaxy instance via `http://localhost:8080` immediately after executing the command above

  - `quay.io/bgruening/galaxy-rna-workbench` is the Image/Container name, that directs docker to the correct path in the [docker index](https://quay.io/repository/bgruening/galaxy-rna-workbench)
  - `-d` will start the docker container in Daemon mode.

    For an interactive session, one executes:

    ```
    $ docker run -i -t -p 8080:80 quay.io/bgruening/galaxy-rna-workbench /bin/bash
    ```

    and manually invokes the `startup` script to start PostgreSQL, Apache and Galaxy.

  Docker images are "read-only". All changes during one session are lost after restart. This mode is useful to present Galaxy to your colleagues or to run workshops with it.

  To install Tool Shed repositories or to save your data, you need to export the calculated data to the host computer. Fortunately, this is as easy as:

  ```
  $ docker run -d -p 8080:80 -v /home/user/galaxy_storage/:/export/ quay.io/bgruening/galaxy-rna-workbench
  ```

  Given the additional `-v /home/user/galaxy_storage/:/export/` parameter, docker will mount the folder `/home/user/galaxy_storage` into the Container under `/export/`. A `startup.sh` script, that is usually starting Apache, PostgreSQL and Galaxy, will recognize the export directory with one of the following outcomes:

    - In case of an empty `/export/` directory, it will move the [PostgreSQL](http://www.postgresql.org/) database, the Galaxy database directory, Shed Tools and Tool Dependencies and various configure scripts to /export/ and symlink back to the original location.
    - In case of a non-empty `/export/`, for example if you continue a previous session within the same folder, nothing will be moved, but the symlinks will be created.

  This enables you to have different export folders for different sessions - meaning real separation of your different projects.

  It will start the Galaxy RNA workbench with the configuration and launch of a Galaxy instance and its population with the needed tools. The instance will be accessible at [http://localhost:8080](http://localhost:8080).

  For a more specific configuration, you can have a look at the [documentation of the Galaxy Docker Image](http://bgruening.github.io/docker-galaxy-stable/).
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## Users and passwords

The Galaxy Admin User has the username `admin@galaxy.org` and the password `admin`.
In order to use certain features of Galaxy, like e.g. the RNA structure visualization, one has to be logged in.
Also the installation of additional tools requires a login.

The PostgreSQL username is `galaxy`, the password `galaxy` and the database name `galaxy`.

If you want to create new users, please make sure to use the `/export/` volume. Otherwise your user will be removed after your docker session is finished.
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## Tours

The RNA workbench provides the possibility to run interactive tours that illustrate how the main interface works in relation to real-life user tasks. These show many common operations, such as searching, parametrizing, and running tools, or saving a history of operations in a sharable workflow.

The following video demonstrates the main elements that compose the Galaxy user interface:

[![Galaxy RNA workbench UI tour](https://i.imgur.com/c06O3I0.png)](https://www.youtube.com/watch?v=rP59wYIxWcI "Kitematic galaxy-rna-workbench launch")
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

# Available tools

In this section we list all tools that have been integrated in the RNA workbench. The list is likely to grow as soon as further tools and workflows are contributed. To ease readability, we divided them into categories.
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## RNA structure prediction and analysis

Tool | Description | Reference
---- | ----------- | ---------
[antaRNA](http://www.bioinf.uni-freiburg.de/Software/antaRNA/) | Possibility of inverse RNA structure folding and a specification of a GC value constraint | [Kleinkauf et al. 2015](https://doi.org/10.1093/bioinformatics/btv319)
[CoFold](http://www.e-rna.org/cofold/) | A thermodynamics-based RNA secondary structure folding algorithm | [Proctor and Meyer, 2015](https://doi.org/10.1093/nar/gkt174)
[Kinwalker](http://www.bioinf.uni-leipzig.de/Software/Kinwalker/) | Algorithm for cotranscriptional folding of RNAs to obtain the min. free energy structure | [Geis et al. 2008](https://dx.doi.org/10.1016/j.jmb.2008.02.064)
[MEA](http://www.bioinf.uni-leipzig.de/Software/mea/) | Prediction of maximum expected accuracy RNA secondary structures | [Amman et al. 2013](https://dx.doi.org/10.1007/978-3-319-02624-4_1)
[RNAshapes](https://bibiserv2.cebitec.uni-bielefeld.de/rnashapes) | Structures to a tree-like domain of shapes, retaining adjacency and nesting of structural features | [Janssen and Giergerich, 2014](https://doi.org/10.1093/bioinformatics/btu649)
[RNAz](http://www.tbi.univie.ac.at/~wash/RNAz/) | Predicts structurally conserved and therm. stable RNA secondary structures in mult. seq. alignments | [Washietl et al. 2005](https://dx.doi.org/10.1073/pnas.0409169102)
[segmentation-fold](https://github.com/yhoogstrate/segmentation-fold)| An application that predicts RNA 2D-structure with an extended version of the Zuker algorithm | -
[ViennaRNA](http://www.tbi.univie.ac.at/RNA/) | A tool compilation for prediction and comparison of RNA secondary structures | [Lorenz et al. 2011](https://dx.doi.org/10.1186/1748-7188-6-26)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## RNA alignment

Tool | Description | Reference
---- | ----------- | ---------
[Compalignp](http://www.biophys.uni-duesseldorf.de/bralibase/) | An RNA counterpart of the protein specific "Benchmark Alignment Database" | [Wilm et al. 2006](https://dx.doi.org/10.1186/1748-7188-1-19)
[LocARNA](http://rna.informatik.uni-freiburg.de/LocARNA/Input.jsp) | A tool for multiple alignment of RNA molecules | [Will et al. 2012](https://dx.doi.org/10.1261/rna.029041.111)
[MAFFT](http://mafft.cbrc.jp/alignment/software/) | A multiple sequence alignment program for unix-like operating systems | [Katoh and Standley, 2016](https://doi.org/10.1093/bioinformatics/btw108)
[RNAlien](http://rna.tbi.univie.ac.at/rnalien/) | A tool for RNA family model construction | [Eggenhofer et al. 2016](https://doi.org/10.1093/nar/gkw558)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## RNA annotation

Tool | Description | Reference
---- | ----------- | ---------
[ARAGORN](http://mbio-serv2.mbioekol.lu.se/ARAGORN/) | A tool to identify tRNA and tmRNA genes | [Laslett and Canback, 2004](https://doi.org/10.1093/nar/gkh152)
[Fusion Matcher (FuMa)](https://github.com/yhoogstrate/fuma) | A tool that reports identical fusion genes based on gene-name annotations | [Hoogstrate et al. 2016](https://doi.org/10.1093/bioinformatics/btv721)
[GotohScan](http://www.bioinf.uni-leipzig.de/Software/GotohScan/) | A search tool that finds shorter sequences in large database sequences | [Hertel et al. 2009](https://doi.org/10.1093/nar/gkn1084)
[INFERNAL](http://eddylab.org/infernal/) | A tool searching DNA sequence databases for RNA structure and sequence similarities | [Nawrocki et al. 2015](https://doi.org/10.1093/nar/gku1063)
[RNABOB](http://eddylab.org/software.html) | A tool for fast pattern searching for RNA secondary structures | -
[RNAcode](http://wash.github.io/rnacode/) | Predicts protein coding regions in a a set of homologous nucleotide sequences | [Washietl et al. 2011](https://dx.doi.org/10.1261/rna.2536111)
[RNAmmer](http://www.cbs.dtu.dk/services/RNAmmer/) | Predicts 5s/8s, 16s/18s, and 23s/28s ribosomal RNA in full genome sequences | [Lagesen et al. 2007](https://dx.doi.org/10.1093/nar/gkm160)
[tRNAscan](http://lowelab.ucsc.edu/tRNAscan-SE/) | Searches for tRNA genes in genomic sequences | [Lowe and Eddy, 1997](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC146525/)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## RNA-protein interaction

Tool | Description | Reference
---- | ----------- | ---------
[AREsite2](http://rna.tbi.univie.ac.at/AREsite2) | A database for AU-/GU-/U-rich elements in human and model organisms | [Fallmann et al. 2016](https://dx.doi.org/10.1093/nar/gkv1238)
[DoRiNA](http://dorina.mdc-berlin.de/) | A database of RNA interactions in post-transcriptional regulation | [Blin et al. 2014](https://dx.doi.org/10.1093/nar/gku1180)
[PARalyzer](https://ohlerlab.mdc-berlin.de/software/PARalyzer_85/)| An algorithm to generate a map of interacting RNA-binding proteins and their targets | [Corcoran et al. 2011](https://dx.doi.org/10.1186/gb-2011-12-8-r79)
[Piranha](https://github.com/smithlabcode/piranha) | A peak-caller for CLIP- and RIP-seq data | -
[RNAcommender](https://github.com/gianlucacorrado/RNAcommender) | A tool for genome-wide recommendation of RNA-protein interactions | [Corrado et al. 2016](https://doi.org/10.1093/bioinformatics/btw517)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## RNA target prediction

Tool | Description | Reference
---- | ----------- | ---------
[TargetFinder](https://github.com/carringtonlab/TargetFinder) | A tool to predict small RNA binding sites on target transcripts from a sequence database | -
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## RNA Seq and HTS analysis

### Preprocessing

Tool | Description | Reference
---- | ----------- | ---------
[FastQC!](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/) | A quality control tool for high throughput sequence data | -
[Trim Galore!](https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/) | Automatic quality and adapter trimming as well as quality control | -
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

### RNA-Seq

Tool | Description | Reference
---- | ----------- | ---------
[BlockClust](https://toolshed.g2.bx.psu.edu/view/rnateam/blockclust/) | Small non-coding RNA clustering from deep sequencing read profiles | [Videm et al. 2014](https://doi.org/10.1093/bioinformatics/btu270)
[FlaiMapper](https://github.com/yhoogstrate/flaimapper) | A tool for computational annotation of small ncRNA-derived fragments using RNA-seq data | [Hoogstrate et al. 2015](https://doi.org/10.1093/bioinformatics/btu696)
[MiRDeep2](https://www.mdc-berlin.de/8551903/en/) | Discovers microRNA genes by analyzing sequenced RNAs | [Friedländer et al. 2008](https://dx.doi.org/10.1038/nbt1394)
[NASTIseq](https://ohlerlab.mdc-berlin.de/software/NASTIseq_104/)| A method that incorporates the inherent variable efficiency of generating perfectly strand-specific libraries | [Li et al. 2013](https://dx.doi.org/10.1101/gr.149310.112)
[PIPmiR](https://ohlerlab.mdc-berlin.de/software/Pipeline_for_the_Identification_of_Plant_miRNAs_84/) | An algorithm to identify novel plant miRNA genes from a combination of deep sequencing data and genomic features | [Breakfield et al. 2011](https://dx.doi.org/10.1101/gr.123547.111)
[SortMeRNA](http://bioinfo.lifl.fr/RNA/sortmerna/) | A tool for filtering, mapping and OTU-picking NGS reads in metatranscriptomic and -genomic data | [Kopylova et al. 2011](https://dx.doi.org/10.1093/bioinformatics/bts611)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

### Read Mapping

Tool | Description | Reference
---- | ----------- | ---------
[HISAT2](https://ccb.jhu.edu/software/hisat2/) | Hierarchical indexing for spliced alignment of transcripts | [Pertea et al. 2016](https://dx.doi.org/10.1038/nprot.2016.095)
[TopHat2](https://ccb.jhu.edu/software/tophat/) | Spliced aligner for RNA-seq experiments | [Kim et al. 2013](https://dx.doi.org/10.1038%2Fnprot.2013.084)
[Bowtie 2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml) | Fast and sensitive read alignment | [Langmead et al. 2012](https://dx.doi.org/10.1038/nmeth.1923) 
[BWA](http://bio-bwa.sourceforge.net/) | Software package for mapping low-divergent sequences against a large reference genome | [Li and Durbin 2009](https://dx.doi.org/10.1093/bioinformatics/btp324), [Li and Durbin 2010](https://dx.doi.org/10.1093/bioinformatics/btp698)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

### Transcript Assembly

Tool | Description | Reference
---- | ----------- | ---------
[Cufflinks tool suite](http://cole-trapnell-lab.github.io/cufflinks/) | Transcriptome assembly and differential expression analysis for RNA-Seq | [Trapnell et al. 2012](https://dx.doi.org/10.1038/nprot.2012.016), [Trapnell et al. 2013](https://dx.doi.org/10.1038/nbt.2450)
[Trinity](https://github.com/trinityrnaseq/trinityrnaseq/wiki) | De novo transcript sequence reconstruction from RNA-Seq | [Haas et al. 2013](https://dx.doi.org/10.1038%2Fnprot.2013.084)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

### Quantification

Tool | Description | Reference
---- | ----------- | ---------
[featureCounts](http://bioinf.wehi.edu.au/featureCounts/) | a ultrafast and accurate read summarization program | [Liao et al. 2014](http://dx.doi.org/10.1093/bioinformatics/btt656)
[htseq-count](http://www-huber.embl.de/HTSeq/doc/count.html) | Tool for counting reads in features | [Anders et al. 2015](https://dx.doi.org/10.1093%2Fbioinformatics%2Fbtu638)
[Sailfish](http://www.cs.cmu.edu/~ckingsf/software/sailfish/) | Rapid Alignment-free Quantification of Isoform Abundance | [Patro et al. 2014](http://dx.doi.org/10.1038/nbt.2862)
[Salmon](https://combine-lab.github.io/salmon/) | Fast, accurate and bias-aware transcript quantification | [Patro et al. 2017](http://dx.doi.org/10.1038/nmeth.4197)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

### Differential expression analysis

Tool | Description | Reference
---- | ----------- | ---------
[DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html) | Differential gene expression analysis based on the negative binomial distribution | [Love et al. 2014](http://doi.org/10.1186/s13059-014-0550-8)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

### Utilities

Tool | Description | Reference
---- | ----------- | ---------
[SAMtools](http://samtools.sourceforge.net/) | Utilities for manipulating alignments in the SAM format | [Heng et al. 2009](https://doi.org/10.1093/bioinformatics/btp352)
[BEDTools](http://bedtools.readthedocs.io/en/latest/) | Utilities for genome arithmetic | [Quinlan and Hall 2010](https://doi.org/10.1093/bioinformatics/btq033)
[deepTools](https://deeptools.github.io/) | Tools for exploring deep-sequencing data | [Ramirez et al. 2014](https://doi.org/10.1093/nar/gku365), [Ramirez et al. 2016](https://doi.org/10.1093/nar/gkw257)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

## Ribosome profiling

Tool | Description | Reference
---- | ----------- | ---------
[RiboTaper](https://ohlerlab.mdc-berlin.de/software/RiboTaper_126/) | An analysis pipeline for Ribo-Seq experiments, exploiting the triplet periodicity of ribosomal footprints to call translated regions | [Calviello et al. 2016](https://dx.doi.org/10.1038/nmeth.3688)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

# Training

To learn about RNA sequencing data analysis, we recommend you to have a look at the training material from the [Galaxy Training network](http://galaxyproject.github.io/training-material/RNA-Seq/), and particularly the tutorial about the [Reference-based RNA-seq data analysis](https://galaxyproject.github.io/training-material//RNA-Seq/tutorials/ref_based).

In the Galaxy RNA workbench, you will also find way to learn about the RNA analyis with some [Galaxy interactive tours](https://github.com/galaxyproject/galaxy-tours) to show you the way into the Galaxy instance, its tools and possibilities.

# Contributors

 - [Andrea Bagnacani](https://github.com/bagnacan)
 - [Bérénice Batut](https://github.com/bebatut)
 - [Joerg Fallmann](https://github.com/jfallmann)
 - [Florian Eggenhofer](https://github.com/eggzilla)
 - [Bjoern Gruening](https://github.com/bgruening)
 - [Youri Hoogstrate](https://github.com/yhoogstrate)
 - [Torsten Houwaart](https://github.com/TorHou)
 - [Cameron Smith](https://github.com/smithcr)
 - [Sebastian Will](https://github.com/s-will)
 - [Markus Wolfien](https://github.com/mwolfien)
 - [Dilmurat Yusuf](https://github.com/dyusuf)
 - [Pavankumar Videm](https://github.com/pavanvidem)
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

# How to contribute

The RNA-workbench community welcomes new contributions and help in any way.
We have collected detailed instructions and some guidance in our [CONTRIBUTING.md](https://github.com/bgruening/galaxy-rna-workbench/blob/master/CONTRIBUTING.md).

# Support and bug reports

For support, questions, or feature requests fill bug reports on our [issue page](https://github.com/bgruening/galaxy-rna-workbench/issues).
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

# MIT license

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
<p align="right"><a href="#top">&#x25B2; back to top</a></p>

