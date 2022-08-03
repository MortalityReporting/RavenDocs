Browse and View Cases
=====================

Browsing Cases
--------------

When you first load Raven you will be taken to the Browse Cases page.
This page provides an overview of the currently stored cases in the
Raven FHIR Server, including the case decedent name, the unique Case ID
#, the time of death of the decedent, the system of origin for the
report, and the current export status of the case. Clicking a row will
take you to the case page for that case.

**Note:** If you have no data on your Raven FHIR Server, you will not
see any cases listed. You should begin by selecting the “Import CSV”
button and following the instructions on the `Import Page of the User
Manual <User-Manual-Importing>`__.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/browse_cases.jpeg
   :alt: Browse Cases Screenshot

   Browse Cases Screenshot

Searching and Filtering Cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the top of the list of cases you will find options for searching by
Case ID # and filtering by the system of origin. Please note that the
search functionality does not allow for the use of advanced search
conditions.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/search_and_filter_cases.jpeg
   :alt: Search and Filter Cases Screenshot

   Search and Filter Cases Screenshot

Import and Export Status
~~~~~~~~~~~~~~~~~~~~~~~~

In the far right column for each case in the list you will see the
current status of the case as related to the Raven Platform. Possible
statuses are “Imported”, “Pending”, and “Sent”. For more information on
the export process, please see the `Export Data section of the User
Manual <User-Manual-Exporting>`__.

Viewing Case Files
------------------

Selecting a case row from the Browse Cases screen will take you to a
more detailed view of that case file. In the case file header bar you
are provided with the Case ID #, decedent full name, and the date and
time of death.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/view_case_header.jpeg
   :alt: View Cases Screen Header Bar

   View Cases Screen Header Bar

While viewing a case you are also presented with additional navigation
option and viewing options in the header bar. \* “Browse Cases” returns
you to the Browse Case view. \* “Import CSV” takes you to the import
page. For more information, please see the `Importing Data page of the
User Manual <User-Manual-Importing>`__. \* “FHIR Explorer” opens the
FHIR Explorer window, which allows you to view the raw FHIR Resource
versions of the information displayed. For more information, please see
the `FHIR Explorer page of the User
Manual <User-Manual-FHIR-Explorer>`__. \* “VRDR Document” toggles the
VRDR Document view of the FHIR Explorer. For more information, please
see the `FHIR Explorer page of the User
Manual <User-Manual-FHIR-Explorer>`__. \* “Export” initiates the case
export to an external EDRS. For more information, please see the
`Exporting page of the User Manual <User-Manual-Exporting>`__.

You may also switch between several tabs for viewing different sections
of the case report. Case Summary provides an overview of the case
details. Decedent Detail provides a look at the decedent’s demographic
information.

*Please note that the Case Notes, Toxicology, and Documents tabs are
currently in development for Raven 2.0.*

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/case_file_tabs.jpeg
   :alt: Case File Tabs

   Case File Tabs

Case Summary
~~~~~~~~~~~~

The Case Summary tab is the default selected view when first opening a
case. This tab provides the most detailed look at the case itself. If
there are errors in the imported record they will be highlighted here to
enable user review of the data.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/case_summary.jpeg
   :alt: Case Summary View

   Case Summary View

The top section of the case summary contains information about the
certification of death itself, including the agent who signed the
certificate, deputy coroner, and so forth.

The second section of the summary contains core case information, such
as relevant dates, whether or not surgery or an autopsy has been
performed, and locations related to aspects of the case.

The bottom section is the summary of the cause and manner of death,
providing the time prior to onset of death for each cause, along with
any other contributing factors.

With the FHIR Explorer open, you can click on each element in the Case
Summary to show its location in the FHIR Bundle. For more information on
this, please see the `FHIR Explorer page of this
wiki <User-Manual-FHIR-Explorer>`__.

Decedent Details
~~~~~~~~~~~~~~~~

The Decedent Details tab provides an overview of the decedent’s
demographic details, including the decedent’s full name, gender, date of
birth, age, race, ethnicity, and address.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/decedent_details.jpeg
   :alt: Decedent Details View

   Decedent Details View
