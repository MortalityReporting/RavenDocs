Exporting Data to External EDRS(s)
==================================

Raven provides the capability of exporting the FHIR VRDR Resources
representing a case to external Electronic Death Registration Systems.
In the top right corner of the Case File screen, you will find the
“Export” button which allows you to initiate the export process.

Selecting this button will change the status shown on the button to
“Exporting” as it attempts to connect to the external systems. Once the
export is complete, the status will be reflected in the button text by
displaying “Exported”.

Viewing Case Export Status in Browse Cases
------------------------------------------

When reviewing the primary list of cases in the Browse Cases screen, you
will be provided with the current status of the case as it relates the
system as a whole, with a focus on the external export.

Currently three statuses are reflected: \* “Imported” is the initial
state for every case shown in the Raven Dashboard, indicating the case
was properly imported into the FHIR Server. \* “Pending” is displayed
once an export has been initiated but is not yet been completed. \*
“Sent” is displayed once the exported data has been passed to the
external EDRS systems. Please be aware that this does not reflect the
**success** of the export API to the external EDRS systems.
