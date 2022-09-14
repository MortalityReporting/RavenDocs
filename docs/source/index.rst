Welcome to the Raven Platform documentation! 
============================================

This wiki exists as a guide to help users understand 
the Raven mortality platform, providing
both end-user manuals as well as technical documentation for items such
as data schema.

What is Raven?
--------------

Raven is an open-source, proof-of-concept platform that serves as a reference implementation and provides testing tools for interoperability between case management systems (CMS) and other external actors. The external actors are those data sources with which CMS need to communicate to exchange Medicolegal Death Investigation (MDI) data, and may include, but not be limited to, electronic death registration systems (EDRS) and forensic toxicology laboratory information management systems (LIMS).

The current Raven tooling and tests aid developers in implementing the MDI FHIR record format by validating FHIR messages against MDI IG guidelines and FHIR-based extended API operations. Tools included in the Raven 2.0 platform are as follows, 

- Workflow Simulator:
  The workflow simulator is an end-to-end framework that manages the project workstreams. Individual components under the Project Workstreams are composed 
  in the workflow simulator.    
- Case Importing:
  Case Importing is a Raven 2.0 feature that imports the Comma-separated Values (CSV) or spreadsheet file into the MDI FHIR server in an MDI FHIR IG 
  compliant format.  
  
  The FHIR data model is complicated and structured with multi-levels and logical references. In order to help transitioning from non-FHIR data to MDI IG 
  compliant format, the MDI CSV format was designed. The Case Importing feature maps the pre-defined MDI CSV format to the MDI FHIR IG format and persists 
  them in the MDI FHIR server. 
- Validate & Compare: The MDI (Medicolegal Death Investigation) Validator is a web application that allows users to upload or copy-paste their MDI FHIR IG 
  data for validation. The MDI Validator uses the HL7 FHIR validator as a core validation engine and provides a user interface (UI) wrapper that is 
  tailored to the MDI IG.  
  
  The Comparison Tool is a connectathon supporting tool that will compare pre-validated test case MDI FHIR IG data with the user generated FHIR data. Users 
  will want to ensure that not only their data validated but also their contents in FHIR correctly populated. The Comparison Tool will provide a compressed 
  case view with side by-side comparison of the imported record and the correct test case record. This will let users easily hone in on individual content 
  issues and have confidence in their process. 
- Case Viewer: The Case Viewer is a UI Component which allows the browsing and viewing of Raven FHIR Server records, encompassing both MDI Case Documents 
  (MDI to EDRS) and Toxicology Reports (LIMS to MDI). In addition to providing a user-friendly option for viewing the data present on the FHIR Server, the 
  layout is structured from the perspective of the MDI Implementation Guide to serve as an educational tool to better understand the data structure and 
  fields which make up the MDI to EDRS and Toxicology to MDI documents. 
  
  The Case Viewer also features a FHIR Resource Explorer, which allows users to select a field and see the underlying FHIR Resource structure containing 
  the related data. The FHIR Resource Explorer will support JSON and XML formats, as well as a human readable “narrative view”. 
- Raven/Bluejay FHIR Servers: Raven/Bluejay FHIR server is developed to persist MDI FHIR Data and provide the data using FHIR APIs and extended operations. 
  Raven/Bluejay FHIR server includes support for the MDI IG. 

For more information on each Raven tool components, Raven’s MDI CSV schema, or
FHIR MDI standard please see the corresponding
sections in this wiki, accessible through the table of contents below or
the sidebar navigation menu.

Table of Contents
=================


.. toctree::

   architecture
   fhir
   mdi
   userManual
   deployment

Raven is released under the `Apache License
2.0 <https://github.com/MortalityReporting/raven-platform/blob/main/LICENSE>`__.

.. note::

   -  All data shown is synthetic for demonstration purposes only and does
      not represent actual cases or decedents.*
   -  Screenshots may be taken from earlier internal versions of Raven and
      may not be 100% accurate to the final release.*

   If you find an error in the wiki, please go to the `contact
   page <https://github.com/MortalityReporting/raven-platform/wiki/Development-Team>`__ and let us know!

