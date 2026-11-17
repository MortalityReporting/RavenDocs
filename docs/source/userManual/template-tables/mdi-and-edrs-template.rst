
.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Sections
     - Elements
     - Description
   * - Tracking Numbers
     -
     - This section is for tracking separate identifiers: an identifier for the local MDI system and the state registrar (EDRS) file number.
   * - Tracking Numbers
     - Tracking Number: MDI Case Number
     - A locally unique case number from the case management system. Optional.
   * - Tracking Numbers
     - Tracking Number: EDRS File Number
     - A locally unique case number from the state registrar (EDRS). Usually assigned once the case has been registered or submitted to the state registrar. Optional.
   * - Decedent
     -
     - This section is for decedent demographic information. All information resides in the US Core Patient resource within the document.
   * - Decedent
     - Decedent Name
     - Primary name of the decedent. Accepted formats: ``<First Name> <Last Name>``, ``<First Name> <Middle Initial> <Last Name>``, or ``<First Name> <Middle Name> <Last Name>``.
   * - Decedent
     - Decedent Race
     - Race of the decedent. Accepted values are shown in the dropdown. If the decedent has multiple race entries, use a comma-separated list to enter multiple races.
   * - Decedent
     - Decedent Ethnicity
     - Ethnicity of the decedent. Accepted values are shown in the dropdown.
   * - Decedent
     - Decedent SexAtDeath
     - Decedent's sex at the time of death. Accepted values are shown in the dropdown.
   * - Decedent
     - Decedent SSN
     - Social Security number of the decedent. Accepted format: ``###-##-####``.
   * - Decedent
     - Decedent Age
     - Age of the decedent. In the case of an infant or fetal death, an age denomination may be used. Accepted formats: ``<Age Value>`` or ``<Age Value> <Age Unit>``.
   * - Decedent
     - Decedent DOB
     - Date on which the decedent was born. Accepted formats: ``mm/dd/yyyy`` or ``mm-dd-yyyy``.
   * - Decedent
     - Decedent Marital Status
     -
   * - Decedent
     - Decedent Residence: Street
     - Primary street address of the decedent's residence. Multiple lines are supported.
   * - Decedent
     - Decedent Residence: City
     -
   * - Decedent
     - Decedent Residence: County
     -
   * - Decedent
     - Decedent Residence: State, U.S. Territory, or Canadian Province
     -
   * - Decedent
     - Decedent Residence: Postal Code
     -
   * - Decedent
     - Decedent Residence: Country
     -
   * - Cause and Manner of Death
     -
     - This section is for information collected in the Cause and Manner section of the MDI case document. Data includes the cause-of-death pathway, manner of death, death date, and injury description and circumstances.
   * - Cause and Manner of Death
     - Cause of Death Part I Line a
     - First line of the cause of death.
   * - Cause and Manner of Death
     - Cause of Death Part I Line b
     - Second line of the cause of death.
   * - Cause and Manner of Death
     - Cause of Death Part I Line c
     - Third line of the cause of death.
   * - Cause and Manner of Death
     - Cause of Death Part I Line d
     - Fourth line of the cause of death.
   * - Cause and Manner of Death
     - Cause of Death Part I Interval, Line a
     - Approximate interval of the first cause of death. A unit of age must be provided. Accepted format: ``<Age> <Age Unit>``.
   * - Cause and Manner of Death
     - Cause of Death Part I Interval, Line b
     - Approximate interval of the second cause of death. A unit of age must be provided. Accepted format: ``<Age> <Age Unit>``.
   * - Cause and Manner of Death
     - Cause of Death Part I Interval, Line c
     - Approximate interval of the third cause of death. A unit of age must be provided. Accepted format: ``<Age> <Age Unit>``.
   * - Cause and Manner of Death
     - Cause of Death Part I Interval, Line d
     - Approximate interval of the fourth cause of death. A unit of age must be provided. Accepted format: ``<Age> <Age Unit>``.
   * - Cause and Manner of Death
     - Cause of Death Part II
     - Other contributing conditions to the cause of death. If multiple contributing conditions apply, use a comma-separated list.
   * - Cause and Manner of Death
     - Manner of Death
     - Manner of death. Accepted values are shown in the dropdown.
   * - Cause and Manner of Death
     - Date of Injury
     - If an injury led to death, the date of the injury. Accepted formats: ``mm/dd/yyyy`` or ``mm-dd-yyyy``.
   * - Cause and Manner of Death
     - Time of Injury
     - If an injury led to death, the time of the injury. The Date of Injury must be completed for the time of injury to be accepted. Accepted formats: ``hh:mm:ss``, ``hh:mm``, or ``hh:mm AM/PM``.
   * - Cause and Manner of Death
     - How Injury Occurred
     - A text description of the injury.
   * - Cause and Manner of Death
     - Did Injury Occur at Work?
     - In the case of an injury, whether the injury was part of the decedent's work. Accepted values are shown in the dropdown.
   * - Cause and Manner of Death
     - Decedent's Transportation Role During Injury
     - If a vehicle was involved in an injury, whether the decedent was a driver, passenger, or pedestrian. Accepted values are shown in the dropdown.
   * - Death Circumstances
     -
     - This section describes specific findings and circumstances related to the decedent's death, including the death location, injury location, death date, pregnancy status, and whether tobacco use contributed to death.
   * - Death Circumstances
     - Location of Death
     - Full or partial address describing the location of death.
   * - Death Circumstances
     - Location of Injury
     - If an injury occurred, a description or full or partial address of the location of the injury.
   * - Death Circumstances
     - Pregnancy Status
     - Whether the decedent was pregnant and, if so, how close to term the decedent was. Accepted values are shown in the dropdown.
   * - Death Circumstances
     - Did Tobacco Use Contribute to Death?
     - If the decedent used tobacco, whether tobacco use contributed to the cause of death. Accepted values are shown in the dropdown.
   * - Jurisdiction
     -
     - This section describes jurisdictional findings for the case, including the date of death, date pronounced dead, and place of death.
   * - Jurisdiction
     - Decedent Date of Death
     - Date of death of the decedent. Accepted formats: ``mm/dd/yyyy`` or ``mm-dd-yyyy``.
   * - Jurisdiction
     - Decedent Time of Death
     - Time of death of the decedent. The Decedent Date of Death must be completed for the time of death to be accepted. Accepted formats: ``hh:mm:ss``, ``hh:mm``, or ``hh:mm AM/PM``.
   * - Jurisdiction
     - Date Establishment Method
     - Circumstances under which the date of death was established. Accepted values are shown in the dropdown.
   * - Jurisdiction
     - Date Pronounced Dead
     - Date on which the decedent was formally pronounced dead. Accepted formats: ``mm/dd/yyyy`` or ``mm-dd-yyyy``.
   * - Jurisdiction
     - Time Pronounced Dead
     - Time at which the decedent was formally pronounced dead. Date Pronounced Dead must be completed for the time to be accepted. Accepted formats: ``hh:mm:ss``, ``hh:mm``, or ``hh:mm AM/PM``.
   * - Jurisdiction
     - Place of Death
     - Type of place where the decedent died, such as a home, hospital, or hospice. Accepted values are shown in the dropdown.
   * - Exam-Autopsy
     -
     - This section describes the autopsy findings, if an autopsy occurred.
   * - Exam-Autopsy
     - Autopsy Performed?
     - Whether an autopsy was performed on the body.
   * - Exam-Autopsy
     - Autopsy Results Available?
     - If an autopsy was performed, whether the results are available and used to determine the cause of death.
   * - Chief Medical Examiner/Coroner
     -
     - This section describes the primary chief medical examiner or coroner associated with the case.
   * - Chief Medical Examiner/Coroner
     - Medical Examiner Name
     - Name of the medical examiner. Accepted formats: ``<First Name> <Last Name>``, ``<First Name> <Middle Initial> <Last Name>``, or ``<First Name> <Middle Name> <Last Name>``.
   * - Chief Medical Examiner/Coroner
     - Medical Examiner Phone Number
     - Phone number of the medical examiner's office or primary contact number. Accepted format: ``###-###-####``.
   * - Chief Medical Examiner/Coroner
     - Medical Examiner License Number
     - Medical examiner license number associated with the jurisdiction in which the case is owned.
   * - Chief Medical Examiner/Coroner
     - Medical Examiner Office: Street
     - Primary street address of the medical examiner's office. Multiple lines are supported.
   * - Chief Medical Examiner/Coroner
     - Medical Examiner Office: City
     -
   * - Chief Medical Examiner/Coroner
     - Medical Examiner Office: County
     -
   * - Chief Medical Examiner/Coroner
     - Medical Examiner Office: State, U.S. Territory, or Canadian Province
     -
   * - Chief Medical Examiner/Coroner
     - Medical Examiner Office: Postal Code
     -
   * - Certifier
     -
     - This section describes the certifier of the case, if the case has been certified. The chief medical examiner and the certifier can often be the same person. If the case is not certified, leave this section blank.
   * - Certifier
     - Certifier Name
     - Name of the certifier. Accepted formats: ``<First Name> <Last Name>``, ``<First Name> <Middle Initial> <Last Name>``, or ``<First Name> <Middle Name> <Last Name>``.
   * - Certifier
     - Certifier Type
     - Whether the certifier is a physician, pronouncer, or other type of certifier.
