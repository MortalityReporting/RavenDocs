.. _componentOverview:

Component Overview
==================

.. image::
   ../images/component_diagram.png
   :alt: Raven Component Architecture


Raven FHIR Server
-----------------
The Raven platform stores MDI case data in the Raven FHIR server. The Raven FHIR server is developed 
using `HAPI FHIR Java library <https://hapifhir.io/hapi-fhir/>`_ with 
`fhirbase <https://www.health-samurai.io/fhirbase>`_ as the backend database. Basic instance 
level of the FHIR APIs are implemented and available as, ::

    GET  [base FHIR Url]/Patient/[id] or [search parameters for SEARCH]
    POST [base FHIR Url]/Patient with Patient Resource in the payload
    DELETE [base FHIR Url]/Patient/[id]

In addition to the basic FHIR API, FHIR operation APIs are also implemented for transaction, 
batch, $document, and $process-message operations. $process-message is the operation that
Toxicology-to-CMS workflow is using.

Bluejay FHIR Server
-------------------
The Bluejay FHIR server is an instance that is configured to simulate EDRS that supports 
:ref:`mdiAPI` (MDI-API). The Bluejay FHIR server is also based on the same code stack as Raven FHIR Server. 
Thus, the Bluejay FHIR server also provides the basic instance level of the FHIR APIs. 

MDI-API that the Bluejay FHIR server currently supports is search API. Case Management Systems can
test their MDI-API's search API feature with the Bluejay FHIR server. Please contact 
:ref:`our team <members>` to arrange the testing.

Raven Dashboard
-----------------
The Raven Dashboard is the user interface for the Raven Platform. It consists of multiple core modules and features.

* Case Importing and Viewing
   * Case Viewer - View MDI case records currently stored on the Raven FHIR Server, with the ability to view the underlying FHIR structures in a human readable narrative, XML, or JSON.
   * Import Case Records - Import records to the Raven FHIR Server. Records can be submitted directly as a FHIR MDI-to-EDRS Document Bundle or from the MDI test case spreadsheet (XLSX file).
* Validate and Compare
   * FHIR Validator - UI wrapper for the official HL7 FHIR Validator command line tool.
   * Record Comparison (In Development) - Compare a user-generated FHIR MDI Document bundle created from a test case against a known valid rendering of the same test case.
* Workflow Simulator (In Development) - Move through steps of one of several test scenarios for various MDI related workflows, such as CMS to EDRS or a Toxicology Lab to CMS. The workflow simulator integrates other features.

The Raven Dashboard is a frontend TypeScript project develped using the Angular framework, leveraging major libraries such as Angular Material Design components.

Raven Import API
----------------
The Raven Import API provides a backend service to import test cases from XLSX spreadsheets into the Raven FHIR Server as a FHIR MDI-to-EDRS Document Bundle. The API returns the results of the process to the Dashboard for rendering to users.

Validation Service
------------------
The Validation Service is a web API which wraps the HL7 command line FHIR validation tool. The Raven Dashboard allows users to post a FHIR resource to the validation service, which returns to the results of the validation.
