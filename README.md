RNA Galaxy Workbench
====================

The RNA analyses workbench is developed by the RNA Bioinformatics Center which is part of the  [German Network for Bioinformatics Infrastructure (de.NBI)](http://www.denbi.de/). 


Usage
=====

At first you need to install docker. Please follow the instruction on https://docs.docker.com/installation/

After the successful installation, all what you need to do is:

``docker run -d -p 8080:80 bgruening/galaxy-rna-workbench``

I will shortly explain the meaning of all the parameters. For a more detailed describtion please consult the [docker manual](http://docs.docker.io/), it's really worth reading.

Let's start: ``docker run`` will run the Image/Container for you. In case you do not have the Container stored locally, docker will download it for you. ``-p 8080:80`` will make the port 80 (inside of the container) available on port 8080 on your host. Inside the container a Apache Webserver is running on port 80 and that port can be bound to a local port on your host computer. With this parameter you can access your Galaxy instance via ``http://localhost:8080`` immediately after executing the command above. ``bgruening/galaxy-deeptools`` is the Image/Container name, that directs docker to the correct path in the [docker index](https://index.docker.io/u/bgruening/galaxy-stable/). ``-d`` will start the docker container in daemon mode. For an interactive session, you can execute:

``docker run -i -t -p 8080:80 bgruening/galaxy-rna-workbench``

and run the ``` startup ``` script by your own, to start PostgreSQL, Apache and Galaxy.

Docker images are "read-only", all your changes inside one session will be lost after restart. This mode is usefull to present Galaxy to your collegues or to run workshops with it. To install Tool Shed respositories or to save your data you need to export the calculated data to the host computer.

Fortunately, this is as easy as:

``docker run -d -p 8080:80 -v /home/user/galaxy_storage/:/export/ bgruening/galaxy-rna-workbench``

With the additional ``-v /home/user/galaxy_storage/:/export/`` parameter, docker will mount the folder ``/home/user/galaxy_storage`` into the Container under ``/export/``. A ``startup.sh`` script, that is usually starting Apache, PostgreSQL and Galaxy, will recognise the export directory with one of the following outcomes:

  - In case of an empty ``/export/`` directory, it will move the [PostgreSQL](http://www.postgresql.org/) database, the Galaxy database directory, Shed Tools and Tool Dependencies and various config scripts to /export/ and symlink back to the original location.
  - In case of a non-empty ``/export/``, for example if you continue a previouse session within the same folder, nothing will be moved, but the symlinks will be created.

This enables you to have different export folders for different sessions - means real separation of your different projects.


Enabling Interactive Environments in Galaxy
-------------------------------------------

Interactive Environments (IE) are sophisticated ways to extend Galaxy with powerful services, like IPython, in a secure and reproducible way.
For this we need to be able to launch Docker containers inside our Galaxy Docker container. At least docker 1.3 is needed on the host system.

``docker run -d -p 8080:80 -p 8021:21 -p 8800:8800 --privileged=true -v /home/user/galaxy_storage/:/export/ bgruening/galaxy-stable``

The port 8800 is the proxy port that is used to handle Interactive Environments. ``--privileged`` is needed to start docker containers inside docker.

Using Parent docker
-------------------
On some linux distributions, Docker-In-Docker can run into issues (such as running out of loopback interfaces). If this is an issue,
you can use a 'legacy' mode that use a docker socket for the parent docker installation mounted inside the container. To engage, set the 
environmental variable DOCKER_PARENT

``docker run -d -p 8080:80 -p 8021:21 -p 8800:8800 --privileged=true -e DOCKER_PARENT=True -v /var/run/docker.sock:/var/run/docker.sock -v /home/user/galaxy_storage/:/export/ bgruening/galaxy-stable``



Users & Passwords
================

The Galaxy Admin User has the username ``admin@galaxy.org`` and the password ``admin``.
The PostgreSQL username is ``galaxy``, the password is ``galaxy`` and the database name is ``galaxy`` (I know I was really creative ;)).
If you want to create new users, please make sure to use the ``/export/`` volume. Otherwise your user will be removed after your docker session is finished.


Requirements
============

- [docker](https://docs.docker.com/installation/)


Contributers
============

 - Cameron Smith
 - Torsten Houwaart
 - Bjoern Gruening


History
=======

 - 0.1: Initial release!


Support & Bug Reports
=====================

For support, questions, or feature requests contact deeptools@googlegroups.com or fill bug reports at https://github.com/bgruening/galaxy_recipes/issues.



Licence (MIT)
=============

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
