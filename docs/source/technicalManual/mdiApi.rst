.. _mdiAPI:

================
Standard MDI API
================

.. note::
    Standard MDI API will be documented as a best practice in the MDI IG site in the future. 
    Until then, the Raven documentation will temporarily house the Standard MDI API specification.
    
    
Operation APIs for MDI-to-EDRS Workflow
=======================================
MDI Implementation Guide (IG) is available in http://hl7.org/fhir/us/mdi/  This 
guide should be used for the payload content format.
 
FHIR has also defined the Restful API for operations. The FHIR Restful API document is available from 
https://hl7.org/FHIR/http.html. And, FHIR Restful API Operations are documented in 
https://hl7.org/FHIR/operationslist.html. MDI API is extended operations of the FHIR Restful 
API operations. Thus, the basic rules of FHIR API are also applied to MDI API. For example,

* Content-type for FHIR resources is application/fhir+xml or application/fhir+json. This needs to 
  be specified in the HTTP header. 
* application/x-www-form-urlencoded can be used for POST search requests if HTTP Form is used. 
 
In FHIR, FHIR resources, interactions, and operations are published using CompatibilityStatement 
(GET [base]/metadata). Detailed information about the CompatibilityStatement is available 
in https://hl7.org/FHIR/capabilitystatement.html. It is recommended that EDRS FHIR servers publish 
their capability statement as defined in this link. 

Security Recommendations
========================
This section covers a minimum level of security recommended by the MDI FHIR IG. There are more data 
exchange protocols and content models defined in the `FHIR Security document <https://www.hl7.org/fhir/security.html>`_. 
MDI systems that require a higher level of security should refer to the FHIR Security document 
for the interoperability.  

Secure Data Transportation
--------------------------
In most modern systems, digital data are exchanged using web services. FHIR recommends a web service 
called RESTful Application Programming Interface (REST API) where REST stands for **RE**\ presentational **S**\ tate 
**T**\ ransfer. REST API uses Transport Layer Security (TLS) for the secure transportation. More accurately, 
TLS 1.2 or higher needs to be used. This is also known as HTTPS. All data exchanges in MDI FHIR IG must 
be done in HTTPS

Standard Authorization Protocol
-------------------------------
A standard authorization protocol that can be used for the data access is the OAuth 2.0 (OAuth2) 
Authorization Framework defined in `RFC 6749 <https://www.rfc-editor.org/rfc/rfc6749>`_. There are many documents provided by OAuth2 service 
providers that are much easier and simpler to understand. Searching on Internet using “OAuth2” keyword 
will return several related documents.

Roles in OAuth2
^^^^^^^^^^^^^^^
OAuth2 defines several components that play different roles. Systems in MDI IG should play the roles to 
support the OAuth2. The OAuth2 roles are changed depending on the roles in the MDI workflows. Table1 
shows which OAuth2 roles the systems in MDI IG should play in the MDI-to-EDRS and Toxicology-to-MDI 
workflows. As more workflows are added to the MDI IG, additional roles may be added to the system, 
which may be ended up playing multiple roles.

+-----------------------+---------------------------------------------------------------------+-------------+--------------+
|Role                   |Responsibility                                                       |MDI-to-EDRS  |Tox-to-MDI    |
+=======================+=====================================================================+=============+==============+
|| Authorization Server || Server that authenticates the resource owner and issues access     || EDRS       || CMS         |
||                      || tokens to the client application. The authorization server can be  ||            ||             |
||                      || the same as the authentication server or can be a separate server. ||            ||             |
+-----------------------+---------------------------------------------------------------------+-------------+--------------+
|| Client               || Application that wants to access the resource on behalf of the     || CMS        || LIMS        |
||                      || resource owner. The client can be a web application, a mobile      ||            ||             |
||                      || application, or a desktop application.                             ||            ||             |
+-----------------------+---------------------------------------------------------------------+-------------+--------------+
|| Resource Owner       || User who owns the resource (such as a photo or a document) that    || CMS Users  || LIMS Users  |
||                      || a client application wants to access. The resource owner grants    || EDRS Users ||             |
||                      || permission to the client application to access the resource.       ||            ||             |
+-----------------------+---------------------------------------------------------------------+-------------+--------------+
|| Resource             || Server that hosts the resource that the client application wants   || EDRS       || CMS         |
|| Server (Provider)    || to access. The resource server verifies the access token and       ||            ||             |
||                      || grants access to the resource if the token is valid.               ||            ||             |
+-----------------------+---------------------------------------------------------------------+-------------+--------------+
**Table1**\ : Roles in OAuth2 and MDI Systems


OAuth2 Flows
^^^^^^^^^^^^
OAuth2 defines different flows based on the client (or application) types. This document only discusses 
the flow(s) that might be applicable to the client types in MDI. Figure 1 depicts the authorization code 
flow that can provide authentication and authorization of clients in MDI workflows. Detail transactions 
for the authorization code flow are explained in section 4.1 of `RFC 6749 <https://www.rfc-editor.org/rfc/rfc6749>`_.

.. figure:: ../images/authorization_code_flow.png
   :alt: Authorization Code Flow in OAuth2
   
**Figure 1**\ : Authorization Code Flow in OAuth2


Client Registration
~~~~~~~~~~~~~~~~~~~
For a client to be able to get authenticated and authorized, the client must be registered at the 
authorization server. When a client is registered, the client should provide *redirection_uri*\ . 
*Client_id* will then be issued to the client. The client will use the *client_id* and *redirection_uri* 
for its authentication and authorization.


Authorization Request
~~~~~~~~~~~~~~~~~~~~~
Client first needs to get an authorization code. In Figure 1, 1, 2, and 3 are the authorization request 
steps. Client should provide client identifier with *client_id* and *redirection_uri (optional)*. *Client_id* 
and *redirection_uri* will be matched with registered data at the authorization server (1). If the request 
is valid, then the client will be redirected to user authentication (2) where authentication and consent 
occur. Once client authenticated and authorized, authorization code is returned to client by being 
redirected to the *redirection_uri* (3).

Parameters for the authorization request are as follows. They are included as URL parameters with HTTPS 
GET method. However, POST can also be used by having the parameters included in the payload with a 
content-type set to **application/x-www-form-urlencoded**\ . 

**Parameters**

==================   ===============   =================================================================
**Request**
--------------------------------------------------------------------------------------------------------
response_type        ``required``      Fixed value: code
client_id            ``required``      Client identifier issued at the registration
redirection_uri      ``optional``      Full URL that authorization server will use to respond to request
scope                ``optional``
state                ``recommended``
**Response**
--------------------------------------------------------------------------------------------------------
code                 ``required``      Authorization Code to be used for the access token request
state                ``required``      If client puts state in the request
==================   ===============   =================================================================

Response to the request is sent to the *redirection_uri* at the client using **application/x-www-form-urlencoded** 
content-type. 

Example:
::
   GET /authorize?response_type=code&client_id=s6BhdRkqt3&state=xyz&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
   Host: server.example.com

Access Token Request
~~~~~~~~~~~~~~~~~~~~
After authorization code is successfully received, access token request can be sent to authorization server 
(or token server) for an access token. Steps 4 and 5 in figure 1 are access token request flow. Parameters 
for the access token request are as follows.

**Parameters**

==================   ===============   =================================================================
**Request**
--------------------------------------------------------------------------------------------------------
grant_type           ``required``      Fixed value: authorization_code
code                 ``required``      The authorization code received from the request.
redirection_uri      ``required``      Full URL that authorization server will use to respond to request
client_id            ``required``      If the client is not authenticating with authorization server
**Response**
--------------------------------------------------------------------------------------------------------
access_token         ``required``      Access token issued by the authorization server
token_type           ``required``      Type of the token issued
expires_in           ``recommended``   The lifetime (in sec) of the access token
refresh_token        ``optional``      Used to obtain a new access token
scope                ``optional``      
==================   ===============   =================================================================

Example
::
   POST /token HTTP/1.1
   Host: server.example.com
   Authorization: Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW
   Content-Type: application/x-www-form-urlencoded
   
   grant_type=authorization_code&code=SplxlOBeZQQYbYS6WxSbIA&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb


Refresh Token Request
~~~~~~~~~~~~~~~~~~~~~
If refresh token is available, then a request can be sent to the authorization server (or token endpoint). 
If client authentication is included, the authentication needs to be performed.

**Parameters**

==================   ===============   =================================================================
**Request**
--------------------------------------------------------------------------------------------------------
grant_type           ``required``      Fixed value: refresh_token
refresh_token        ``required``      Refresh token issued to a client.
scope                ``optional``      
**Response**
--------------------------------------------------------------------------------------------------------
access_token         ``required``      Access token issued by the authorization server
token_type           ``required``      Type of the token issued
expires_in           ``recommended``   The lifetime (in sec) of the access token
refresh_token        ``optional``      Used to obtain a new access token
scope                ``optional``      
==================   ===============   =================================================================

Example
::
   POST /token HTTP/1.1
   Host: server.example.com
   Authorization: Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW
   Content-Type: application/x-www-form-urlencoded
   
   grant_type=refresh_token&refresh_token=tGzv3JOkF0XG5Qx2TlKWIA


Accessing Resource Server
~~~~~~~~~~~~~~~~~~~~~~~~~
After authentication/authorization is (are) completed, client can put the access token in the header and 
submit the request to resource server for data. The access token is placed in the header as follows.
::
   Authorization: Bearer <access token>


Client must check the *expires_in* value. If token is expired, and refresh access token is supported, then 
client can submit the request for renew. 


Search API
==========
.. image::
   ../images/mapi_cms_to_edrs_workflow.png
   :alt: MDI to EDRS Workflow

The above diagram depicts the MDI to EDRS API workflow. And, the MAPI design will follow this workflow.
We will start with the SEARCH operation. In most states, the case is created by funeral directors. 
We will assume that the case has already been created at the EDRS with a decedent's demographics.

The basic FHIR has search API. However, the FHIR search parameters are specific to a resource. The extended
search queries are complicated. So, MAPI extended the FHIR document generation operation ($document) and 
defined search parameters that represent MDI data elements. Let's first review how MAPI extended the 
'document generation' operation. 

Extended Operation for MDI-to-EDRS Document generation
------------------------------------------------------
This is a resource instance type extended operation. It means that the MDI document is generated from the 
Composition resource. And the extension is made to the extended search parameters.

This is an idempotent operation. Both POST and GET can be used with the following endpoint URL pattern. ::

  POST [base FHIR Url]/Composition/$mdi-documents
  GET  [base FHIR Url]/Composition/$mdi-documents?name1=value1&name2=value2


**Search Parameters for the MDI Document Generation**

.. table:: Search Parameters for the MDI Document Generation Operation
    :class: tight-table
   
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|Name                  |Cardinality  |Type      |Documentation                                                                |
+======================+=============+==========+=============================================================================+
|In Parameters                                                                                                                |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|id                    |0..1         |uri       |Resource ID of Composition - MDI to EDRS                                     |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|patient               |0..*         |          |One or more decedent related search parameters                               |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|patient.birthdate     |0..1         |string    |Decedent's date of birth*                                                    |                          
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|patient.family        |0..1         |string    |Decedent's last name                                                         |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|patient.given         |0..1         |string    |Decedent's first name                                                        |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|patient.gender        |0..1         |string    |Decedent's gender                                                            |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|| edrs-file-number    || 0..1       || token   || Search by extension-tracking-numbers in                                    |
||                     ||            ||         || Composition - MDI to EDRS                                                  |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|| mdi-case-number     || 0..1       || token   || Search by extension-tracking-numbers in                                    |
||                     ||            ||         || Composition - MDI to EDRS                                                  |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|death-location        |0..1         |string    |District of death location                                                   |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|death-date-presumed   |0..1         |string    |observation.valueDateTime* (eg: gt01/01/2022T14:04:00)                       |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|death-date-pronounced |0..1         |string    |observation.component* (eg: gt01/01/2022)                                    |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|death-date            |0..1         |string    |search observation's valueDateTime* and component.pronounced date time.      |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|Out Parameters                                                                                                               |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+
|| return              || 0..1       || resource|| Searchset Bundle that includes MDI document                                |
||                     ||            ||         || bundles. If [id] is supplied, then this should be                          |
||                     ||            ||         || Bundle - Document MDI to EDRS                                              |
+----------------------+-------------+----------+-----------------------------------------------------------------------------+

\* Type for date or dateTime is defined as string for MDI-API. This is to support a `date parameter search in FHIR <https://hl7.org/fhir/r4/search.html#date>`_. The first two characters support date range search. 


Please note that the Search parameters related to patient are formatted with “.” (dot). In FHIR, this means 
that the search parameters after “.” are *part* of patient parameter in Parameters resource. 
See the example below.

.. code-block:: json-object

    {
       "resourceType":"Parameters",
       "parameter":[
          {
             "name":"patient",
             "part":[
                {
                   "name":"family",
                   "valueString":"Hans"
                },
                {
                   "name":"given",
                   "valueString":"Kennoby"
                }
             ]
          }
       ]
    }


If ``id`` is provided within URL path (e.g., /Composition/``id``/$mdi-documents), then the output response 
should be an MDI document bundle as there will be only one or zero result.

If *id* or *search paraemters* is provided in the URL parameter (e.g. [base]/Composition?name=value) 
or Parameters resource in the payload, then the output response should be a *searchset* Bundle resource 
with matching MDI document Bundle resources even if there is only one result. If “OR” search parameter 
is needed in the searching parameters, then as specified in the FHIR specification 
(https://hl7.org/fhir/R4/search.html#escaping), “,” should be used. For example, if we want to search 
records that has death-location equals to either a, b, or c, then its search parameter in Parameters
resource will be like below. ::

 “name”: "death-location",
 “valueString”: “a,b,c”

Please see the examples of search Parameters resource and its response.

**Request**

.. code-block:: json
   :caption: POST [FHIRbaseURL]/Composition/$mdi-documents
    
    {
       "resourceType":"Parameters",
       "parameter":[
          {
             "name":"patient",
             "part":[
                {
                   "name":"family",
                   "valueString":"Hans"
                },
                {
                   "name":"given",
                   "valueString":"Kennoby"
                }
             ]
          }
       ]
    }


**Response**

.. code-block:: json

    {
       "resourceType":"Bundle",
       "id":"13ab1ecf-38ce-4f47-aebb-a38396a80775",
       "type":"searchset",
       "total":1,
       "entry":[
          {
             "resourceType":"Bundle",
             "id":"fd240814-5911-49bb-bb20-72066add4a18",
             "meta":{
                "profile":[
                   "http://hl7.org/fhir/us/mdi/StructureDefinition/Bundle-document-mdi-to-edrs"
                ]
             },
             "type":"document",
             "entry":[
                {
                   "fullUrl":"Composition/965a0688-e6f4-4bff-a96d-639cbd7ea295",
                   "resource":{
                      "resourceType":"Composition",
                      "id":"965a0688-e6f4-4bff-a96d-639cbd7ea295"
                   }
                }
             ]
          }
       ]
    }
    

Error Handling
--------------
**API Level Errors**
API itself can indicate errors. API errors are displayed in the HTTP code. 2xx are returned when API 
transactions are successfully processed. 4xx or 5xx are error codes. 3xx are not errors. These codes 
need to be supported at the client side if redirections are required by the server. More details can 
be found from https://en.wikipedia.org/wiki/List_of_HTTP_status_codes. 

CMS must check if the correct endpoint and search parameters are used if such errors are returned. Server
also returns error code when there are document level errors. In this case *OperationOutcome* could be
included in the payload. CMS would want to parse the payload as it contains the source of errors. For
more information about the *OperationOutcome*, see the following section.

**MDI Document Level Errors with 2xx HTTP response**
For all non 2xx status code, error(s) must be indicated in the response with a *OperationOutcome* resource. 

In *OperationOutcome*, EDRS must be include information what caused the error if the error needs to be 
fixed by CMS. If it’s the EDRS that needs to fix the error, it must be indicated so that CMS user(s) can 
contact EDRS for the error. Below shows an example of *OperationOutcome*.

.. code-block:: json
    :caption: HTTP/1.1 500 Internal Server Error

    {
       "resourceType":"OperationOutcome",
       "id":"searchfail",
       "text":{
          "status":"generated",
          "div":"<div xmlns=\"http://www.w3.org/1999/xhtml\">\n      
            <p>The &quot;name&quot; parameter has the modifier &quot;exact&quot; which is not supported by 
            this server</p>\n</div>"
       },
       "issue":[
          {
             "severity":"fatal",
             "code":"code-invalid",
             "details":{
                "text":"The \"name\" parameter has the modifier \"exact\" which is not supported by this server"
             }
          }
       ]
    }

Read API
========

READ API URL pattern is. ::

  GET [base FHIR URL]/Composition/id/$document

``id`` is a Composition resource Id, which is assigned by a systems such as CMS and EDRS. If a server maintains
the ``id`` for all generated FHIR Document Bundles, then this ``id`` can be used get the document. In this case,
the response is a MDI document Bundle (not a *searchset* Bundle).

If additional information is needed about the base FHIR operation that MAPI operation is extended from, 
please refer to the following link.
https://www.hl7.org/fhir/composition-operation-document.html


Update API
==========
During the death investigation, C/ME may need to update the case in the EDRS. This API allows CMS to update
the active case. PUT should be used for the HTTP action method. And, Parameters resource is used to include
the MDI document that C/MEs want to update. Since this API presumes that the case already exists in the
EDRS, the case management system must either make sure identifier(s) is included in the MDI document or 
provide a parameter that EDRS can use to find the case to update.

UPDATE API operations and requirement are as follows. ::

  PUT [base url]/Composition/$update-mdi
  Payload = Parameters resource


Input/Output Parameters

+------------------------+-------------+-----------------------------+-----------------------------------+
| Name                   | Cardinality | Type                        | Documentation                     |
+========================+=============+=============================+===================================+
| In Parameters                                                                                          |
+------------------------+-------------+-----------------------------+-----------------------------------+
| ``Jurisdiction defined | 0..*        | string                      | Any required parameters for a     |
| parameters``           |             |                             | jurisdiction                      |
+------------------------+-------------+-----------------------------+-----------------------------------+
| edrs-file-number       | 1..1        | string                      | EDRS case number if available     |
+------------------------+-------------+-----------------------------+-----------------------------------+
|| mdi-document          || 1..1       || Bundle                     || MDI document bundle. The         |
||                       ||            ||                            || “mdi-document” is a reserved     |
||                       ||            ||                            || keyword. This should only be     |
||                       ||            ||                            || used for the MDI to EDRS         |
||                       ||            ||                            || profile bundle document.         |
+------------------------+-------------+-----------------------------+-----------------------------------+
| Out Parameters                                                                                         |
+------------------------+-------------+-----------------------------+-----------------------------------+
|| return                || 0..1       || OperationOutcomeParameters || If an error occurs, OO resource  |
||                       ||            ||                            || is returned. If response data    |
||                       ||            ||                            || need to be sent back,            |
||                       ||            ||                            || Parameters resource can be used. |
+------------------------+-------------+-----------------------------+-----------------------------------+

Ex. **Request** in the payload

.. code-block:: json

    {
       "resourceType":"Parameters",
       "parameter":[
          {
             "name":"edrs-file-number",
             "valueString":"1234"
          },
          {
             "name":"jurisdiction defined key",
             "valueString":"value"
          },
          {
             "name":"mdi-document",
             "resource":{
                "MDI document bundle here "
             }
          }
       ]
    }

*In Parameters* include parameters that can be used for search and MDI document that has updated information. 
UPDATE API allows custom local search parameters. If there are local search parameters that are required
for the case search, the local search parameters can be defined in the Parameters resource. In the table 
above, this is labeled as ``Jurisdiction defined parameters``. It can be any name and type. However, any 
parameter created by this method would only be supported by systems that can understand the parameter. If 
*Jurisdiction defined parameters* exist but cannot be understood, they should be ignored and NOT cause 
an error.

The MDI document in the search parameter, *mdi-document*, needs to conform to MDI IG profiles.  It is 
not required to include all the data elements in the MDI docvument. Only data elements that need to be 
updated can be included. At the EDRS, empty data elements or missing elments should not be understood as 
DELETE. They should be understood as '*Not Applicable*/. Deleting cases or data elements wihtin a case 
should be handled in a separate API (i.e. DELETE API).

If CMS decided to use the attached MDI document to include search parameters, it is recommended to use
identifier extension(s) in the Composistion resource located in the MDI document entry. MDI IG defines 
tracking numbers in the extended identifiers. Thus, this can be used for searching.

The response for a successful UPDATE API should be 200 OK. The payload is not required. If 
EDRS or CMS needs some data with the response, the Parameters resource can be used. Jurisdiction and 
C/ME office can use the same parameters as *In Parameters* parameters. If the submitted MDI document will 
be included in the response body, then “mdi-document” parameter key should be used. If the API operation was 
successful, but there were some warnings that EDRS wants to send back to CMS, then parameter name 
should be “warning”. And, “resource” should be used to include OperationOutcome resource. If the API 
operations were failed, then the response should be OperationOutcome resource with a HTTP error code. 
Please see the example of response below. 

Ex. **Response** if the operation was successful, and EDRS wanted to respond with updated data.

.. code-block:: json

   {
      "resourceType":"Parameters",
      "parameter":[
         {
            "name":"jurisdiction defined key1",
            "valueString":"value1"
         },
         {
            "name":"jurisdiction defined key2",
            "valueString":"value2"
         },
         {
            "name":"mdi-document",
            "resource":{
               "MDI document bundle"
            }
         },
         {
            "name":"warning",
            "resource":{
               "OperationOutcome resource"
            }
         }
      ]
   }


**Response** if error occured.

.. code-block:: json

    {
       "resourceType":"OperationOutcome",
       "id":"searchfail",
       "text":{
          "status":"generated",
          "div":"<div xmlns=\"http://www.w3.org/1999/xhtml\">\n      <p>The &quot;case number&quot; 1234 does not exist</p>\n    </div>"
       },
       "issue":[
          {
             "severity":"fatal",
             "code":"case-invalid",
             "details":{
                "text":"The \"case number\" 1234 does not exist."
             }
          }
       ]
    }

