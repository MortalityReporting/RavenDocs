.. _mdiStandard:

The MDI Standard
================

What is *FHIR*?
---------------

`HL7 Fast Healthcare Interoperability Resources
(FHIR) <http://hl7.org/fhir/>`__ is a successor to HL7’s earlier
industry standards for healthcare messaging, including HL7v2.x and HL7v3.x.
It builds upon previous standards to produce a modern interoperability
standard designed around RESTful APIs, providing more advanced exchange
of healthcare records across systems.

FHIR is built around the concept of “Resources”, logically distinct
entities that typically serve as the minimum level of data granularity
for data exchange. For example, the Patient resource represents core
patient demographic data and serves as a focal reference for many other
resources. Other resources include clinical concepts such as a Condition
or an Observation (e.g., Lab Results).

FHIR R4 (4.0.1) is the most widely adopted version of FHIR, though HL7
has published up to version R5, with R6 in development as of this writing.
For a complete list of FHIR R4 Resources and their respective maturities,
please see the `FHIR R4
Resource List <https://hl7.org/fhir/R4/resourcelist.html>`__.

What is the *MDI FHIR IG*?
--------------------------

The `Medicolegal Death Investigation (MDI) FHIR Implementation Guide (IG) <http://hl7.org/fhir/us/mdi/>`__ is a FHIR
implementation guide detailing the proper method of using FHIR Resources
to construct a FHIR version of a Death and Toxicology Reporting. The MDI standard is
developed to support modernization of interoperability between Coroner/Medical Examiner case management systems (CMS) 
and other systems such as Electronic Death Registrar Systems (EDRS) and Toxicology Lab Information and Management System (LIMS).

The Raven MDI Platform is an MDI FHIR IG reference implementation, which demonstrates the MDI FHIR IG for handling death
records. The Raven Platform allows users to import their own data into MDI FHIR IG resources and store them on the Raven
MDI FHIR Server. Users may then browse their imported records as FHIR Resources, use it in workflow simulations, and more.

The MDI FHIR IG is currently in Trial Use (version 2.0.0-STU2). Further updates will be made as additional needs are identified.

For a more detailed overview of the MDI FHIR IG contents, please see the `official
MDI Implementation Guide <http://hl7.org/fhir/us/mdi/background.html>`__.

Overview of MDI Workflows 
-------------------------

Currently, three workflows are defined in the MDI FHIR IG:

* MDI-and-EDRS Case Creation and Update
* Toxicology-to-MDI
* Death Certificate Review

The MDI FHIR IG defines profiles to describe the required content structures for the supported workflows.

MDI-and-EDRS (Case Creation and Update)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The MDI-and-EDRS workflow describes data exchange between an MDI case management system (CMS) and 
a state's electronic death registration system (EDRS) for case creation and update. In the MDI FHIR IG, this
workflow is supported by the MDI-and-EDRS set of profiles.

In most states, cases are created by funeral directors who begin this workflow with an initial case created
in the state EDRS. The case management system searches the EDRS for a case and retrieves the case with limited
decedent demographic information. The CMS may then update the case during the course of a death investigation.
When the investigation is completed, the case is certified and the completed record is submitted to the state EDRS. 

To support this workflow, Raven users can import, validate, and review MDI-and-EDRS FHIR Document Bundles, as
well as submit their FHIR Document Bundles to a simulated EDRS server.

The MDI-and-EDRS Record Viewer allows users to review records stored on the Raven FHIR Server. To support better
understanding of the data elements, the FHIR Explorer allows users to see the underlying FHIR Resources.

The Workflow Simulator allows users to submit a FHIR Document Bundle to a simulated EDRS server. For externally
generated FHIR Document Bundles, records must be valid before they can be loaded into the Raven FHIR Server for use in EDRS submission. For those who do not have their own dataset or are not ready to
produce FHIR data, Raven allows users to use the preloaded data from the Raven FHIR Server to simulate the case
submission.

For more information on the MDI and EDRS exchange use case, please see:
`Death Case Record Creation and Update for Death Certificate
<https://hl7.org/fhir/us/mdi/mdi_use_cases.html#death-case-record-creation-and-update-for-death-certificate>`__

Toxicology-to-MDI
^^^^^^^^^^^^^^^^^
The Toxicology-to-MDI workflow covers data exchange between a forensic toxicology laboratory information 
management system (LIMS) to an MDI case management system (CMS). In the MDI FHIR IG, this workflow is supported by
Toxicology-to-MDI profiles. The MDI FHIR IG only defines the delivery of a toxicology lab report from a LIMS to a CMS,
and does not cover the initial order request. Unlike the other use cases, this workflow relies on a FHIR message Bundle,
matching traditional HL7v2 style messaging workflows more closely.

Raven users can validate Toxicology-to-MDI FHIR profiles, including complete message Bundles messages. Use data may be imported
into the Raven FHIR Server and then browsed with the Raven record viewing including the FHIR Explorer. 

For more information on the Toxicology use case, please see:
`Transmission of Forensic Toxicology Diagnostic Findings from LIMS to MDI CMS <https://hl7.org/fhir/us/mdi/mdi_use_cases.html#transmission-of-forensic-toxicology-diagnostic-findings-from-lims-to-mdi-cms>`__

Death Certificate Review
^^^^^^^^^^^^^^^^^^^^^^^^
The Death Certificate Review profiles cover data quality improvement and cremation clearance requests.
As with the MDI-and-EDRS case creation and update use case, the Death Certificate Review data exchange occurs between a CMS and a state
EDRS. The Death Certificate Review is a bidirectional workflow which also supports a response, such as updated information from the coroner/medical examiner
system when improving data quality.

The Death Certificate Review records can be browsed in the Record Viewer, including viewing the underlying FHIR resources with the FHIR Explorer
for each data element. The Workflow Simulator Death Certificate Review module also allows for testing submissions.

For more information on the Death Certificate Review use case, please see:
`Death Certificate Review <https://build.fhir.org/ig/HL7/fhir-mdi-ig/mdi_use_cases.html#transmission-of-a-death-certificate-for-review>`__