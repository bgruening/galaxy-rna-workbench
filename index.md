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

To use the Galaxy RNA workbench, you will need [Docker](https://www.docker.com/products/overview#h_installation)

## Usage

To launch locally the Galaxy RNA workbench, run: 

```
$ docker run -d -p 8080:80 bgruening/galaxy-rna-workbench
```

It will start the Galaxy RNA workbench with the configuration and launch of a Galaxy instance and its population with the needed tools. The instance will be accessible at [http://localhost:8080](http://localhost:8080).

For a more specific configuration, you can have a look at the [documentation of the Galaxy Docker Image](http://bgruening.github.io/docker-galaxy-stable/).

# Training


# Credit

The RNA analyses workbench is developed by the RNA Bioinformatics Center (RBC). This center is one of the eight service units of the German Network for Bioinformatics Infrastructure de.NBI, running the German ELIXIR Node ELIXIR Germany.

<img src="Logos/deNBI_logo.jpg" height="35px" alt="de.NBI" valign="middle"><img src="Logos/elixir_germany.png" height="55px" alt="ELIXIR Germany" valign="middle">