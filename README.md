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

## RNA workbench launch

Kitematic users can launch the RNA workbench directly from its interface, browsing all publicly available images from the Docker Hub.

The following video shows the launch of the RNA workbench from Kitematic:

[![Galaxy RNA workbench launch through Kitematic](https://i.imgur.com/P5Mg1Qs.png)](https://www.youtube.com/watch?v=fYer4Xdw_h4 "Kitematic galaxy-rna-workbench launch")


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


# Available Tools

| Category   | Tools |
| -------- | ----------- |
| RNA Structure Analysis| [ViennaRNA](http://www.tbi.univie.ac.at/RNA/), [Kinwalker](http://www.bioinf.uni-leipzig.de/Software/Kinwalker/), [MEA](http://www.bioinf.uni-leipzig.de/Software/mea/), [RNAz](http://www.tbi.univie.ac.at/~wash/RNAz/), [Cofold](http://www.e-rna.org/cofold/), [RNAshapes](https://bibiserv2.cebitec.uni-bielefeld.de/rnashapes), [antaRNA](http://www.bioinf.uni-freiburg.de/Software/antaRNA/)|
| RNA Alignment | [Compalignp](http://www.biophys.uni-duesseldorf.de/bralibase/), [MAFFT](http://mafft.cbrc.jp/alignment/software/), [LocARNA](http://rna.informatik.uni-freiburg.de/LocARNA/Input.jsp) |
| RNA Annotation | [GotohScan](http://www.bioinf.uni-leipzig.de/Software/GotohScan/), [RNAcode](http://wash.github.io/rnacode/), [INFERNAL](http://eddylab.org/infernal/), [RNAmmer](http://www.cbs.dtu.dk/services/RNAmmer/), [ARAGORN](http://mbio-serv2.mbioekol.lu.se/ARAGORN/), [tRNAscan](http://lowelab.ucsc.edu/tRNAscan-SE/), [RNABOB](http://eddylab.org/software.html) |
| RNA-protein Interaction |  [DoRiNA](http://dorina.mdc-berlin.de/), [Piranha](https://github.com/smithlabcode/piranha), [RNAcommender](https://github.com/gianlucacorrado/RNAcommender), [PARalyzer](https://ohlerlab.mdc-berlin.de/software/PARalyzer_85/)|
| Ribosome Profiling | [RiboTaper](https://ohlerlab.mdc-berlin.de/software/RiboTaper_126/) |
| RNA-Seq |[SortMeRNA](http://bioinfo.lifl.fr/RNA/sortmerna/), [BlockClust](http://www.bioinf.uni-freiburg.de/Software/) , [MiRDeep2](https://www.mdc-berlin.de/8551903/en/)  |
| RNA Target Prediction | [TargetFinder](https://github.com/carringtonlab/TargetFinder) |

# Contributors

 - Andrea Bagnacani
 - Bérénice Batut
 - Joerg Fallmann
 - Bjoern Gruening
 - Torsten Houwaart
 - Cameron Smith
 - Sebastian Will
 - Dilmurat Yusuf


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
