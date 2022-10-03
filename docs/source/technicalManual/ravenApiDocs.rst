.. _ravenAPI:

Raven Platform API Documentation
================================
Raven Platform maintains the following APIs. 

FHIR server APIs: Raven coponents use FHIR server to load and query MDI data. Thus, basic FHIR APIs are
supported (i.e. Create, Read, Update, and Delete (CRUD) in basic resource types are defined in the MDI.) 

Full FHIR API documentation is available from https://hl7.org/fhir/R4/http.html. 

The following default FHIR operations are supported as well. ::

    Process message:   $process-message (https://hl7.org/fhir/R4/composition-operation-document.html)
    Generate Document: $document (https://hl7.org/fhir/R4/messageheader-operation-process-message.html)

In order to support MDI-API, the FHIR server also implements FHIR extended operations. the extended 
operations are available in ":ref:`mdiAPI`"
