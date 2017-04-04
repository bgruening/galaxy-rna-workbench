# Contributing

The Galaxy RNA-workbench project welcomes new contributors!
This document briefly describes how to contribute to the [RNA-workbench](https://github.com/bgruening/galaxy-rna-workbench).

## Before you Begin

If you have an idea for a feature to add or an approach for a bugfix,
the most common venues for this are [GitHub issues](https://github.com/bgruening/galaxy-rna-workbench/issues).
If you have general Galaxy related questions or want to contribute to Galaxy as a framework join the project
at https://github.com/galaxyproject/galaxy. We are are generally available via [Gitter](https://gitter.im/galaxyproject/Lobby) or
[IRC](https://wiki.galaxyproject.org/GetInvolved#IRC_Channel).

## Reporting a new issue

If no existing issue seems appropriate, a new issue can be
opened using [this form](https://github.com/bgruening/galaxy-rna-workbench/issues/new).

## How to Contribute

* All changes to the [RNA-workbench](https://github.com/bgruening/galaxy-rna-workbench)
  should be made through pull requests to this repository (with just two
  exceptions outlined below).

* If you are new to Git, the [Try Git](http://try.github.com/) tutorial is a good places to start.
  More learning resources are listed at https://help.github.com/articles/good-resources-for-learning-git-and-github/ .

* Make sure you have a free [GitHub](https://github.com/) account.

* Fork the [RNA-workbench repository](https://github.com/bgruening/galaxy-rna-workbench) on
  GitHub to make your changes.
  To keep your copy up to date with respect to the main repository, you need to
  frequently [sync your fork](https://help.github.com/articles/syncing-a-fork/):
  ```
    $ git remote add upstream https://github.com/bgruening/galaxy-rna-workbench
    $ git fetch upstream
    $ git checkout dev
    $ git merge upstream/dev
  ```

* Commit and push your changes to your
  [fork](https://help.github.com/articles/pushing-to-a-remote/).

* Open a [pull
  request](https://help.github.com/articles/creating-a-pull-request/)
  with these changes. You pull request message ideally should include:

   * A description of why the changes should be made.

   * A description of the implementation of the changes.

   * A description of how to test the changes.

* The pull request should pass all the continuous integration tests which are
  automatically run by GitHub using e.g. Travis CI.

* Your pull request will be reviewed by the RNA community and merged if one member of the core team
  approves the changes.

## A Quick Note about new Tools

  Galaxy tools should be published to the
  [Tool Shed](https://galaxyproject.org/toolshed) and specified in our
  [tool list](https://github.com/bgruening/galaxy-rna-workbench/blob/master/rna_workbench.yml).
  Our continuous integration tests, will build a new workbench with your tool included automatically and will run
  a few tests to check the integrety.

  More information about tool development can be found [on the comunity hub](https://galaxyproject.org/develop).
