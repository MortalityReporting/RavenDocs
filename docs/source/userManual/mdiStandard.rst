.. _mdiStqandard:

The MDI Standard
================

What is *FHIR*?
---------------

`HL7 Fast Healthcare Interoperability Resources
(FHIR) <http://hl7.org/fhir/>`__ is a successor to HL7’s earlier
industry standards healthcare messaging, HL7v2.x and HL7v3.x. It builds
upon those standards to produce a modern interoperability standard,
enabling the easy exchange of healthcare records across systems.

FHIR is built around the concept of “Resources”, logically distinct
entities that serve as the minimum granularity for transfer. For
example, the Patient resource represents core patient demographic data
and serves a focal reference for many other resources. Other resources
include clinical concepts such as Condition or an Observation.

FHIR is currently up to its R5 release, though R4 is still the most
prevalent of the modern releases and continues to be the release in
which most development is focused. For a complete list of FHIR R4
Resources and their respective maturities, please see the `FHIR R4
Resource List <https://hl7.org/fhir/R4/resourcelist.html>`__.

What is *MDI IG*?
-----------------

The `Medicolegal Death Investigation (MDI) Implementation Guide (IG) <http://build.fhir.org/ig/HL7/fhir-mdi-ig/>`__ is a FHIR
implementation guide detailing the proper method of using FHIR resources
to construct a FHIR version of a Death and Toxicology Reporting. The MDI standard is
developed to support modernization of interoperability between Coroner/Medical Examiner case management systems (CMS) 
and other systems such as Electronic Death Registrar Systems (EDRS) and Toxicology Lab Information and Management System (LIMS).

The Raven Platform uses the MDI IG for handling death
records, importing MDI data and exporting to FHIR resources. 
The Raven Platform allows users to import their own data into
FHIR MDI resources and store them on the Raven FHIR Server.

MDI IG is still in the draft version and being updated based on the HL7 FHIR IG development cycles. 
MDI IG developers are adapting VRDR data elements if data concepts are overlapped instead of creating
new ones so that the transitions can be achieved smoothly. Data elements that exist in IJE but not needed in MDI 
are not included while data elements that are required in MDI are included. MDI IG developer group encourages the
MDI community to actively participate in providing their needs, adapting the MDI IG, and testing in Raven platform.

For a more detailed breakdown of MDI contents, please see the `official
MDI Implementation Guide <http://build.fhir.org/ig/HL7/fhir-mdi-ig/background.html>`__.

Overview of MDI Workflows 
-------------------------

Currently, two workflows are defined in the MDI IG, MDI-to-EDRS and Toxicology-to-MDI. The MDI IG defines
required content structures for the workflows. In order to achieve successful interoperability,
each participating system MUST follow and conform to the MDI IG.

MDI-to-EDRS
^^^^^^^^^^^
MDI-to-EDRS workflow represents the interoperability between MDI case management system (CMS) and 
state's electronic death registration system (EDRS). As it happens in most states,
the case is mostly created by funeral directors. Thus, this workflow begins with an initial case created at 
the EDRS. CMS first searches EDRS for a case and retrieves the case with limited decedent's demographics. 
CMS may update the case during the journey of the death investigation. When the investigation is completed,
the case shall be certified and submitted to EDRS. 

In this workflow, users can validate the MDI-to-EDRS FHIR bundle documents, load the documents, and submit to EDRS.
It's highly recommended for users to first validate the FHIR data before loading to Raven. For those who do not
have their own dataset or are not ready to produce the dataset, Raven allows users to search the Raven FHIR Server, 
load the case and play with the case. Users can explore the raw FHIR data along with the rendered data in forms.

Toxicology-to-MDI
^^^^^^^^^^^^^^^^^
Toxicology-to-MDI workflow represents the interoperability between forensic toxicology laboratory information 
management system (LIMS) to an MDI case management system (CMS). The workflow is bidirectional. There is an
inital lab order sent from CMS with samples. After lab work is performed, the lab report is sent back to 
CMS from LIMS. In this workflow, FHIR messaging is used for the data exchanges.

Users can validate the Toxicology-to-MDI FHIR bundle messages and load the messages. Toxicology case viewer and 
API operations are work-in-progress. 
