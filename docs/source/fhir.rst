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

FHIR VRDR Resources
-------------------

The `Vital Records Mortality and Morbidity Reporting (VRDR)
Implementation Guide <http://hl7.org/fhir/us/vrdr/>`__ is a FHIR
implementation guide detailing the proper method of using FHIR resources
to construct a FHIR version of a Death Certificate. The VRDR standard is
used by Electronic Death Registrar Systems (EDRS) that reside at the
state level, in order to report to federal standards.

The Raven Platform uses the VRDR implementation for handling death
records, allowing exporting to those same external EDRS systems. When
possible, the Raven Platform allows users to import their own data into
FHIR VRDR resources and store them on the Raven FHIR Server.

VRDR consists of 4 major domains of death data: \* Decedent Demographic
Information - The decedent’s demographic information, such as name,
related persons, date of birth, and other similar. \* Death
Investigation Data - Autopsy Information, injury incident information,
death location, and other information related to death investigations.
\* Death Certification Data - The cause of death pathway, manner of
death, the certifying agent, and information otherwise related to the
actual death certification. \* Decedent Disposition Information -
Disposition related information, such as funeral home, attending
mortician, and disposition method.

For a more detailed breakdown of VRDR contents, please see the `official
VRDR data model
guide <http://hl7.org/fhir/us/vrdr/vrdr_fhir_ig_uml_data_model.html>`__.

Inclusion of Base FHIR Resources
--------------------------------

There is a gap that exists with mapping the Raven MDI data to VRDR
resources, as not all MDI fields can be properly mapped to VRDR. Raven
addresses this gap through the use of base FHIR resources included as
part of the FHIR Bundles alongside the VRDR Resources. The use of these
base resources are considered temporary pending a proper FHIR MDI
implementation guide with the necessary profiles.
