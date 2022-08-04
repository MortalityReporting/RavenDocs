Architecture and Components
===========================

System Overview
---------------

The following diagram is intended to give a general look at the Raven
Platform. Please note that this is not to be considered a strictly
technical architecture diagram for development purposes, and is only
intended to demonstrate a high level view of the functionality of the
system as relates to the physical layout of components, connection to
external end points, and the users’ scope.


.. image:: 
   images/RavenRevisedDiagram.png
   :alt: Raven Overview Diagram

Raven Dashboard
---------------

The Raven Dashboard is the user facing piece of the Raven Platform. The
landing page for the dashboard is the browse cases screen, which
provides a list of current cases stored on the Raven FHIR Server with a
few high level details such as identifiers along with the current export
status for that case. Selecting a case allows for viewing the details of
that case, and allows the initiation of the export process.

The dashboard also provides case import functionality. Users may select
a local CSV of case records, configure a mapping of that user CSV to the
Raven MDI CSV format, and then pass it to the Raven Import API to be
posted on the FHIR Server. Upon mapping, the dashboard will also allow
the user to download the Raven MDI CSV version of their data.

Raven FHIR Server
-----------------

The Raven FHIR Server is a customized FHIR Server built on top of a
Fhirbase database. It serves as the API access to the database as per
FHIR specifications.

Raven Import and Submission API
-------------------------------

This component provides for two separate APIs that the Raven Platform
utilizes. The first is the Import (and Mapper) API, which handles the
conversion of MDI CSV Data for posting to the FHIR Server. This portion
of the API is hit by the dashboard when a user imports their data into
the system. The second API is the Submission API, which allows the
exportation of the FHIR VRDR documents to an external endpoint or
endpoints, presumably as part of an external Electronic Death Records
System (EDRS).
