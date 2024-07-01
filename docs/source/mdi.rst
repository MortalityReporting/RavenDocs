.. _mdi-csv:

Medicolegal Death Investigation (MDI) CSV Data
==============================================

In order for user data to be imported into the Raven FHIR Server and
accessed by the Raven Platform, it must be available as FHIR VRDR
Resources. (For more information on FHIR VRDR, please visit the :ref:`fhir` page in this wiki.) However, as it is still
an emerging technology most systems cannot natively provide their data
as FHIR resources. In order to facilitate non-FHIR enabled systems in
using the Raven Platform, the MDI CSV format is provided. The Raven
Platform is designed to be able to map the Raven MDI CSV format into the
proper FHIR Resources.

CSV (“Comma-separated Values”) is a common plain text format for storing
data, such as tables or spreadsheets. Each column for a field is
separated by a comma, with each new line indicating a row of data. For
MDI CSV, each row represents a full death investigation case file.

You can find an example of MDI CSV data in the Raven Platform repository
at
https://github.com/MortalityReporting/raven-platform/blob/main/testing-documents/ConnectathonTestCases.csv.

Using MDI CSV
-------------

This section discusses general concerns regarding mapping to MDI CSV
from your own data. For a complete tutorial on using the Raven Dashboard
to assist in the mapping of your external data to the MDI CSV format.

Non-mappable Fields
~~~~~~~~~~~~~~~~~~~

If there are no clear mappings between your data set and the reference
MDI CSV, you may include a blank field which will be considered as a
null value.

Unique Identifiers (CASEID and SYSTEMID)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FHIR Resources include an “identifier” element which allows users to
define unique system identifiers for a Resource independent of the
Resource’s logical ID on a specific FHIR Server. For example, in
clinical data a Patient resource may include a series of identifiers
that represent the patient in a specific Hospital system. For MDI CSV
data you must include two identifiers, “CASEID” and “SYSTEMID”, in order
to distinguish your decedent cases from other cases. “SYSTEMID” is used
to represented the original CMS from which the case originated, while
“CASEID” is a unique representation of that specific case. This allows a
single instance of Raven to serve many systems simultaneously.

Note on Identifier vs ID in FHIR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please be aware that the FHIR “identifier” element is not the same as
the FHIR “id” element. The FHIR “id” element, also known as logical ID,
is a representation of the FHIR Resource on a specific FHIR server and
is not a consistent identifier for a single resource across servers. If
your resource has a logical ID of “12345” on FHIR Server A and is then
transferred to FHIR Server B, it is highly unlikely to have the same
logical ID on FHIR Server B. The “identifier” element on the other hand
should always represent a single, unique entity across any FHIR server.
For instance, a patient’s SSN acts as a unique identifier that will be
the same on FHIR Server A as it is on FHIR Server B. This is why you
must include unique identifier elements for your data for it to be
accessible.

MDI CSV Data Fields and FHIR Mappings
-------------------------------------

For a list of the MDI CSV fields as well as mappings to FHIR (in a
separate sheet), please see the provided `Google Sheets
document <https://docs.google.com/spreadsheets/d/1OShYZEl8ZklDffcmHA3UsoruKc1F9O0f_0t7fnFWESI/edit?usp=sharing>`__.
