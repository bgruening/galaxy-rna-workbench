---
layout: default
---

# About

The Galaxy RNA workbench is a framework dedicated to the analysis of RNAs. 

The framework is based on a [Galaxy instance](https://galaxyproject.org/) with only RNA related tools:

- [ViennaRNA](http://www.tbi.univie.ac.at/RNA/)
- Compalignp to compute fractional identity between trusted alignment and test alignment
- DoRINA: data source for RNA interactions in post-transcriptional regulation
- GotohScan to find subsequences in db
- Kinwalker for the cotranscriptional folding of RNAs
- MAFFT, a multiple alignment program for amino acid or nucleotide sequences
- MEA to predict MEA structures and compare structures of RNAs
- Piranha, a peak-caller for CLIP- and RIP-Seq data
- [RiboTaper](https://ohlerlab.mdc-berlin.de/software/RiboTaper_126/), a method for defining traslated ORFs using Ribosome Profiling data
- RNAcode to analyze the protein coding potential in MSA
- [RNAcommender](https://github.com/gianlucacorrado/RNAcommender) a tool for genome-wide recommendation of RNA-protein interactions
- [SortMeRNA](http://bioinfo.lifl.fr/RNA/sortmerna/) for fast and accurate filtering of ribosomal RNAs in metatranscriptomic dat
- [LocARNA](http://www.bioinf.uni-freiburg.de/Software/LocARNA/) for multiple Alignment and Folding of RNAs
- [PARalyzer](https://ohlerlab.mdc-berlin.de/software/PARalyzer_85/), a method to generate a high resolution map of interaction sites between RNA-binding proteins and their targets
- [infernal](http://infernal.janelia.org/) for the inference of RNA Alignments
- RNAmme to find rRNA genes in a DNA sequence
- trna_prediction for the prediction of t-RNA with aragorn and tRNAscan-SE
- [RNAz](https://www.tbi.univie.ac.at/~wash/RNAz/) for predicting structural noncoding RNAs
- BlockClust for the non-coding RNA clustering from deep sequencing read profiles
- [Cofold](http://www.e-rna.org/cofold/) for the prediction of RNA secondary structure that takes co-transcriptional folding into account
- [RNAshapes](http://bibiserv.techfak.uni-bielefeld.de/rnashapes/) for RNA secondary structure predictions
- MiRDeep2 for identification of novel and known miRNAs in deep sequencing data
- RNABOB for fast pattern searching for RNA structural motifs
- antaRNA, using ant colony optimization to solve the inverse folding problem in RNA research
- [TargetFinder](https://github.com/carringtonlab/TargetFinder.git) to predict plant small RNA target

# Usage

The Galaxy RNA workbench is based on a dedicated Galaxy instance wrapped into a Docker container. It is based on the [Galaxy Docker Image](http://bgruening.github.io/docker-galaxy-stable/)

## Requirement

To use the Galaxy RNA workbench, you will need [Docker](https://www.docker.com/products/overview#h_installation). 

Windows and OS-X users are encouraged to use [Kitematic](https://github.com/bgruening/galaxy-rna-workbench/blob/master/howto_kitematic.md), a graphical User-Interface for managing Docker containers.

For Linux users and people familiar with the command line can follow the instruction on installing Docker from [Docker website](https://docs.docker.com/installation).

## Usage

Starting the RNA workbench Docker container is analogous to starting the generic Galaxy Docker image: 

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
  $ docker run -i -t -p 8080:80 bgruening/galaxy-rna-workbench
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

# Training

To learn about RNA sequencing data analysis, we recommend you to have a look at the training material from the [Galaxy Training network](http://bgruening.github.io/training-material/RNA-Seq/), and particularly the [tutorial about the Reference-based RNA-seq data analysis](http://bgruening.github.io/training-material//RNA-Seq/tutorials/ref_based).

In the Galaxy RNA workbench, you will also find way to learn about the RNA analyis with some [Galaxy tours](https://github.com/galaxyproject/galaxy-tours) to show you the way into the Galaxy instance, its tools and possibilities.


# Credit

The RNA analyses workbench is developed by the RNA Bioinformatics Center (RBC). This center is one of the eight service units of the German Network for Bioinformatics Infrastructure de.NBI, running the German ELIXIR Node ELIXIR Germany.

<img src="assets/img/deNBI_logo.jpg" height="35px" alt="de.NBI" valign="middle"> <img src="assets/img/elixir_germany.png" height="55px" alt="ELIXIR Germany" valign="middle">

Contributors to this RNA analyses workbench:

 - Bérénice Batut
 - Joerg Fallmann
 - Bjoern Gruening
 - Torsten Houwaart
 - Cameron Smith
 - Sebastian Will
 - Dilmurat Yusuf
