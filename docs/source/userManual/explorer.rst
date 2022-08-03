FHIR Explorer
=============

In the top right corner of the Raven Dashboard, you will find a toggle
switch for the FHIR Explorer.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/fhir_explorer_button.jpeg
   :alt: FHIR Explorer Button

   FHIR Explorer Button

Selecting this will open the FHIR Explorer window, shifting the
currently selected case data to the side.

By default, this displays the full FHIR Resource bundle from the Raven
FHIR Server, allowing you to look over the corresponding raw FHIR data
in JSON format.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/fhir_explorer_pane.jpeg
   :alt: FHIR Explorer Pane

   FHIR Explorer Pane

This view also allows you to see how each individual element in the case
summary is being mapped from the FHIR bundle. Selecting an element in
the case summary will navigate the FHIR bundle to the FHIR resource from
which it was obtained and display it in the FHIR Explorer window.

In the screenshot below you can see this with the “Place of Death”
element. When selected the FHIR Explorer shifts to a Location resource
which contains the relevant portion of the record.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/fhir_explorer_element_level_view.jpeg
   :alt: FHIR Explorer Element Level View

   FHIR Explorer Element Level View

VRDR Document View
------------------

Below the FHIR Explorer toggle you will also find a VRDR Document
button.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/vrdr_document_button.jpeg
   :alt: FHIR VRDR Document Button

   FHIR VRDR Document Button

With the FHIR Explorer enabled, you can select this button to change the
view of the FHIR Explorer window to the FHIR VRDR Document Bundle, again
in JSON format. This allows you to navigate the bundle in order to see
how corresponding case element reflect the VRDR requirements.

.. figure:: https://github.com/MortalityReporting/raven-platform/blob/main/screenshots/vrdr_explorer_pane.jpeg
   :alt: FHIR VRDR Document Explorer Pane

   FHIR VRDR Document Explorer Pane
