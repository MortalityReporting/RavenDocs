Workflow Simulator
==================
The Workflow Simulator is a modular component of the Raven Testing Tool that enables users to simulate 
data flows coming into their MDI systems as it relates to FHIR adoption. The simulator also provides users 
clear indicators and metrics to help them make decisions on where to spend their resources as they rebuild 
for modernization and interoperability within their data ecosystems. 

Architecture
------------
This would be a module within the Raven Platform or could be used independent of Raven for testing and metrics.
The following diagram depicts what can be achieved with the collection of modules in staged views. Please note 
that this is not to be considered a strictly technical architecture diagram for development purposes, and is 
only intended to demonstrate a high level view of the functionality of the system as relates to the physical 
layout of components, connection to external end points, and the users’ scope.

.. image:: 
   ../images/Raven20Diagram.png
   :alt: Raven Overview Diagram
   
The workflow simulator is an end-to-end framework that manages the project workstreams. Individual components 
under the Project Workstreams are modularly composed in the workflow simulator.


Use Cases/Workflows
-------------------
Documentation under development

CMS to EDRS
^^^^^^^^^^^
  Step 1 - Import/Select Record

  Step 2 - Validate/Compare

  Step 3 - Configure Endpoint

  Step 4 - API Interaction (Submit)
