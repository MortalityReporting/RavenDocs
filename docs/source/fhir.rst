.. _fhir:

FHIR
====

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

FHIR MDI Resources
------------------

The `Medicolegal Death Investigation (MDI)
Implementation Guide <http://build.fhir.org/ig/HL7/fhir-mdi-ig/>`__ is a FHIR
implementation guide detailing the proper method of using FHIR resources
to construct a FHIR version of a Death and Toxicology Reporting. The MDI standard is
developed to support modernization of interoperability between Coroner/Medical Examiner systems (CMS) 
and other systems such as Electronic Death Registrar Systems (EDRS) and Toxicology Lab Information and Management System (LIMS).

The Raven Platform uses the MDI IG for handling death
records, allowing importing MDI data and exporting to FHIR resources. 
The Raven Platform allows users to import their own data into
FHIR MDI resources and store them on the Raven FHIR Server.

MDI IG is still in the draft version ann being updated based on the HL7 FHIR IG development cycles. 
MDI IG developers are adapting VRDR data elements if data concepts are overlapped instead of creating
new ones so that the transitions can be achieved smoothly. Data elements that exist in IJE but not needed in MDI 
are not included while data elements that are required in MDI are included. MDI IG developer group encourages
MDI community to actively participate in providing their needs, adapting the MDI IG, and testing in Raven platform.

For a more detailed breakdown of MDI contents, please see the `official
MDI Implementation Guide
 <http://build.fhir.org/ig/HL7/fhir-mdi-ig/background.html>`__.
