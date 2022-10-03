.. _componentOverview:

Component Overview
==================
Raven / Bluejay FHiR Server
---------------------------
Raven platform stores all the MDI case data in the Raven FHIR server and all the EDRS case data in the 
Bluejay FHIR server. Both Raven and Bluejay FHIR server shares the same code stack. Thus, functionally,
they have same capability.

The FHIR server is developed using HAPI FHIR library with fhirbase as a backend database. Basic instance 
level of FHIR APIs are implemented such as, ::

    GET  [base FHIR Url]/Patient/[id] or [search parameters for SEARCH]
    POST [base FHIR Url]/Patient with Patient Resource in the payload
    DELETE [base FHIR Url]/Patient/[id]

In addition to the basic FHIR API, FHIR operation APIs are also implemented for transaction, batch, $document, 
$process-message operations. 

To support MDI-API, FHIR extended operations are implemented as defined in the ":ref:'_mdiStqandard'"
page. More pieces of information about the Raven FHIR server APIs are available in the ":ref:`_ravenAPI`".

Raven Dashboard
-----------------
Coming Soon ...
