Standard MDI API
================
API for MDI Implementation Guide
--------------------------------
MDI Implementation Guide (IG) is available in https://build.fhir.org/ig/HL7/fhir-mdi-ig/index.html. This guide 
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

 | POST [base]/Composition/$mdi-documents
 | GET [base]/Composition/$mdi-documents?name1=value1&name2=value2


**Extended Operation for MDI Document** - In & Out Parameters

+------------------------+-------------+----------+---------------+-----------------------------------+
| Name                   | Cardinality | Type     | Documentation                                     |
+========================+=============+==========+===============+===================================+
| In Parameters                                                                                       |
+========================+=============+==========+===============+===================================+
| id                     | 0..1        | uri      | Resource ID of Composition - MDI to EDRS          |
+------------------------+-------------+----------+---------------------------------------------------+
| patient                | 0..*        |          | One or more decedent related search parameters    |
+------------------------+-------------+----------+---------------------------------------------------+
| patient.birthdate      | 0..1        | date     | Decedent's date of birth                          |
+------------------------+-------------+----------+---------------------------------------------------+
| patient.family         | 0..1        | string   | Decedent's last name                              |
+------------------------+-------------+----------+---------------------------------------------------+
| patient.given          | 0..1        | string   | Decedent's first name                             |
+------------------------+-------------+----------+---------------------------------------------------+
| patient.gender         | 0..1        | token    | Decedent's gender                                 |
+------------------------+-------------+----------+---------------------------------------------------+
| tracking-number        | 0..1        | token    | Search by identifier in Composition - MDI to EDRS |
+------------------------+-------------+----------+---------------------------------------------------+
| death-location         | 0..1        | string   | District of death location                        |
+------------------------+-------------+----------+---------------------------------------------------+
| death-date.actual      | 0..1        | date     | It should be either actual, pronounced, or all    |
| death-date.pronounced  |             |          | if 'all' is used, then it means searching by both |
| death-date.all         |             |          | 'actual' and 'pronounced' date of death           |
+------------------------+-------------+----------+---------------------------------------------------+
| Out Parameters                                                                                      |
+========================+=============+==========+===============+===================================+
| return                 | 0..1        | resource | Searchset Bundle that includes MDI document       |
|                        |             |          | bundles. If [id] is supplied, then this should be |
|                        |             |          | Bundle - Document MDI to EDRS                     |
+------------------------+-------------+----------+---------------------------------------------------+

Please note that the Search parameters related to patient are formatted with “.”. In FHIR, this means 
that the search parameters after “.” are part of a patient parameter. See the example below.

.. code-block:: json
    {
    "resourceType": "Parameters",
    "parameter": [
        {
        "name": "patient",
        "part": [
            { 
            "name": "family",
            "valueString": "Hans"
            },
            { 
            "name": "given",
            "valueString": "Kennoby"
            }
        ]
        }
    ]
    }

If [id] is provided within URL path (e.g., /Composition/[id]/$mdi-documents), then the output response 
should be an MDI document bundle as there will be only one or zero result.

If *id* or *search paraemters* is provided in the URL parameter or Parameters resource in the payload 
(e.g. [base]/Composition?name=value), then the output response should be a *searchset* bundle with 
matching MDI documents even if there is only one result. If “OR” search parameter is needed a searching 
parameter, then as specified in the FHIR specification (search.html), “,” should be used 
(e.g. “valueString”: “a,b,c” for matching either a, b, or c).

| “name”: xyz,
| “valueString”: “a”

| “name”: xyz,
| “valueString”: “a”


**Request**

.. code-block:: json
    POST [base]/Composition/$mdi-documents
    {
    "resourceType": "Parameters",
    "parameter": [
        {
        "name": "patient",
        "part": [
            { 
            "name": "family",
            "valueString": "Hans"
            },
            { 
            "name": "given",
            "valueString": "Kennoby"
            }
        ]
        }
    ]
    }


**Response**

.. code-block:: json
    GET [base]/Composition/$mdi-documents?name=Abc
    {
    "resourceType": "Bundle",
    "id": "13ab1ecf-38ce-4f47-aebb-a38396a80775",
    "type": "searchset",
    "total": 1,
    "entry": [
        {
        "resourceType": "Bundle",
        "id": "fd240814-5911-49bb-bb20-72066add4a18",
        "meta": {
            "profile": [
            "http://hl7.org/fhir/us/mdi/StructureDefinition/Bundle-document-mdi-to-edrs"
            ]
        },
        "type": "document",
        "entry": [
            {
            "fullUrl": "Composition/965a0688-e6f4-4bff-a96d-639cbd7ea295",
            "resource": {
                "resourceType": "Composition",
                "id": "965a0688-e6f4-4bff-a96d-639cbd7ea295",
                . . .
            }
        ]
        }
    ]
    }

Error Handling
^^^^^^^^^^^^^^
**API Level Errors**
API itself can indicate errors. API errors are displayed in the HTTP code. 2xx are returned when API 
transactions are successfully processed. 4xx or 5xx are error codes. 3xx are not errors. These codes 
need to be supported at the client side if redirections are required by the server. More details can 
be found from https://en.wikipedia.org/wiki/List_of_HTTP_status_codes. 

CMS must check if correct endpoint and search parameters are used if such errors are returned.

**MDI Document Level Errors**
For all non 2xx status code, error(s) must be indicated in the response with a *OperationOutcome* resource. 

In *OperationOutcome*, EDRS must be include information what caused the error if the error needs to be 
fixed by CMS. If it’s EDRS that needs to fix the error, it must be indicated so that CMS user(s) can 
contact EDRS for the error. Below shows an example of *OperationOutcome*.

.. code-block:: json
    HTTP/1.1 500 Internal Server Error
    {
    "resourceType": "OperationOutcome",
    "id": "searchfail",
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n      
        <p>The &quot;name&quot; parameter has the modifier &quot;exact&quot; which is not supported by 
        this server</p>\n</div>"
    },
    "issue": [
        {
        "severity": "fatal",
        "code": "code-invalid",
        "details": {
            "text": "The \"name\" parameter has the modifier \"exact\" which is not supported by this server"
        }
        }
    ]
    }


READ API (or GET A Document)
----------------------------
| GET [base]/Composition/[id]/$document

[id] is obtained from SEARCH API. $document is a standard FHIR operation to generate a (MDI) document.

Reference API document used as a base for this:
https://www.hl7.org/fhir/composition-operation-document.html

Example: 
https://apps.hdap.gatech.edu/raven-fhir-server/fhir/Composition/e4dda395-28fc-4232-bb75-1b3484fcc369/$document

UPDATE APIs
-----------
General format of update and amend APIs for MDI document is as follow,

| POST [base  url]/Composition/$update-mdi
| Payload = Parameters resource

Feature specific *operation* APIs are described in the subsections below. 

Input/Output
+------------------------+-------------+----------------------------+---------------------------------+
| Name                   | Cardinality | Type                       | Documentation                   |
+========================+=============+============================+=================================+
| In Parameters                                                                                       |
+========================+=============+==========+===============+===================================+
| Justification defined  | 0..*        | string                     | Any required parameters for a   |
| parameters             |             |                            | jurisdiction                    |
+------------------------+-------------+----------------------------+---------------------------------+
| mdi-document           | 0..1        | Bundle                     | MDI document bundle. The        |
|                        |             |                            | “mdi-document” is a reserved    |
|                        |             |                            | keyword. This should only be    |
|                        |             |                            | used for the MDI to EDRS        |
|                        |             |                            | profile bundle document.        |
+------------------------+-------------+----------------------------+---------------------------------+
| Out Parameters                                                                                      |
+========================+=============+============================+=================================+
| return                 | 0..1        | OperationOutcomeParameters | If an error occurs, OO resource |
|                        |             |                            | is returned. If response data   |
|                        |             |                            | need to be sent back,           |
|                        |             |                            | Parameters resource can be used.|
+------------------------+-------------+----------+---------------------------------------------------+

Ex. Request Body
.. code-block:: json
    {    
    "resourceType": "Parameters",    
    "parameter": [
        { 
        "name": edrs-rack-number",
        "valueString": "1234"
        },        
        { 
        "name": "jurisdiction defined key2",
        "valueString": "value2"
        },
        . . .

        { 
        "name": "mdi-document",
        "resource": <MDI document bundle>
        }
        ]
    } 


For In Parameters, jurisdictions can add their own parameters if it is needed for the update or amend 
operation. The Jurisdiction defined params should only be used within the jurisdiction. However, if 
parameters exist but cannot be understood, they should be ignored and NOT cause an error.

The mdi-document needs to conform to MDI document profile in the MDI IG. Profile specific update and 
amend APIs may use the profile specification to include only the data it needs to include. It is 
possible that all information can be included in the MDI document bundle and let the servers choose 
what they want to consume. However, this is not recommended and not safe for security.

Case Management System (CMS) needs to include file number, work number, or case number in the EDRS. 
This information can be specified in the Composition.identifiers. If a jurisdiction is already using 
the Composition.identifier for another purpose, then Jurisdiction defined params can be used. 
Currently, the following identifiers are used for the connect-a-thon testing.

* NH: Six-digit death certificate ID in the Composition.identifier.
      Work number in the URL parameter. This can use Jurisdiction defined params.
* GA: EDRS number is used in the Compoistion.identifier

The response if the UPDATE API was successful should be 200 OK. The payload is not required. If 
EDRS or CMS needs to respond with a message, Parameters resource can be used. Jurisdiction and 
CME office can define parameters using Parameters resource. If the submitted MDI document will 
be included in the response body, then “mdi-document” parameter key should be used. If the API was 
successful, but there were some warnings that EDRS wants to send back to CMS, then parameter name 
should be “warning”. And, “resource” should be used to include OperationOutcome resource.

If error occurs, then OperationOutcome will be sent back to CMS. 

Ex. Response Body (if the operation was successful, and EDRS wants to respond with data) 

.. code-block:: json
    {
        "resourceType": "Parameters",    
        "parameter": [
        { 
        "name": "jurisdiction defined key1",
        "valueString": "value1"
        },        
        { 
        "name": "jurisdiction defined key2",
        "valueString": "value2"
        },
        . . .

        { 
        "name": "mdi-document",
        "resource": <MDI document bundle>
        },
        { 
        "name": "warning",
        "resource": <OperationOutcome resource>
        }
        ]
    }

Response Body (If error occurs)

.. code-block:: json
    {
    "resourceType": "OperationOutcome",
    "id": "searchfail",
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n      <p>The &quot;case number&quot; 1234 does not exist</p>\n    </div>"
    },
    "issue": [
        {
        "severity": "fatal",
        "code": "case-invalid",
        "details": {
            "text": "The \"case number\" 1234 does not exist."
            }
        }
    ]
    }

Cause-Manner Update API ($cause-manner-update-mdi)
--------------------------------------------------
Causes of death are defined after the death investigation. Thus, when the case is created, and search(es) 
were performed, causes-of-death data elements would be likely either not available or marked as pending. 
This API is used to update the causes of death in the working death report. 

In the cause-of-death update API, Case Management System (CMS) can focus on the cause_manner section 
slice of MDI document as shown in 
https://build.fhir.org/ig/HL7/fhir-mdi-ig/StructureDefinition-Composition-mdi-to-edrs.html. 
All resource profiles that are referred to in this section should be included in the entry of the Bundle 
document. The other sections are optional, which can be added based on the need. Please refer to the 
following example. 

| POST [base]/Composition/$cause-manner-update-mdi

Payload:
.. code-block:: json
    {    
    "resourceType": "Parameters",    
    "parameter": [
        { 
        "name": "mid-document",
        "resource": {
            "resourceType": "Bundle",
            …
            "entry": [ {
            "resourceType": "Composition", …
            "section": […] // sliced section for cause_manner.
            } …
            ]
        }
    ]
    }

Additional parameters can be added to the Parameters resource if it’s required for a jurisdiction workflow. 
Sliced sections for other profiles can also be added. However, it may violate in some jurisdiction death 
registration systems that enforce the confidentiality during the data exchanges.

Amending Certificate API (after death report is certified)
----------------------------------------------------------
Future work

Certification API
-----------------
Future work

CREATE API
----------
Future work

DELETE API
----------
Future work
