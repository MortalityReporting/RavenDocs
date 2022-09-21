.. _record-management:

Record Management
=================

Importing MDI Records
---------------------
Case Importing is a Raven 2.0 feature that imports the Comma-separated Values (CSV) or spreadsheet file into the MDI FHIR server in an MDI FHIR IG compliant format.  
  
The FHIR data model is complicated and structured with multi-levels and logical references. In order to help transitioning from non-FHIR data to MDI IG compliant format, the MDI CSV format was designed. The Case Importing feature maps the pre-defined MDI CSV format to the MDI FHIR IG format and persists them in the MDI FHIR server. 

## MDI FHIR Document Bundle
## Spreadsheet Schema

Viewing Cases
-------------
The Case Viewer is a UI Component which allows the browsing and viewing of Raven FHIR Server records, encompassing both MDI Case Documents (MDI to EDRS) and Toxicology Reports (LIMS to MDI). In addition to providing a user-friendly option for viewing the data present on the FHIR Server, the layout is structured from the perspective of the MDI Implementation Guide to serve as an educational tool to better understand the data structure and fields which make up the MDI to EDRS and Toxicology to MDI documents. 
  
The Case Viewer also features a FHIR Resource Explorer, which allows users to select a field and see the underlying FHIR Resource structure containing the related data. The FHIR Resource Explorer will support JSON and XML formats, as well as a human readable “narrative view”. 

## Searching Cases
## Case Summary
## Toxicology Report Summary