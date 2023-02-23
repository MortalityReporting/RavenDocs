Workflow Simulator
==================
The Workflow Simulator is a module of the Raven platform that allows users to simulate data flows between Medicolegal Death Investigation (MDI)
systems such as case management systems (CMS), electronic death registration systems (EDRS), and toxicology laboratory information systems (LIMS).
The supported data flows are defined by interoperability use cases. There are two types of established use cases: Testing Use Cases and
Operational Use Cases.   

1. Testing Use Cases: Use cases that are developed for testing events to evaluate the interoperability implementation of MDI systems  
2. Operational Use Cases: Use cases that are defined by users in the MDI community to standardize the operations such as search, update,
 certification, amendment, or messaging.  

Some testing use cases can be supported by individual Raven modules such as the FHIR Validator and Record Comparison modules. Operational
use cases, which are often more complex, such as the Search EDRS API workflow, can be implemented as a proof-of-concept using the Workflow
Simulator prior to production development. Thus, users can use the Workflow Simulator as clear indicators and metrics to help making decisions
on where to spend their resources as they rebuild for modernization and interoperability within their data ecosystems.  


Workflows/Use Cases
-------------------
When opening the Workflow Simulator module, the user will be given a list of currently implemented workflows
to select from. Once selected, the workflow will be loaded, presented as a step by step process in Raven.

.. image:: 
   ../images/workflow-simulator/workflow-list.png
   :alt: Raven Overview Diagram

Search EDRS (CMS to EDRS)
^^^^^^^^^^^^^^^^^^^^^^^^^
Step 1 - Import/Select Record (Optional)

The first step of the Search EDRS workflow allows the user to select an MDI to EDRS Document from the Raven FHIR Server to use to auto
populate search parameters with the values from the record. Users may also import a record into the workflow as an MDI to EDRS Document
Bundle in the FHIR JSON format. This step is entirely optional, and if a user wishes to proceed without a case select they can
manually input all search parameters required.

.. image:: 
   ../images/workflow-simulator/search-edrs-step1a.png
   :alt: Select MDI to EDRS Document

.. image:: 
   ../images/workflow-simulator/search-edrs-step1b.png
   :alt: Import MDI to EDRS Document Bundle JSON


Step 2 - Configure Endpoint

After the user decides on whether they would like to use an existing record, they are taken to the Configure Endpoint step. This part of
workflow is the configuration of the FHIR endpoint for testing the search functionality against an Electronic Death Registration System (EDRS).
Users may select between a pre-registered Endpoint or a Custom Endpoint. Pre-registered endpoints are configured in Raven and will typically
provide open testing endpoints, including the Raven BlueJay server which acts as a test EDRS. Selecting a pre-registered endpoint requires no
additional configuration from the user. For custom endpoints, users may provide a non-registered testing endpoint and setup basic authorization
as needed. Custom endpoints are not recorded in any form by the Raven platform, and their use is entirely the responsibility of the user.
Please note that the Raven platform is a single page application based in a web browser, and using custom endpoints may result in the user's
browser recording sensitive information separate from the Raven platform. (This should be managed by the user in coordination with their
organization's internal IT policies.)

.. image:: 
   ../images/workflow-simulator/search-edrs-step2.png
   :alt: Configure Endpoint


Step 3 - Search EDRS (API Interaction)

The final step of the Search EDRS workflow is the execution of search parameters against the identified EDRS endpoint. The potential parameters
fields are data driven and populated automatically based on the FHIR MDI Implementation Guide "MDI Documents" Operation Definition. Users may
select any number of parameter fields they wish to use. If a record was selected or imported during step 1, the parameters will attempt to have
their values automatically populated. As the user enters data or modifies the parameter fields, an example of the FHIR Parameters resource is
shown for demonstration purposes which matches the current state of the parameters HTML form. This allows users building reference
implementations a model to which they can refer in their own development, tying a standard HTML style form to the underlying FHIR resource it
will produce. Once satisified with their search parameters, users may connect to the EDRS and attempt to find matching records.

.. image:: 
   ../images/workflow-simulator/search-edrs-step3a.png
   :alt: Search EDRS Parameters

If records are identified on the EDRS, the results are shown below the parameters. The results can be viewed either as a human readable table
summarizing the matching records, or as a raw FHIR search set bundle. In addition, users can use the HTTP Request and Response tabs to better
be able to identify the headers involved in the HTTP call to the EDRS. In the summary table under the default Results tab, a record may be
selected to load further information.

.. image:: 
   ../images/workflow-simulator/search-edrs-step3b.png
   :alt: Search Results


Once selected in the Results table, the record is displayed below the table. As with the full search results, this can be viewed either as a
human readable summary and as the underyling FHIR MDI to EDRS Document Bundle

.. image:: 
   ../images/workflow-simulator/search-edrs-step3b.png
   :alt: Result Record Summary


