Local Deployment Instructions
=============================

This tutorial will provide a walkthrough of deploying the Raven Platform
locally using Docker. It is divided into a prerequisites section as well
as 4 steps, each on their own wiki page. You may navigate between the
steps using the sidebar menu or through the navigation controls at the
bottom of each page.

Contents Overview
-----------------

.. toctree::
   
   deployment/prerequisites
   deployment/database
   deployment/server
   deployment/api
   deployment/dashboard
   deployment/containers

-  `Prerequisites <Local-Demo-Prerequisites>`__ - This section provides
   a list of software and account requirements you will need for a
   deployment. Please read this page thoroughly and ensure you have
   everything setup before proceeding with the Raven deployment.

1. `Getting Started and FHIR
   Database <Local-Demo-Step-1-Getting-Started>`__ - This section covers
   the prerequisites for setting up the Raven Platform on your local
   system, cloning the Raven Platform repository, and setting up a
   simple FHIR database to work with.
2. `Raven FHIR Server <Local-Demo-Step-2-Raven-FHIR-Server>`__ - This
   section covers deployment of the Raven FHIR Server.
3. `Raven Import and Submission
   API <Local-Demo-Step-3-Raven-Import-and-Submission-API>`__ - This
   section covers deployment of the Raven Import and Submission API
   component which contains the Import/Mapper and Export/Submission
   APIs.
4. `Raven Dashboard <Local-Demo-Step-4-Raven-Dashboard>`__ - This
   section covers deployment of the Raven Dashboard.

-  `Managing Raven Containers and Data
   Persistence <Local-Demo-Managing-Raven-Containers>`__ - If during the
   course of your deployment or use you need to stop and start
   individual containers, consult this section. This section also
   briefly discusses data persistence within the local deployment of the
   Raven Platform.
