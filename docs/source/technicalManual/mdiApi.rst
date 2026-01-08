.. _mdiAPI:

=======================
Standard MDI API (MAPI)
=======================

.. note::
   Standard MDI API (MAPI) will be documented as a best practice in the MDI IG site in the future. 
   Until then, the Raven documentation will temporarily house the standard MAPI specification.
    
Operation APIs for MDI-to-EDRS Workflow
=======================================
MDI FHIR Implementation Guide (IG) is available in http://hl7.org/fhir/us/mdi/  This 
IG should be used for the payload of MAPI.
 
FHIR defines base restful APIs for FHIR data transportation. Their documents are available 
from https://hl7.org/FHIR/http.html. And, the FHIR API Operations are documented 
in https://hl7.org/FHIR/operationslist.html. MAPI is extended the FHIR ASPI operations. 
Therefor, the basic rules of FHIR APIs and operations are also applied to MAPI. For example,

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
|Role                   |Responsibility                                                       | MDI-and-EDRS|  Tox-and-MDI |
+=======================+=====================================================================+=============+==============+
| Authorization Server  | Server that authenticates the resource owner and issues access      | EDRS        | CMS          |
|                       | tokens to the client application. The authorization server can be   |             |              |
|                       | the same as the authentication server or can be a separate server.  |             |              |
+-----------------------+---------------------------------------------------------------------+-------------+--------------+
| Client                | Application that wants to access the resource on behalf of the      | CMS         | LIMS         |
|                       | resource owner. The client can be a web application, a mobile       |             |              |
|                       | application, or a desktop application.                              |             |              |
+-----------------------+---------------------------------------------------------------------+-------------+--------------+
| Resource Owner        | User who owns the resource (such as a photo or a document) that     | CMS Users   | LIMS Users   |
|                       | a client application wants to access. The resource owner grants     | EDRS Users  |              |
|                       | permission to the client application to access the resource.        |             |              |
+-----------------------+---------------------------------------------------------------------+-------------+--------------+
| Resource              | Server that hosts the resource that the client application wants    | EDRS        | CMS          |
| Server (Provider)     | to access. The resource server verifies the access token and        |             |              |
|                       | grants access to the resource if the token is valid.                |             |              |
+-----------------------+---------------------------------------------------------------------+-------------+--------------+

**Table1**\ : Roles in OAuth2 and MDI Systems


OAuth2 Flows
^^^^^^^^^^^^
OAuth2 defines different flows based on the client (or application) types. This document only discusses 
the flow(s) that might be applicable to the client types in MDI. Figure 1 depicts the authorization code 
flow that can provide authentication and authorization of clients in MDI workflows. Detail transactions 
for the authorization code flow are explained in section `4.1 <https://www.rfc-editor.org/rfc/rfc6749#section-4.1>`_ of `RFC 6749 <https://www.rfc-editor.org/rfc/rfc6749>`_.

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
client can submit the request to renew the access token (see sections above related to the requests). 

Error Handling
~~~~~~~~~~~~~~
If error occurs during authorization, the server should respond as specified in `5.2 <https://www.rfc-editor.org/rfc/rfc6749#section-5.2>`_ of `RFC 6749 <https://www.rfc-editor.org/rfc/rfc6749>`_.
In summary, the response should be 400 (Bad Request) status code (unless specified otherwise) with the 
following parameters.

**Error Parameters**\ :

+------------------------------------------------------------------------------------------------------------------------+
| **Key**                                                                                                                |
+-------------------------+----------------+-----------------------------------------------------------------------------+
| error                   |``required``    | A single ASCII error code from the following values:                        |
+-------------------------+----------------+-----------------------------------------------------------------------------+
| **Values**                                                                                                             |
+-------------------------+----------------------------------------------------------------------------------------------+
|| invalid_request        || The request is missing a required parameter, includes an unsupported parameter value        |
||                        || (other than grant type), repeats a parameter, includes multiple credentials, utilizes       |
||                        || more than one mechanism for authenticating the client, or is otherwise malformed.           |
+-------------------------+----------------------------------------------------------------------------------------------+
|| invalid_client         || Client authentication failed (e.g., unknown client, no client authentication included,      |
||                        || or unsupported authentication method).  The authorization server MAY return an HTTP 401     |
||                        || (Unauthorized) status code to indicate which HTTP authentication schemes are supported.     |
||                        || If the client attempted to authenticate via the "Authorization" request header field,       |
||                        || the authorization server MUST respond with an HTTP 401 (Unauthorized) status code and       |
||                        || include the "WWW-Authenticate" response header field matching the authentication scheme     |
||                        || used by the client.                                                                         |
+-------------------------+----------------------------------------------------------------------------------------------+
|| invalid_grant          || The provided authorization grant (e.g., authorization code, resource owner credentials)     |
||                        || or refresh token is invalid, expired, revoked, does not match the redirection URI used      |
||                        || in the authorization request, or was issued to another client.                              |
+-------------------------+----------------------------------------------------------------------------------------------+
|| unauthorized_client    | The authenticated client is not authorized to use this authorization grant type.             |
+-------------------------+----------------------------------------------------------------------------------------------+
| unsupported_grant_type  | The authorization grant type is not supported by the authorization server.                   |
+-------------------------+----------------------------------------------------------------------------------------------+
| invalid_scope           || The requested scope is invalid, unknown, malformed, or exceeds the scope granted by the     | 
|                         || resource owner.                                                                             |
+-------------------------+----------------------------------------------------------------------------------------------+
| Values for the "error" parameter MUST NOT include characters outside the set %x20-21 / %x23-5B / %x5D-7E.              |
+-------------------------+----------------+-----------------------------------------------------------------------------+
| **Key**                                                                                                                |
+-------------------------+----------------+-----------------------------------------------------------------------------+
|| error_description      || ``optional``  || Human-readable ASCII text providing additional information, used to assist | 
||                        ||               || the client developer in understanding the error that occurred. Values for  |
||                        ||               || the"error_description" parameter MUST NOT include characters outside the   |
||                        ||               || set %x20-21 / %x23-5B / %x5D-7E.                                           |
+-------------------------+----------------+-----------------------------------------------------------------------------+
|| error_uri              || ``optional``  || A URI identifying a human-readable web page with information about the     |
||                        ||               || error, used to provide the client developer with additional information    |
||                        ||               || about the error. Values for the "error_uri" parameter MUST conform to the  |
||                        ||               || URI-reference syntax and thus MUST NOT include characters outside the set  |
||                        ||               || %x21 / %x23-5B / %x5D-7E.                                                  |
+-------------------------+----------------+-----------------------------------------------------------------------------+


Example
::

   HTTP/1.1 400 Bad Request
   Content-Type: application/json;charset=UTF-8
   Cache-Control: no-store
   Pragma: no-cache
   
   {
      "error":"invalid_request"
   }


Search API
==========
.. image::
   ../images/mapi_cms_to_edrs_workflow.png
   :alt: MDI to EDRS Workflow

The above diagram depicts the MDI to EDRS API workflow. MAPI design follows this workflow.
We will start with the SEARCH operation. In most states, the case is created by funeral directors. 
For this document, we assume that the case has already been created at the EDRS with decedent's demographics.

The FHIR defines basic search API. However, the FHIR search parameters are specific to a resource. The extended
search queries are complicated. So, MAPI extended the FHIR document generation operation ($document) and 
defined search parameters that represent MDI data elements. Details about the base $document operation is described
in https://www.hl7.org/fhir/composition-operation-document.html

Let's first review how MAPI extended the $document operation. 

Extended Operation for MDI-to-EDRS Document Generation
------------------------------------------------------
This is a resource instance type extended operation. It means that the MDI document is generated from the 
Composition resource. And the extension is made to the extended search parameters.

This is an idempotent operation. Both POST and GET can be used with the following endpoint URL pattern. ::

  POST [base FHIR Url]/Composition/$document with Parameters resource in the payload
  GET  [base FHIR Url]/Composition/$document?name1=value1&name2=value2


**Search Parameters for the MDI Document Generation**
   
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|Name                  |Cardinality  |Type            |Documentation                                                                                      |
+======================+=============+================+===================================================================================================+
|In Parameters                                                                                                                                            |
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|id                    |0..1         |uri             |Composition.id of Composition - MDI to EDRS                                                        |
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|tracking-number       |0..1         |token           |Composition.extension:extension-tracking-number of Composition - MDI and EDRS                      |
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|patient\ :sup:`1`     |0..1         |                |One or more decedent related search parameters                                                     |
+--+-------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|  | patient.birthdate |0..*         |date\ :sup:`2`  |Decedent's date of birth                                                                           |                          
+--+-------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|  | patient.family    |0..*         |string          |Decedent's last name                                                                               |
+--+-------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|  | patient.given     |0..*         |string          |Decedent's first name                                                                              |
+--+-------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|  | patient.gender    |0..*         |token           |Decedent's gender                                                                                  |
+--+-------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|death-location        |0..1         |string          |Location address in Location-death                                                                 |
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|death-date-pronounced |0..1         |date\ :sup:`2`  |Observation.component:datetimePronouncedDead in Observation - Death Date (either time or dateTime) |
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|death-date            |0..1         |date\ :sup:`2`  |Value[x] (actual or presumed date of death) in Observation - Death Date (either dateTime or Period)|
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|| manner-of-death     || 0..1       || string        || Manner of death code. code must be from the specified valueset\ :sup:`3` as described below.     |
||                     ||            ||               ||   38605008, Natural death                                                                        |
||                     ||            ||               ||   7878000, Accidental death                                                                      |
||                     ||            ||               ||   44301001 Suicide                                                                               |
||                     ||            ||               ||   27935005, Homicide                                                                             |
||                     ||            ||               ||   185973002, Patient awaiting investigation                                                      |
||                     ||            ||               ||   65037004, Undetermined manner of death                                                         |
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|Out Parameters                                                                                                                                           |
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+
|| return              || 0..1       || resource      || Bundle - Searchset or Bundle - Document MDI and EDRS. If [id] is supplied,                       |
||                     ||            ||               || then this should be Bundle - Document MDI and EDRS                                               |
+----------------------+-------------+----------------+---------------------------------------------------------------------------------------------------+

.. note::
   \1 The *search parameters* for **patient** are formatted with “.” (dot). In FHIR, this means that the search parameters 
   after “.” are ``part`` of patient parameter in Parameters resource. See the example below.

   \2 `date parameter search in FHIR <https://hl7.org/fhir/r4/search.html#date>`_ uses first two characters for date range search 
   (eg. "lt" for less than). To use the *date range search*, the ``Type`` needs to be string.   

   \3 Manner of death code in FHIR: https://hl7.org/fhir/us/vrdr/ValueSet-vrdr-manner-of-death-vs.html

Example of a patient parameter

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


If ``id`` is provided within URL path (e.g., /Composition/``id``/$document), then the output response 
should be an MDI document bundle as there will be only one or zero result.

If *id* or *search paraemters* is provided in the URL parameter (e.g. [base]/Composition?name=value) 
or Parameters resource in the payload, then the output response should be a *searchset* Bundle resource 
with matching MDI document Bundle resources even if there is only one result. If “OR” search parameter 
is needed in the searching parameters, then as specified in the FHIR specification 
(https://hl7.org/fhir/R4/search.html#escaping), “,” should be used. For example, if we want to search 
records that has death-location equals to either a, b, or c, then its search parameter in Parameters
resource will be like below. ::

 "name”: "death-location",
 "valueString": "a,b,c"

Please see the examples of search Parameters resource and its response.

**Request**

.. code-block:: json
   :caption: POST [FHIRbaseURL]/Composition/$document
    
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

READ API uses the base FHIR operation $document. The URL pattern is. ::

  GET [base FHIR URL]/Composition/id/$document

``id`` is a Composition resource Id, which is assigned by systems such as CMS and EDRS. If a server maintains
the ``id`` for all generated FHIR Document Bundles, then this ``id`` should be used to get the document.
The response for this API is a MDI document Bundle (not a *searchset* Bundle).

Update API
==========
During the death investigation, C/ME may need to update the case in the EDRS. This API allows CMS to update
the active case. PUT should be used for the HTTP action method. And, Parameters resource is used to include
the MDI document or profile(s) that C/MEs want to update. Since this API presumes that the case already exists 
in the EDRS, the case management system must either make sure identifier(s) is included in the MDI document or 
provide a parameter that EDRS can use to find the case to update.

FHIR endpoint for UPDATE API operations is as follow. ::

  PUT [base url]/Composition/$update-mdi

The payload is Parameters resource as defined below.

Input/Output Parameters

+------------------------+-------------+-----------------------------+-----------------------------------+
| Name                   | Cardinality | Type                        | Documentation                     |
+========================+=============+=============================+===================================+
| In Parameters                                                                                          |
+------------------------+-------------+-----------------------------+-----------------------------------+
| ``Jurisdiction defined | 0..*        | string                      | Any required parameters for a     |
| parameters``           |             |                             | jurisdiction                      |
+------------------------+-------------+-----------------------------+-----------------------------------+
| tracking-number        | 1..1        | token                       | EDRS case number if available     |
+------------------------+-------------+-----------------------------+-----------------------------------+
| mdi-document           | 1..1        | Bundle                      | MDI document bundle. The          |
|                        |             |                             | “mdi-document” is a reserved      |
|                        |             |                             | keyword. This should only be used |
|                        |             |                             | for the MDI-and-EDRS profile      |
|                        |             |                             | bundle document.                  |
+------------------------+-------------+-----------------------------+-----------------------------------+
| warning                | 1..1        | OperationOutcome            | Informational OperationOutcome    |
|                        |             |                             | (For response ONLY)               |
+------------------------+-------------+-----------------------------+-----------------------------------+
| Out Parameters                                                                                         |
+------------------------+-------------+-----------------------------+-----------------------------------+
| return                 | 0..1        | OperationOutcome            | If an error occurs, OO resource   |
|                        |             |                             | is returned. If response data     |
|                        |             |                             | need to be sent back,             |
|                        |             |                             | Parameters resource can be used.  |
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
                [Your MDI document bundle goes here in JSON or XML.]
             }
          }
       ]
    }

*In Parameters* includes parameters that can be used for the update operation. 

UPDATE API allows custom parameters (labeled as ``Jurisdiction defined parameters``). They are locally
defined parameters. It can be used in any ways by the systems that defined the parameters. 
If *Jurisdiction defined parameters* exist but cannot be understood, they should be ignored and 
should NOT cause any error.

The *mdi-document*, is a death certificate document in MDI FHIR IG. If CMS is updating the complete death 
certificate, then all the required data elements should exist in the docvument. 

Partial document is allowed if CMS needs to update only portion of death certificate document. However, 
to conform to MDI FHIR IG, any empty required fields must be extended to include data-absent-reason extension.

The response for a successful UPDATE API should be 200 OK. The payload is not required in the response. 
If EDRS or CMS needs to respond with some data in the response, the Parameters resource can be used. 
EDRS and CMS can use the same parameters as *In Parameters* parameters. If the submitted document will 
be included in the response body, then “mdi-document” parameter key should be used. 

If the API operation was successful, but there were some warnings that EDRS wants to send back to CMS, 
then parameter key, “warning”, should be used. And, “resource” should be used to include OperationOutcome 
resource. If the API operations were failed, then the response should be OperationOutcome resource with a 
HTTP error status code. Please see the example of response below. 

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

Update using FHIR Messaging
---------------------------
If a messaging infrastructure is already in place, or if the content needs to be forwarded to another endpoint, 
it may be necessary to handle the target endpoint differently, given that the FHIR receiving endpoint is not the 
actual target. If this direction is deemed appropriate, the FHIR `process-message` operation 
(https://hl7.org/fhir/R4/messageheader-operation-process-message.html) can be employed.

If the decision is to utilize the `process-message` operation, the payload should take the form of a bundle, 
with the initial entry being a `MessageHeader` resource. Subsequent to this entry, parameters must be present, 
adhering to the specifications outlined in the Update API.