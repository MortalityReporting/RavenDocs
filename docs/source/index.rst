Welcome to the Raven Platform documentation! 
============================================

This wiki exists as a guide to help users understand 
the Raven mortality platform, providing
both end-user manuals as well as technical documentation for items such
as data schema.

What is Raven?
--------------

Raven is a Proof-Of-Concept Case Management System for a local Coroners
or Medical Examiners. Raven stores Decedent case data in the form of
`FHIR resources <https://www.hl7.org/fhir/>`__, which can be easily
shared and analyzed across many platforms. Raven’s components consist
of:

-  Raven Dashboard: The Raven Dashboard serves is the frontend for the
   Raven Platform through which user’s can import their own data, view
   currently stored FHIR VRDR Resources, and export FHIR VRDR Resources
   to external Death Registration Systems.
-  Raven FHIR Server: The Raven FHIR Server provides API access to a
   Fhirbase database, which acts as the data store for the Raven
   Platform.
-  Raven Import and Submission API: The Raven Import and Submission API
   component (sometimes seen under the legacy name Raven Mapper API)
   provides for two distinct APIs, one for importing MDI CSV data to the
   FHIR Server and another for submitting exported VRDR compliant
   documents to external systems.

For more information on each Raven component, Raven’s MDI CSV schema, or
FHIR Vital Records Death Reporting standard please see the corresponding
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

