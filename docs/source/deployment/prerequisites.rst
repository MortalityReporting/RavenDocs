Local Demo Prerequisites
========================

To begin deploying the Raven Platform, you will require Docker/Docker
Desktop and Git at a minimum.

-  `Docker <https://docs.docker.com/get-docker/>`__ - Docker is a
   platform for deploying “containers”, which provide for consistent
   environments in which software can run in isolation. The Raven
   Platform components are provided as Docker containers to simplify
   running each component in your local environment. To learn more about
   Docker and containers, please see:
   [[https://www.docker.com/resources/what-container]].

**For Windows Users:** From the Windows Store you can install the
Windows Ubuntu terminal, giving you the ability to work from a Linux
command line environment. You may also wish to setup Windows Subsystem
for Linux 2 (WSL2) and enable the WSL2 integration in Docker Desktop.
This circumvents many common issues working with Docker on a Windows
system. For more information on Docker and WSL 2, please visit
[[https://docs.docker.com/docker-for-windows/wsl/]].

Git should be pre-installed in most environments, including the base Mac
terminal and Windows Ubuntu terminal.

In addition to these tools, if you intended to attempt to build
components of Raven without using Docker, you will require the
following:

1) `Java JDK version 10 or
   higher <https://www.oracle.com/java/technologies/javase-downloads.html>`__
   - The Java Development Kit is required to run some components of the
   Raven Platform.

2) `Maven <http://maven.apache.org/>`__ - Maven is a build tool for Java
   based projects, and is used to build some of the Raven components.

**For Mac Users:** Homebrew is the recommended means of installing and
managing Maven and Git. For more on Homebrew, please visit
[[https://brew.sh/]].

Once you have all of the required tools installed, you are ready to get
started. \__\_ `Continue to Step 1 - Getting Started and FHIR
Database <Local-Demo-Step-1-Getting-Started>`__
