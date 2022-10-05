Welcome to the Raven Platform documentation! 
============================================

This wiki exists as a guide to help users understand 
the Raven mortality platform, providing
both end-user manuals as well as technical documentation for items such
as data schema.

What is Raven?
--------------

Raven is an open-source, proof-of-concept platform that serves as a reference implementation and provides testing tools for interoperability between case management systems (CMS) and other external actors. The external actors are those data sources with which CMS need to communicate to exchange Medicolegal Death Investigation (MDI) data, and may include, but not be limited to, electronic death registration systems (EDRS) and forensic toxicology laboratory information management systems (LIMS).

The current Raven tooling and tests aid developers in implementing the MDI FHIR record format by validating FHIR messages against MDI IG guidelines and FHIR-based extended API operations. For more information on each Raven tool components, Raven’s MDI CSV schema, or
FHIR MDI standard please see the corresponding
sections in this wiki, accessible through the table of contents below or
the sidebar navigation menu.


.. toctree::
   :numbered:
   :hidden:
   
   developmentTeam
   endUserManual
   technicalManual

Raven is released under the `Apache License
2.0 <https://github.com/MortalityReporting/raven-platform/blob/main/LICENSE>`__.

Source repositories for Raven can be found in the `GitHub Mortality Reporting Organization <https://github.com/MortalityReporting/>`_.

.. note::

   -  All data shown is synthetic for demonstration purposes only and does
      not represent actual cases or decedents.*
   -  Screenshots may be taken from earlier internal versions of Raven and
      may not be 100% accurate to the final release.*

   If you find an error in the Raven platform and documentation, please go to the ":ref:`members`" page 
   and let us know!

