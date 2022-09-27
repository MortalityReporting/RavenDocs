Standard MDI API
================
API for MDI Implementation Guides (IG) 
--------------------------------------
MDI Implementation Guide is available in https://build.fhir.org/ig/HL7/fhir-mdi-ig/index.html. This guide 
is currently working in progress. Thus, please visit frequently for any updates.
 
FHIR has already defined the Restful API. The FHIR Restful API document is available from 
https://hl7.org/FHIR/http.html. And, FHIR Restful API Operations are documented in 
https://hl7.org/FHIR/operationslist.html. Not all API interactions and operations are required to be 
implemented for the data transactions between CMS and EDRS. However, there are common parts that all API 
implementations need to conform, 
 
MIME-type for FHIR resources is application/fhir+xml or application/fhir+json. This needs to be specified 
for Content-Type in the HTTP header. application/x-www-form-urlencoded can be used for POST search requests 
if HTTP Form is used. 
 
This document defines MDI Standard API in FHIR (MAPI-FHIR). MAPI-FHIR is based on the MDI IG that supports 
CMS interoperability with external systems such as EDRS or forensic lab. Thus, EDRS that conforms to 
MAPI-FHIR should be able to implement FHIR API.  
 
All implemented FHIR resources, interactions, and operations can be published using CompatibilityStatement 
via FHIR metadata API (GET [base]/metadata). Detail information about the CompatibilityStatement is available 
in https://hl7.org/FHIR/capabilitystatement.html. Please see the Appendix A for the CompatibilityStatement 
from the Raven FHIR server. 
 
It’s recommended for EDRS to provide CompatibilityStatement. If the API method for the metadata cannot be 
available, then EDRS needs to provide CMS with what resources, interactions, and operations are available 
via other methods such as PDF or Word document. 

Security
--------
It’s recommended to use OAuth2 with OpenID. EDRS should provide authorization server to authenticate and 
authorize the CMS to access the EDRS FHIR server. Please refer to http://www.hl7.org/fhir/smart-app-launch/ 
if EDRS wishes to implement SMART on FHIR framework. However, SMART on FHIR is not required.  

.. image:: 
   ../images/mapi_cms_to_edrs_workflow.png
   :alt: CMS to EDRS Workflow

SEARCH API
----------
FHIR API is very extensive. However, not all interactions and operations are required to be implemented. 
The search API described in this section is the one that can be suitable for the workflow between CMS and 
EDRS.

Extended Operation for MDI Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is a resource instance type extended operation to generate a document from Composition Resource using 
the search parameters.

This is an idempotent operation. Both POST and GET can be used with the following endpoint URL pattern.

```
POST [base]/Composition/$mdi-documents
GET [base]/Composition/$mdi-documents?name1=value1&name2=value2
```

.. flat-table:: Extended Operation for MDI Document - In & Out Parameters
   :header-rows: 1
   * - Name
     - Cardinality
     - Type
     - Documentation
   * - :cspan: `3` In Parameters
   * - id
     - 0..1
     - uri
     - Resource ID of Composition - MDI to EDRS
   * - patient
     - 0..*
     - 
     - One or more decedent related search parameters
   * - patient.birthdate
     - 0..1
     - date
     - Decedent’s date of birth
