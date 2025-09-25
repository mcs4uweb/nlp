class XmlConstants:
    """
    This class acts as a namespace for static XML templates and constants.
    It is not meant to be instantiated. Its attributes should be accessed directly
    via the class name (e.g., XmlConstants.THORACIC_TEST_REPORT_XML).
    """

    def __init__(self):
        """Prevents instantiation of this constants class."""
        raise NotImplementedError("This class is not meant to be instantiated.")

    # Using triple quotes allows for a clean, multi-line string definition.
    # The variable is named in UPPERCASE_SNAKE_CASE, the Python convention for constants.
    THORACIC_TEST_REPORT_XML: str = """
<report xmlns="urn:com-cerner-patient-ehr:v3">
    <clinical-data>
        <document-data>
            <document encounter-id="97953477" is-published="true" documentation-dt-tm="2023-01-08T22:25:37.000-06:00" title="Thoracic test" event-end-dt-tm="2024-01-08T22:25:36.000-06:00" event-id="203481876" event-status-code="25" group-id="203481876" updt-dt-tm="2023-01-09T04:25:38.000Z">
                <event-type event-code-id="2820507" event-display="Admission Note Physician"/>
                <participation participating-personnel="12742069" participation-dt-tm="2023-01-08T22:25:36.000-06:00" personnel-free-text-name="" participating-entity-id="12742069" participating-entity-freetext="" participating-entity-type="PERSONNEL" type-code="112">
                    <participation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:36.000-06:00</participation-dt-tm>
                </participation>
                <participation participating-personnel="12742069" participation-dt-tm="2023-01-08T22:25:37.000-06:00" personnel-free-text-name="" participating-entity-id="12742069" participating-entity-freetext="" participating-entity-type="PERSONNEL" type-code="104">
                    <participation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:37.000-06:00</participation-dt-tm>
                </participation>
                <participation participating-personnel="12742069" participation-dt-tm="2023-01-08T22:25:37.000-06:00" personnel-free-text-name="" participating-entity-id="12742069" participating-entity-freetext="" participating-entity-type="PERSONNEL" type-code="107">
                    <participation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:37.000-06:00</participation-dt-tm>
                </participation>
                <event-end-dt-tm time-zone="America/Chicago">2024-01-08T22:25:36.000-06:00</event-end-dt-tm>
                <updt-dt-tm time-zone="UTC">2023-01-09T04:25:38.000Z</updt-dt-tm>
                <encntr-id>97953477</encntr-id>
                <documentation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:37.000-06:00</documentation-dt-tm>
                <document-contribution event-id="203481876" status-code="25" version="1">
                    <section is-published="true" documentation-dt-tm="2023-01-08T22:25:37.000-06:00" sequence="000_500_00771121957464" title="Thoracic test" event-end-dt-tm="2024-01-08T22:25:36.000-06:00" event-id="203481878" event-status-code="25" group-id="203481876" updt-dt-tm="2023-01-09T04:25:38.000Z">
                        <event-type event-code-id="2820507" event-display="Admission Note Physician"/>
                        <participation participating-personnel="12742069" participation-dt-tm="2023-01-08T22:25:36.000-06:00" personnel-free-text-name="" participating-entity-id="12742069" participating-entity-freetext="" participating-entity-type="PERSONNEL" type-code="112">
                            <participation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:36.000-06:00</participation-dt-tm>
                        </participation>
                        <participation participating-personnel="12742069" participation-dt-tm="2023-01-08T22:25:37.000-06:00" personnel-free-text-name="" participating-entity-id="12742069" participating-entity-freetext="" participating-entity-type="PERSONNEL" type-code="104">
                            <participation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:37.000-06:00</participation-dt-tm>
                        </participation>
                        <participation participating-personnel="12742069" participation-dt-tm="2023-01-08T22:25:37.000-06:00" personnel-free-text-name="" participating-entity-id="12742069" participating-entity-freetext="" participating-entity-type="PERSONNEL" type-code="107">
                            <participation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:37.000-06:00</participation-dt-tm>
                        </participation>
                        <event-end-dt-tm time-zone="America/Chicago">2024-01-08T22:25:36.000-06:00</event-end-dt-tm>
                        <updt-dt-tm time-zone="UTC">2023-01-09T04:25:38.000Z</updt-dt-tm>
                        <encntr-id>97953477</encntr-id>
                        <documentation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:37.000-06:00</documentation-dt-tm>
                        <blob-body blob-handle="{80-42-07-c4-5b-3d-48-8c-88-c2-2b-00-97-80-4a-93}">
                            <blob-content media-type="application/pdf" media-format-name="PDF" format="BASE64" number-of-pages="2">
                                <image-page-metadata page-index="1" height-in-inches="11.0" width-in-inches="8.5"/>
                                <image-page-metadata page-index="2" height-in-inches="11.0" width-in-inches="8.5"/>
                            </blob-content>
                        </blob-body>
                    </section>
                    <documentation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:37.000-06:00</documentation-dt-tm>
                    <participation participating-personnel="12742069" participation-dt-tm="2023-01-08T22:25:37.000-06:00" personnel-free-text-name="" participating-entity-id="12742069" participating-entity-freetext="" participating-entity-type="PERSONNEL" type-code="104">
                        <participation-dt-tm time-zone="America/Chicago">2023-01-08T22:25:37.000-06:00</participation-dt-tm>
                    </participation>
                </document-contribution>
            </document>
        </document-data>
    </clinical-data>
    <request-attributes distribution-id="0" print-dt-tm="2023-01-11T17:11:10.779Z" request-id="0" request-scope="0" route-id="0" route-stop-id="0" request-type-flag="0" patient-request-ind="false">
        <print-dt-tm time-zone="UTC">2023-01-11T17:11:10.779Z</print-dt-tm>
    </request-attributes>
    <code-list>
        <code code="112" code-set="21" description="VERIFY" display="VERIFY" meaning="VERIFY" sequence="0"/>
        <code code="2572441073" code-set="263" description="EDIPI" display="EDIPI" meaning="" sequence="0"/>
        <code code="104" code-set="21" description="Perform" display="Perform" meaning="PERFORM" sequence="0"/>
        <code code="26026547" code-set="263" description="National Provider Identifier" display="National Provider Identifier" meaning="" sequence="0"/>
        <code code="4038127" code-set="320" description="National Provider Identifier" display="National Provider Identifier" meaning="NPI" sequence="0" concept-cki=" "/>
        <code code="1086" code-set="320" description="External Identifier" display="External Identifier" meaning="EXTERNALID" sequence="0"/>
        <code code="107" code-set="21" description="Sign" display="Sign" meaning="SIGN" sequence="0"/>
        <code code="25" code-set="8" description="Auth (Verified)" display="Auth (Verified)" meaning="AUTH" sequence="0" concept-cki="CERNER!AfxL7AEMY9rGt4AhCr0MCQ"/>
    </code-list>
    <personnel-list>
        <personnel prsnl-id="12742069">
            <personnel-source>CLINICAL_DATA</personnel-source>
            <provider-name name-full="Portal, Portal" name-first="Portal" name-last="Portal" begin-dt-tm="2020-02-04T21:44:15.000Z" end-dt-tm="292278994-08-17T07:12:55.807Z">
                <begin-dt-tm time-zone="UTC">2020-02-04T21:44:15.000Z</begin-dt-tm>
                <end-dt-tm time-zone="UTC">292278994-08-17T07:12:55.807Z</end-dt-tm>
            </provider-name>
            <personnel-alias personnelAliasTypeCode="4038127" alias-type-code="4038127" alias-pool-code="26026547" unformatted-alias="1111">1111</personnel-alias>
            <personnel-alias personnelAliasTypeCode="1086" alias-type-code="1086" alias-pool-code="2572441073" unformatted-alias="1000011111">1000011111</personnel-alias>
            <personnel-alias-data personnelAliasTypeCode="4038127" alias-pool-code="26026547" unformatted-alias="1111" formatted-alias="1111">
                <begin-effective-dt-tm time-zone="UTC">2021-03-03T11:17:35.000Z</begin-effective-dt-tm>
                <end-effective-dt-tm time-zone="UTC">292278994-08-17T07:12:55.807Z</end-effective-dt-tm>
            </personnel-alias-data>
            <personnel-alias-data personnelAliasTypeCode="1086" alias-pool-code="2572441073" unformatted-alias="1000011111" formatted-alias="1000011111">
                <begin-effective-dt-tm time-zone="UTC">2021-03-01T15:50:53.000Z</begin-effective-dt-tm>
                <end-effective-dt-tm time-zone="UTC">2100-12-31T06:00:00.000Z</end-effective-dt-tm>
            </personnel-alias-data>
        </personnel>
    </personnel-list>
</report>
"""

    TEST_REPORT_XML: str = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<?xml-stylesheet type="text/xsl" href="http://www.cerner.com/cda_stylesheet/"?>
<ClinicalDocument classCode="DOCCLIN" moodCode="EVN"
    xmlns="urn:hl7-org:v3" xmlns:sdtc="urn:hl7-org:sdtc"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3../../../CDA%20R2/cda-schemas-and-samples/infrastructure/cda/CDA.xsd">
    <realmCode code="US"/>
    <typeId extension="POCD_HD000040" root="2.16.840.1.113883.1.3"/>
    <templateId root="2.16.840.1.113883.10.20.22.1.1"/>
    <templateId root="2.16.840.1.113883.10.20.22.1.2"/>
    <id extension="732028" root="2.16.840.1.113883.3.42.10001.100001.999362"/>
    <code code="34133-9" codeSystem="2.16.840.1.113883.6.1" displayName="Summarization of episode note"/>
    <title>Transition of Care/Referral Summary</title>
    <effectiveTime value="20170623154745.984-0500"/>
    <confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25" displayName="Normal"/>
    <languageCode code="en-US"/>
    <recordTarget contextControlCode="OP" typeCode="RCT">
        <patientRole classCode="PAT">
            <id assigningAuthorityName="SSN" extension="666000001" root="2.16.840.1.113883.4.1"/>
            <id assigningAuthorityName="Person DoD ID"
                extension="1463132140" root="2.16.840.1.113883.3.42.10001.100001.12"/>
            <addr use="HP">
                <streetAddressLine>1234 HOWARD ST</streetAddressLine>
                <city>LA JOLLA</city>
                <state>CA</state>
                <postalCode>92038-    </postalCode>
                <country>US</country>
            </addr>
            <telecom use="HP" value="tel:(760)222-5555"/>
            <patient classCode="PSN" determinerCode="INSTANCE">
                <name use="L">
                    <given>CHDRONE</given>
                    <family>CHDRZZZTESTPATIENT</family>
                </name>
                <administrativeGenderCode code="M"
                    codeSystem="2.16.840.1.113883.5.1"
                    codeSystemName="administrativeGender" displayName="Male">
                    <originalText>Male</originalText>
                </administrativeGenderCode>
                <birthTime value="19600303"/>
                <raceCode code="2054-5"
                    codeSystem="2.16.840.1.113883.6.238"
                    codeSystemName="Race and Ethnicity - CDC" displayName="Black or African American">
                    <originalText>Black or African American</originalText>
                </raceCode>
                <ethnicGroupCode code="2186-5"
                    codeSystem="2.16.840.1.113883.6.238"
                    codeSystemName="Race and Ethnicity - CDC" displayName="Not Hispanic or Latino"/>
                <languageCommunication>
                    <languageCode code="eng"/>
                </languageCommunication>
            </patient>
        </patientRole>
    </recordTarget>
    <author contextControlCode="OP" typeCode="AUT">
        <time value="20170623154745.984-0500"/>
        <assignedAuthor classCode="ASSIGNED">
            <id assigningAuthorityName="National Provider Identifier"
                extension="113322446655" root="2.16.840.1.113883.3.4.6"/>
            <addr nullFlavor="NI"/>
            <telecom nullFlavor="NI"/>
            <assignedAuthoringDevice>
                <manufacturerModelName>Cerner Corporation</manufacturerModelName>
                <softwareName>Millennium Clinical Document Generator</softwareName>
            </assignedAuthoringDevice>
            <representedOrganization classCode="ORG" determinerCode="INSTANCE">
                <id
                    assigningAuthorityName="National Provider Identifier"
                    extension="113322446655" root="2.16.840.1.113883.3.4.6"/>
                <id root="2.16.840.1.113883.3.42.10001.100001"/>
                <name>MB Military Baseline Medical Center</name>
                <telecom use="WP" value="tel:(555)555-5555"/>
                <addr use="WP">
                    <streetAddressLine>7700 Arlington Blvd</streetAddressLine>
                    <city>Falls Church</city>
                    <state>VA</state>
                    <postalCode>20400-    </postalCode>
                    <country>US</country>
                </addr>
            </representedOrganization>
        </assignedAuthor>
    </author>
    <custodian typeCode="CST">
        <assignedCustodian classCode="ASSIGNED">
            <representedCustodianOrganization classCode="ORG" determinerCode="INSTANCE">
                <id
                    assigningAuthorityName="National Provider Identifier"
                    extension="113322446655" root="2.16.840.1.113883.3.4.6"/>
                <id root="2.16.840.1.113883.3.42.10001.100001"/>
                <name>MB Military Baseline Medical Center</name>
                <telecom use="WP" value="tel:(555)555-5555"/>
                <addr use="WP">
                    <streetAddressLine>7700 Arlington Blvd</streetAddressLine>
                    <city>Falls Church</city>
                    <state>VA</state>
                    <postalCode>20400-    </postalCode>
                    <country>US</country>
                </addr>
            </representedCustodianOrganization>
        </assignedCustodian>
    </custodian>
    <documentationOf typeCode="DOC">
        <serviceEvent classCode="PCPR" moodCode="EVN">
            <effectiveTime>
                <low value="19600303"/>
                <high value="20170623154745.019-0500"/>
            </effectiveTime>
            <performer typeCode="PRF">
                <functionCode code="PCP"
                    codeSystem="2.16.840.1.113883.5.88"
                    codeSystemName="HL7 ParticipationFunction" displayName="primary care physician"/>
                <assignedEntity>
                    <id nullFlavor="NI"/>
                </assignedEntity>
            </performer>
        </serviceEvent>
    </documentationOf>
    <component typeCode="COMP">
        <structuredBody classCode="DOCBODY" moodCode="EVN">
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.22.1"/>
                    <templateId root="2.16.840.1.113883.10.20.22.2.22"/>
                    <code code="46240-8"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="History of hospitalizations+History of outpatient visits"/>
                    <title>Encounter(s)</title>
                    <text>
                        <paragraph ID="ENCOUNTER5297815">
                            <content styleCode="Bold">5/24/17</content>
                            <br/>FC Fairchild Clinics 9  (9  )    -    <br/>
                        </paragraph>
                        <paragraph ID="ENCOUNTER5292986">
                            <content styleCode="Bold">5/18/17</content>
                            <br/>FC Fairchild Clinics 9  (9  )    -    <br/>
                        </paragraph>
                        <paragraph ID="ENCOUNTER5289045">
                            <content styleCode="Bold">5/15/17</content>
                            <br/>FC Fairchild Clinics 9  (9  )    -    <br/>
                        </paragraph>
                        <paragraph ID="ENCOUNTER5287420">
                            <content styleCode="Bold">5/12/17 - 5/12/17</content>
                            <br/>FC Fairchild Clinics 9  (9  )    -    <br/>
                            <content ID="ENCNTRDDP5287420">Discharge Disposition: Home or Self Care</content>
                            <br/>Attending Physician: BLACKWELL, BRIAN E<br/>
                        </paragraph>
                        <paragraph ID="ENCOUNTER5320813">
                            <content styleCode="Bold">3/15/17</content>
                            <br/>FC Fairchild Clinics 9  (9  )    -    <br/>
                        </paragraph>
                    </text>
                    <entry>
                        <encounter classCode="ENC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.49"/>
                            <id nullFlavor="NI"/>
                            <code nullFlavor="UNK">
                                <originalText>Dental</originalText>
                            </code>
                            <effectiveTime>
                                <low value="20170524093024.000-0700"/>
                            </effectiveTime>
                            <participant typeCode="LOC">
                                <participantRole classCode="SDLOC">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.32"/>
                                    <code nullFlavor="NI"/>
                                    <addr use="WP">
                                    <streetAddressLine>9</streetAddressLine>
                                    <city nullFlavor="NI"/>
                                    <state nullFlavor="NI"/>
                                    <postalCode nullFlavor="NI"/>
                                    </addr>
                                    <telecom use="WP" value="tel:(9)-"/>
                                    <playingEntity classCode="PLC">
                                    <name>FC Fairchild Clinics</name>
                                    </playingEntity>
                                </participantRole>
                            </participant>
                        </encounter>
                    </entry>
                    <entry>
                        <encounter classCode="ENC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.49"/>
                            <id nullFlavor="NI"/>
                            <code nullFlavor="UNK">
                                <originalText>Dental</originalText>
                            </code>
                            <effectiveTime>
                                <low value="20170518102219.000-0700"/>
                            </effectiveTime>
                            <participant typeCode="LOC">
                                <participantRole classCode="SDLOC">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.32"/>
                                    <code nullFlavor="NI"/>
                                    <addr use="WP">
                                    <streetAddressLine>9</streetAddressLine>
                                    <city nullFlavor="NI"/>
                                    <state nullFlavor="NI"/>
                                    <postalCode nullFlavor="NI"/>
                                    </addr>
                                    <telecom use="WP" value="tel:(9)-"/>
                                    <playingEntity classCode="PLC">
                                    <name>FC Fairchild Clinics</name>
                                    </playingEntity>
                                </participantRole>
                            </participant>
                        </encounter>
                    </entry>
                    <entry>
                        <encounter classCode="ENC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.49"/>
                            <id nullFlavor="NI"/>
                            <code nullFlavor="UNK">
                                <originalText>Dental</originalText>
                            </code>
                            <effectiveTime>
                                <low value="20170515143000.000-0700"/>
                            </effectiveTime>
                            <participant typeCode="LOC">
                                <participantRole classCode="SDLOC">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.32"/>
                                    <code nullFlavor="NI"/>
                                    <addr use="WP">
                                    <streetAddressLine>9</streetAddressLine>
                                    <city nullFlavor="NI"/>
                                    <state nullFlavor="NI"/>
                                    <postalCode nullFlavor="NI"/>
                                    </addr>
                                    <telecom use="WP" value="tel:(9)-"/>
                                    <playingEntity classCode="PLC">
                                    <name>FC Fairchild Clinics</name>
                                    </playingEntity>
                                </participantRole>
                            </participant>
                        </encounter>
                    </entry>
                    <entry>
                        <encounter classCode="ENC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.49"/>
                            <id nullFlavor="NI"/>
                            <code nullFlavor="UNK">
                                <originalText>Dental</originalText>
                            </code>
                            <effectiveTime>
                                <low value="20170512170000.000-0700"/>
                                <high value="20170512180000.000-0700"/>
                            </effectiveTime>
                            <sdtc:dischargeDispositionCode nullFlavor="UNK">
                                <originalText>
                                    <reference value="#ENCNTRDDP5287420"/>
                                </originalText>
                            </sdtc:dischargeDispositionCode>
                            <performer>
                                <assignedEntity classCode="ASSIGNED">
                                    <id
                                    assigningAuthorityName="National Provider Identifier"
                                    extension="1669712303" root="2.16.840.1.113883.3.4.6"/>
                                    <addr use="WP">
                                    <streetAddressLine>701 HOSPITAL LOOP</streetAddressLine>
                                    <city>FAIRCHILD AIR FORCE BASE</city>
                                    <state>WA</state>
                                    <postalCode>99011-    </postalCode>
                                    </addr>
                                    <telecom use="WP" value="tel:(509)247-5820"/>
                                    <assignedPerson classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <prefix>CAPT</prefix>
                                    <given>BRIAN</given>
                                    <given>E</given>
                                    <family>BLACKWELL</family>
                                    </name>
                                    </assignedPerson>
                                </assignedEntity>
                            </performer>
                            <participant typeCode="LOC">
                                <participantRole classCode="SDLOC">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.32"/>
                                    <code nullFlavor="NI"/>
                                    <addr use="WP">
                                    <streetAddressLine>9</streetAddressLine>
                                    <city nullFlavor="NI"/>
                                    <state nullFlavor="NI"/>
                                    <postalCode nullFlavor="NI"/>
                                    </addr>
                                    <telecom use="WP" value="tel:(9)-"/>
                                    <playingEntity classCode="PLC">
                                    <name>FC Fairchild Clinics</name>
                                    </playingEntity>
                                </participantRole>
                            </participant>
                        </encounter>
                    </entry>
                    <entry>
                        <encounter classCode="ENC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.49"/>
                            <id nullFlavor="NI"/>
                            <code nullFlavor="UNK">
                                <originalText>Dental</originalText>
                            </code>
                            <effectiveTime>
                                <low value="20170315160000.000-0700"/>
                            </effectiveTime>
                            <participant typeCode="LOC">
                                <participantRole classCode="SDLOC">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.32"/>
                                    <code nullFlavor="NI"/>
                                    <addr use="WP">
                                    <streetAddressLine>9</streetAddressLine>
                                    <city nullFlavor="NI"/>
                                    <state nullFlavor="NI"/>
                                    <postalCode nullFlavor="NI"/>
                                    </addr>
                                    <telecom use="WP" value="tel:(9)-"/>
                                    <playingEntity classCode="PLC">
                                    <name>FC Fairchild Clinics</name>
                                    </playingEntity>
                                </participantRole>
                            </participant>
                        </encounter>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.4"/>
                    <templateId root="2.16.840.1.113883.10.20.22.2.4.1"/>
                    <code code="8716-3"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="Vital Signs"/>
                    <title>Vital Signs</title>
                    <text>
                        <table border="1" width="95%">
                            <colgroup>
                                <col width="20%"/>
                                <col width="20%"/>
                                <col width="20%"/>
                                <col width="20%"/>
                                <col width="20%"/>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th align="right">Most recent to oldest [Reference Range]:</th>
                                    <th>1</th>
                                    <th>2</th>
                                    <th>3</th>
                                    <th>4</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Temperature Tympanic [36.6-38.1 Deg C]</td>
                                    <td>
                                    <content ID="VSEVN7411460">37 Deg C <br/>(1/31/17 4:15 PM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN7410501">37 Deg C <br/>(1/30/17 2:47 PM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN7409857">37 Deg C <br/>(1/28/17 6:48 AM)</content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Temperature Temporal Artery [36.3-37.8 Deg C]</td>
                                    <td>
                                    <content ID="VSEVN7071696">38 Deg C <br/>*HI*<br/>(1/22/17 5:00 PM)</content>
                                    </td>
                                    <td> </td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Peripheral Pulse Rate [60-100 bpm]</td>
                                    <td>
                                    <content ID="VSEVN7411462">58 bpm <br/>*LOW*<br/>(1/31/17 4:15 PM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN7410503">60 bpm <br/>(1/30/17 2:47 PM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN7409859">60 bpm <br/>(1/28/17 6:48 AM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN7071698">100 bpm <br/>(1/22/17 5:00 PM)</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Respiratory Rate [14-20 br/min]</td>
                                    <td>
                                    <content ID="VSEVN7411468">16 br/min <br/>(1/31/17 4:15 PM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN7410509">16 br/min <br/>(1/30/17 2:47 PM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN7409865">16 br/min <br/>(1/28/17 6:48 AM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN7071704">20 br/min <br/>(1/22/17 5:00 PM)</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Blood Pressure [90-140/90 mmHg]</td>
                                    <td>
                                    <content ID="VSEVN75615267561528">
                                    <content
                                    ID="VSEVN7561526">120</content>/<content ID="VSEVN7561528">80</content> mmHg <br/>(2/9/17 1:27 PM)</content>
                                    </td>
                                    <td> </td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Blood Pressure [90-140/60-90 mmHg]</td>
                                    <td>
                                    <content ID="VSEVN74114707411472">
                                    <content
                                    ID="VSEVN7411470">110</content>/<content ID="VSEVN7411472">60</content> mmHg <br/>(1/31/17 4:15 PM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN74105117410513">
                                    <content
                                    ID="VSEVN7410511">110</content>/<content ID="VSEVN7410513">70</content> mmHg <br/>(1/30/17 2:47 PM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN74098677409869">
                                    <content
                                    ID="VSEVN7409867">110</content>/<content ID="VSEVN7409869">62</content> mmHg <br/>(1/28/17 6:48 AM)</content>
                                    </td>
                                    <td>
                                    <content ID="VSEVN70717067071708">
                                    <content
                                    ID="VSEVN7071706">122</content>/<content ID="VSEVN7071708">84</content> mmHg <br/>(1/22/17 5:00 PM)</content>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </text>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="CLUSTER" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.26"/>
                            <id root="22C86399-02F9-4E8B-A14A-F0F71B22F622"/>
                            <code code="46680005"
                                codeSystem="2.16.840.1.113883.6.96"
                                codeSystemName="SNOMED CT" displayName="Vital Signs"/>
                            <statusCode code="completed"/>
                            <effectiveTime value="20170130144700.000-0800"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="BE39A33C-C30A-4017-87BE-29547C77B260"/>
                                    <code code="8480-6"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Systolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7410511"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170130144700.000-0800"/>
                                    <value unit="mm[Hg]" value="110" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170130164831.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>90-140 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="4DC9F84F-43E7-4167-A175-DDA3D477E253"/>
                                    <code code="8462-4"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Diastolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7410513"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170130144700.000-0800"/>
                                    <value unit="mm[Hg]" value="70" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170130164831.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>60-90 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="BA7D0419-DE14-4BC8-8F90-0B38F039B730"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Peripheral Pulse Rate</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7410503"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170130144700.000-0800"/>
                                    <value unit="1" value="60" xsi:type="PQ">
                                    <translation value="60">
                                    <originalText>bpm</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170130164831.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>60-100 bpm</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="304BF5A2-CA45-4DEF-A1B4-AD42F4AADA6B"/>
                                    <code code="9279-1"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Respiratory Rate</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7410509"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170130144700.000-0800"/>
                                    <value unit="1" value="16" xsi:type="PQ">
                                    <translation value="16">
                                    <originalText>br/min</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170130164831.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>14-20 br/min</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="D9F39A75-68B7-40BA-9E8A-1CC0CD876360"/>
                                    <code code="8310-5"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Temperature Tympanic</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7410501"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170130144700.000-0800"/>
                                    <value unit="Cel" value="37" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170130164831.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>36.6-38.1 Deg C</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="CLUSTER" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.26"/>
                            <id root="A05D2A38-8868-4808-81B1-39A26757E9EE"/>
                            <code code="46680005"
                                codeSystem="2.16.840.1.113883.6.96"
                                codeSystemName="SNOMED CT" displayName="Vital Signs"/>
                            <statusCode code="completed"/>
                            <effectiveTime value="20170128064800.000-0800"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="EFC8616C-5C53-4CD9-82A1-8E1C5AB4D853"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Peripheral Pulse Rate</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7409859"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170128064800.000-0800"/>
                                    <value unit="1" value="60" xsi:type="PQ">
                                    <translation value="60">
                                    <originalText>bpm</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170128084918.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>60-100 bpm</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="B51FF640-F4AE-472E-9366-A313E9D5BB96"/>
                                    <code code="8310-5"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Temperature Tympanic</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7409857"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170128064800.000-0800"/>
                                    <value unit="Cel" value="37" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170128084918.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>36.6-38.1 Deg C</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="A4272B96-16F1-4F64-9A47-3D9A88122404"/>
                                    <code code="8480-6"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Systolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7409867"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170128064800.000-0800"/>
                                    <value unit="mm[Hg]" value="110" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170128084918.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>90-140 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="0B410454-90A7-4A77-9401-0405D30EDC24"/>
                                    <code code="8462-4"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Diastolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7409869"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170128064800.000-0800"/>
                                    <value unit="mm[Hg]" value="62" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170128084918.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>60-90 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="D88D5D66-6B19-491E-B569-6226E08C6BB1"/>
                                    <code code="9279-1"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Respiratory Rate</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7409865"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170128064800.000-0800"/>
                                    <value unit="1" value="16" xsi:type="PQ">
                                    <translation value="16">
                                    <originalText>br/min</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170128084918.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>14-20 br/min</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="CLUSTER" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.26"/>
                            <id root="27422B3F-7B2F-4579-8280-BCFB5E50C354"/>
                            <code code="46680005"
                                codeSystem="2.16.840.1.113883.6.96"
                                codeSystemName="SNOMED CT" displayName="Vital Signs"/>
                            <statusCode code="completed"/>
                            <effectiveTime value="20170131161500.000-0800"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="BA3F71F3-3366-4563-A0BA-8D44DF97D741"/>
                                    <code code="8480-6"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Systolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7411470"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170131161500.000-0800"/>
                                    <value unit="mm[Hg]" value="110" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170131181551.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>90-140 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="66225EF6-BA94-4FB1-A947-067DE7B1E999"/>
                                    <code code="8462-4"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Diastolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7411472"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170131161500.000-0800"/>
                                    <value unit="mm[Hg]" value="60" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170131181551.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>60-90 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="D3341D78-FFE8-4BA5-975D-8F789FF4E88E"/>
                                    <code code="9279-1"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Respiratory Rate</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7411468"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170131161500.000-0800"/>
                                    <value unit="1" value="16" xsi:type="PQ">
                                    <translation value="16">
                                    <originalText>br/min</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170131181551.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>14-20 br/min</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="3B17CCDD-6E99-48A8-8E44-C3A54E0427C7"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Peripheral Pulse Rate</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7411462"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170131161500.000-0800"/>
                                    <value unit="1" value="58" xsi:type="PQ">
                                    <translation value="58">
                                    <originalText>bpm</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Low</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170131181551.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>60-100 bpm</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="F41C4747-72AE-44FA-B114-027BEAECF755"/>
                                    <code code="8310-5"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Temperature Tympanic</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7411460"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170131161500.000-0800"/>
                                    <value unit="Cel" value="37" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170131181551.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>36.6-38.1 Deg C</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="CLUSTER" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.26"/>
                            <id root="FFD4EF74-289E-4E9B-BBA8-FB6CF1335075"/>
                            <code code="46680005"
                                codeSystem="2.16.840.1.113883.6.96"
                                codeSystemName="SNOMED CT" displayName="Vital Signs"/>
                            <statusCode code="completed"/>
                            <effectiveTime value="20170122170000.000-0500"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="063E079A-547F-4855-B3CD-6E669EA7D3F8"/>
                                    <code code="8480-6"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Systolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7071706"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122170000.000-0500"/>
                                    <value unit="mm[Hg]" value="122" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170122162834.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>90-140 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="A1233283-0AC8-4CCB-9B62-549667626AC2"/>
                                    <code code="8462-4"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Diastolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7071708"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122170000.000-0500"/>
                                    <value unit="mm[Hg]" value="84" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170122162834.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>60-90 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="1F2DF312-BE11-498C-87C9-0792982F3CD3"/>
                                    <code code="9279-1"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Respiratory Rate</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7071704"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122170000.000-0500"/>
                                    <value unit="1" value="20" xsi:type="PQ">
                                    <translation value="20">
                                    <originalText>br/min</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170122162834.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>14-20 br/min</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="D2D269D2-7D01-45FB-BD6C-2E6ED5002F3A"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Peripheral Pulse Rate</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7071698"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122170000.000-0500"/>
                                    <value unit="1" value="100" xsi:type="PQ">
                                    <translation value="100">
                                    <originalText>bpm</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170122162834.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>60-100 bpm</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="7F50FC15-98DE-4F4B-ACBB-58AE55A4EA2E"/>
                                    <code code="8310-5"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Temperature Temporal Artery</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7071696"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122170000.000-0500"/>
                                    <value unit="Cel" value="38" xsi:type="PQ"/>
                                    <interpretationCode code="H"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>High</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170122162834.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>36.3-37.8 Deg C</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="CLUSTER" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.26"/>
                            <id root="35381570-144F-4A6C-AD9C-E8EB58016429"/>
                            <code code="46680005"
                                codeSystem="2.16.840.1.113883.6.96"
                                codeSystemName="SNOMED CT" displayName="Vital Signs"/>
                            <statusCode code="completed"/>
                            <effectiveTime value="20170209132700.000-0800"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="C02703B5-F581-431E-930F-FF95F7E7108D"/>
                                    <code code="8480-6"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Systolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7561526"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170209132700.000-0800"/>
                                    <value unit="mm[Hg]" value="120" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170209152755.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>90-140 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.27"/>
                                    <id root="B4516157-B54B-4C8C-BCE9-4F22C7B7CEDE"/>
                                    <code code="8462-4"
                                    codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC">
                                    <originalText>Diastolic Blood Pressure</originalText>
                                    </code>
                                    <text>
                                    <reference value="#VSEVN7561528"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170209132700.000-0800"/>
                                    <value unit="mm[Hg]" value="80" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>Normal</originalText>
                                    </interpretationCode>
                                    <author>
                                    <time value="20170209152755.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>90 mmHg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.5"/>
                    <templateId root="2.16.840.1.113883.10.20.22.2.5.1"/>
                    <code code="11450-4"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="Problem List"/>
                    <title>Problem List</title>
                    <text>
                        <table border="1" width="95%">
                            <colgroup>
                                <col width="20%"/>
                                <col width="20%"/>
                                <col width="20%"/>
                                <col width="20%"/>
                                <col width="20%"/>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>Condition</th>
                                    <th>Effective Dates</th>
                                    <th>Status</th>
                                    <th>Health Status</th>
                                    <th>Informant</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376219">Coronary arteriosclerosis (disorder)(<content ID="CON5376219">Confirmed</content>)</content>
                                    </td>
                                    <td>5/13/14</td>
                                    <td>
                                    <content ID="PROBST5376219">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376219">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376301">Asbestos-induced pleural plaque (disorder)(<content ID="CON5376301">Confirmed</content>)</content>
                                    </td>
                                    <td>12/30/09</td>
                                    <td>
                                    <content ID="PROBST5376301">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376301">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376211">Benign neoplasm of skin (disorder)(<content ID="CON5376211">Confirmed</content>)</content>
                                    </td>
                                    <td>12/10/14</td>
                                    <td>
                                    <content ID="PROBST5376211">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376211">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376317">Diabetes mellitus (disorder)(<content ID="CON5376317">Confirmed</content>)</content>
                                    </td>
                                    <td>2/13/11</td>
                                    <td>
                                    <content ID="PROBST5376317">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376317">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376241">Heart murmur (finding)(<content ID="CON5376241">Confirmed</content>)<sup>1</sup>
                                    </content>
                                    </td>
                                    <td>4/1/16</td>
                                    <td>
                                    <content ID="PROBST5376241">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376241">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376265">Toxic effect of gas, fumes AND/OR vapors (disorder)(<content ID="CON5376265">Confirmed</content>)</content>
                                    </td>
                                    <td>12/30/09</td>
                                    <td>
                                    <content ID="PROBST5376265">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376265">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376215">Malignant neoplasm of skin (disorder)(<content ID="CON5376215">Confirmed</content>)</content>
                                    </td>
                                    <td>12/10/14</td>
                                    <td>
                                    <content ID="PROBST5376215">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376215">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376273">Polyp of nasal sinus (disorder)(<content ID="CON5376273">Confirmed</content>)</content>
                                    </td>
                                    <td>12/30/09</td>
                                    <td>
                                    <content ID="PROBST5376273">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376273">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376237">On examination - cold extremities (context-dependent c(<content ID="CON5376237">Confirmed</content>)</content>
                                    </td>
                                    <td>6/4/13</td>
                                    <td>
                                    <content ID="PROBST5376237">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376237">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376233">Single major depressive episode, moderate (disorder)(<content ID="CON5376233">Confirmed</content>)</content>
                                    </td>
                                    <td>6/17/13</td>
                                    <td>
                                    <content ID="PROBST5376233">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376233">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376321">Sinusitis (disorder)(<content ID="CON5376321">Confirmed</content>)</content>
                                    </td>
                                    <td>2/14/16</td>
                                    <td>
                                    <content ID="PROBST5376321">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376321"> </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376369">Tobacco user (finding)(<content ID="CON5376369">Provisional</content>)<sup>2</sup>
                                    </content>
                                    </td>
                                    <td> </td>
                                    <td>
                                    <content ID="PROBST5376369">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376369"> </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content
                                    ID="PROBLEM5376289">Urethral cyst (disorder)(<content ID="CON5376289">Confirmed</content>)</content>
                                    </td>
                                    <td>12/30/09</td>
                                    <td>
                                    <content ID="PROBST5376289">Active</content>
                                    </td>
                                    <td>
                                    <content ID="PROBHST5376289">Chronic ; </content>
                                    </td>
                                    <td> </td>
                                </tr>
                            </tbody>
                        </table>
                        <paragraph>
                            <sup>1</sup>
                            <content ID="PROBCMT5376245">This is written 2016-04-01 at 918EDT. The encounter comment was written same day. Old murmur problem merged with new ICD10 code problem. Date onset updated.</content>
                        </paragraph>
                        <paragraph>
                            <sup>2</sup>
                            <content ID="PROBCMT5376373">Problem added based off tobacco use documented in social history</content>
                        </paragraph>
                    </text>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="A51FD5C2-E119-4E23-B5D0-477DA85C06EA"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20140513"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="9644486D-E9E8-404B-A56C-BFD292794D14"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376219"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20140513"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="53741008"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Coronary arteriosclerosis (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376219"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101803.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376219"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376219"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376219"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376219"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="6DB1A714-122A-4FE0-92DE-6DC4CD83FCDE"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20091230"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="DC064360-4CBA-4481-80B7-0AAC9F35E48C"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376301"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20091230"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="233659006"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Asbestos-induced pleural plaque (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376301"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101800.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376301"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376301"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376301"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376301"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="790FFB52-5DDE-47E7-A84B-1CE21EEECDB6"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20141210"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="66DD98FF-DB8D-4B03-9757-925567687544"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376211"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20141210"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="92384009"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Benign neoplasm of skin (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376211"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101756.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376211"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376211"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376211"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376211"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="D267E24E-9826-4E08-8E35-1019E6405F1C"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20110213"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="E7C5FB61-DF5D-4DA8-AD23-D22560FAA2C7"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376317"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20110213"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="73211009"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Diabetes mellitus (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376317"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101757.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376317"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376317"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376317"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376317"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="D6B36052-F144-4B12-AE61-38D715778723"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20160401"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="75A2B024-9BAD-4A4A-A4A9-16D0CF309CFE"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376241"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20160401"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="88610006"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Heart murmur (finding)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376241"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101806.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376241"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376241"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376241"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376241"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    contextConductionInd="true"
                                    inversionInd="true" typeCode="SUBJ">
                                    <act classCode="ACT" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.64"/>
                                    <code code="48767-8"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Annotation comment"/>
                                    <text>
                                    <reference value="#PROBCMT5376245"/>
                                    </text>
                                    <author typeCode="AUT">
                                    <time nullFlavor="UNK"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>DES</given>
                                    <family>CONTRIBUTOR_SYSTEM</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    </act>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="2DD313C1-DAF8-4B63-A5D8-B383F6E550C0"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20091230"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="3EAC1FA6-0805-49D8-BF54-400FCABDE7BD"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376265"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20091230"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="57335002"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Toxic effect of gas, fumes AND/OR vapors (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376265"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101802.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376265"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376265"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376265"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376265"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="17F50C42-4DCF-4F61-B70F-9ECAD76F62F3"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20141210"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="37E39358-36AF-4560-8084-10439A99A868"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376215"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20141210"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="372130007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Malignant neoplasm of skin (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376215"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101805.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376215"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376215"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376215"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376215"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="7B665100-DAAB-45C1-B48D-AD7DC6F7F188"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20091230"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="D12BBB41-2682-42A0-8E8F-5B85592C0E85"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376273"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20091230"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="32307003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Polyp of nasal sinus (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376273"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101759.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376273"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376273"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376273"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376273"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="3E90AE44-E696-4B41-ADC9-5DE62A48DA16"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20130604"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="0F8CF8DA-4234-45CF-B30B-DBCE95D40A17"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376237"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20130604"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="164447002"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="On examination - cold extremities (context-dependent category)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376237"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101804.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376237"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376237"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376237"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376237"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="64121CF6-991C-4158-9268-5E228418809D"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20130617"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="A7E24375-7856-4DD7-BCB0-CAF481CAD125"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376233"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20130617"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="191602001"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Single major depressive episode, moderate (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376233"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101801.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376233"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376233"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376233"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376233"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="A576BF0F-0FCF-457C-B87A-C4C4A4D0FC73"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20160214"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="84773D91-96D4-4D7B-8170-2C100CB9178C"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376321"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20160214"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="36971009"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Sinusitis (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376321"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170613164646.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376321"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376321"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="883B4F74-AD8F-4F36-85B2-773DAF9CE4A4"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low nullFlavor="NI"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="E1AC2141-37A3-4BDF-BB3A-6C95325DFA4C"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376369"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low nullFlavor="NI"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="110483000"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Tobacco user (finding)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376369"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170613164644.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376369"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376369"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    contextConductionInd="true"
                                    inversionInd="true" typeCode="SUBJ">
                                    <act classCode="ACT" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.64"/>
                                    <code code="48767-8"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Annotation comment"/>
                                    <text>
                                    <reference value="#PROBCMT5376373"/>
                                    </text>
                                    <author typeCode="AUT">
                                    <time value="20170122163718.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>SYSTEM</given>
                                    <given>Cerner</given>
                                    <family>SYSTEM</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    </act>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.3"/>
                            <id root="887A25B7-0C1C-49A7-B92A-5A846412FB15"/>
                            <code code="CONC"
                                codeSystem="2.16.840.1.113883.5.6"
                                codeSystemName="HL7ActClass" displayName="Concern"/>
                            <statusCode code="active"/>
                            <effectiveTime>
                                <low value="20091230"/>
                                <high nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship inversionInd="false" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.4"/>
                                    <id root="C0EC68CD-7FF1-4C59-9602-8165456710A7"/>
                                    <code code="55607006"
                                    codeSystem="2.16.840.1.113883.6.96" displayName="Problem"/>
                                    <text>
                                    <reference value="#PROBLEM5376289"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20091230"/>
                                    <high nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="70795003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Urethral cyst (disorder)" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBLEM5376289"/>
                                    </originalText>
                                    </value>
                                    <author>
                                    <time value="20170615101758.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.6"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <text>
                                    <reference value="#PROBST5376289"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBST5376289"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship typeCode="REFR">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.5"/>
                                    <code code="11323-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Health status"/>
                                    <text>
                                    <reference value="#PROBHST5376289"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#PROBHST5376289"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.6.1"/>
                    <code code="48765-2"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                    <title>Allergies, Adverse Reactions, Alerts</title>
                    <text>
                        <table border="1" width="95%">
                            <colgroup>
                                <col width="25%"/>
                                <col width="45%"/>
                                <col width="15%"/>
                                <col width="15%"/>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>Substance</th>
                                    <th>Reaction</th>
                                    <th>Severity</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4167465">Amoxicillin</content>
                                    </td>
                                    <td> </td>
                                    <td>
                                    <content ID="ALLSEV4167465">Medium</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4167465">Proposed</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4041547">Amoxicillin-Clavulanate ER</content>
                                    </td>
                                    <td>
                                    <content ID="REACTION4041549">wheeze</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSEV4041547">Moderate</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4041547">Active</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4011825">diphenhydramine/HC/nystatin/TCN topical</content>
                                    </td>
                                    <td>
                                    <content ID="REACTION4011827">Vomiting</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSEV4011825"> </content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4011825">Active</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4118963">iodine</content>
                                    </td>
                                    <td>
                                    <content ID="REACTION4118965">Respiratory distress</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSEV4118963">Moderate</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4118963">Active</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4011829">Latex</content>
                                    </td>
                                    <td>
                                    <content ID="REACTION4011831">Rash</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSEV4011829">Moderate</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4011829">Active</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4100587">Meaningful Use Measure-Calculation Placeholder</content>
                                    </td>
                                    <td> </td>
                                    <td>
                                    <content ID="ALLSEV4100587">Medium</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4100587">Proposed</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4011821">PEANUT OIL (PEANUT OIL)</content>
                                    </td>
                                    <td>
                                    <content ID="REACTION4011823">Rash</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSEV4011821"> </content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4011821">Active</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4011835">Pollen</content>
                                    </td>
                                    <td>
                                    <content ID="REACTION4011837">wheeze</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSEV4011835">Moderate</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4011835">Active</content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="ALLERGEN4011817">Sulfa-Drugs</content>
                                    </td>
                                    <td>
                                    <content ID="REACTION4011819">Vomiting</content>
                                    </td>
                                    <td>
                                    <content ID="ALLSEV4011817"> </content>
                                    </td>
                                    <td>
                                    <content ID="ALLSTAT4011817">Active</content>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </text>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="0D95A95B-4D97-4857-9F12-53CFA15DB107"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Proposed"/>
                            <effectiveTime>
                                <low nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="948602E0-1AA5-4899-8EC3-C5EE375B09E5"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="419199007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Allergy to substance" xsi:type="CD"/>
                                    <author>
                                    <time value="20170614010135.000-0400"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code nullFlavor="UNK">
                                    <originalText>
                                    <reference value="#ALLERGEN4167465"/>
                                    </originalText>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4167465"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.8"/>
                                    <code code="SEV"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Severity Observation"/>
                                    <text>
                                    <reference value="#ALLSEV4167465"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#ALLSEV4167465"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="2E122676-1231-49FE-993E-B493DE012581"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Active"/>
                            <effectiveTime>
                                <low value="19900203"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="BFECC911-516D-4758-8160-5AD18B817968"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="19900203"/>
                                    </effectiveTime>
                                    <value code="416098002"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Drug allergy" xsi:type="CD"/>
                                    <author>
                                    <time value="20170130165211.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code code="19711"
                                    codeSystem="2.16.840.1.113883.6.88"
                                    codeSystemName="RxNorm" displayName="Amoxicillin / Clavulanate">
                                    <originalText>
                                    <reference value="#ALLERGEN4041547"/>
                                    </originalText>
                                    <translation
                                    code="d00089"
                                    codeSystem="2.16.840.1.113883.6.314"
                                    codeSystemName="multum-drug-id" displayName="amoxicillin-clavulanate"/>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4041547"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="MFST">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.9"/>
                                    <id root="F5F3232A-7A6B-49DB-8353-9E0D1553968C"/>
                                    <code nullFlavor="UNK"/>
                                    <text>
                                    <reference value="#REACTION4041549"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#REACTION4041549"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.8"/>
                                    <code code="SEV"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Severity Observation"/>
                                    <text>
                                    <reference value="#ALLSEV4041547"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="6736007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#ALLSEV4041547"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="A41AB07E-903F-4168-9CE2-0FE5ED8AC6D4"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Active"/>
                            <effectiveTime>
                                <low value="20091230000000.000-0600"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="CA96C2A0-0D69-4F5E-ADC1-6A97FE346927"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20091230000000.000-0600"/>
                                    </effectiveTime>
                                    <value code="419511003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Propensity to adverse reactions to drug" xsi:type="CD"/>
                                    <author>
                                    <time value="20170122141335.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code nullFlavor="OTH">
                                    <originalText>
                                    <reference value="#ALLERGEN4011825"/>
                                    </originalText>
                                    <translation
                                    code="d07724"
                                    codeSystem="2.16.840.1.113883.6.314"
                                    codeSystemName="multum-drug-id" displayName="diphenhydrAMINE/HC/nystatin/TCN topical"/>
                                    <translation
                                    code="7597"
                                    codeSystem="2.16.840.1.113883.6.88"
                                    codeSystemName="RxNorm" displayName="Nystatin"/>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4011825"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="MFST">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.9"/>
                                    <id root="8B2038CA-19EE-4195-B82E-5B746B09BBF7"/>
                                    <code nullFlavor="UNK"/>
                                    <text>
                                    <reference value="#REACTION4011827"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#REACTION4011827"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="491CF1B5-9D92-4456-8416-C96CB3568FA9"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Active"/>
                            <effectiveTime>
                                <low value="20000102"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="93D74BC1-EEBC-4CD1-81DA-8C8960C157EA"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20000102"/>
                                    </effectiveTime>
                                    <value code="419199007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Allergy to substance" xsi:type="CD"/>
                                    <author>
                                    <time value="20170327121525.000-0400"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code code="5933"
                                    codeSystem="2.16.840.1.113883.6.88"
                                    codeSystemName="RxNorm" displayName="Iodine">
                                    <originalText>
                                    <reference value="#ALLERGEN4118963"/>
                                    </originalText>
                                    <translation
                                    code="d05776"
                                    codeSystem="2.16.840.1.113883.6.314"
                                    codeSystemName="multum-drug-id" displayName="iodine"/>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4118963"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="MFST">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.9"/>
                                    <id root="A27C3275-8A3F-4D34-BC82-5EB064FBE564"/>
                                    <code nullFlavor="UNK"/>
                                    <text>
                                    <reference value="#REACTION4118965"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#REACTION4118965"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.8"/>
                                    <code code="SEV"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Severity Observation"/>
                                    <text>
                                    <reference value="#ALLSEV4118963"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="6736007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#ALLSEV4118963"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="07CD86C0-129A-461D-9E59-3669A243BEFE"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Active"/>
                            <effectiveTime>
                                <low value="20000201"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="687935B1-5CCF-4A13-9C8D-29701B51368B"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20000201"/>
                                    </effectiveTime>
                                    <value code="419199007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Allergy to substance" xsi:type="CD"/>
                                    <author>
                                    <time value="20170122163242.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code nullFlavor="UNK">
                                    <originalText>
                                    <reference value="#ALLERGEN4011829"/>
                                    </originalText>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4011829"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="MFST">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.9"/>
                                    <id root="919C7B05-FAE1-40CF-9337-9FFCF597F9E4"/>
                                    <code nullFlavor="UNK"/>
                                    <text>
                                    <reference value="#REACTION4011831"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#REACTION4011831"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.8"/>
                                    <code code="SEV"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Severity Observation"/>
                                    <text>
                                    <reference value="#ALLSEV4011829"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="6736007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#ALLSEV4011829"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="1E303105-4E7B-4719-BF01-44DE4F1C36FA"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Proposed"/>
                            <effectiveTime>
                                <low nullFlavor="NI"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="5CA6E4B8-472B-4EC6-9C17-823582D36802"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low nullFlavor="NI"/>
                                    </effectiveTime>
                                    <value code="416098002"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Drug allergy" xsi:type="CD"/>
                                    <author>
                                    <time value="20170303233717.000-0500"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code nullFlavor="UNK">
                                    <originalText>
                                    <reference value="#ALLERGEN4100587"/>
                                    </originalText>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4100587"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.8"/>
                                    <code code="SEV"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Severity Observation"/>
                                    <text>
                                    <reference value="#ALLSEV4100587"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#ALLSEV4100587"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="F774C77B-7996-446B-90B0-03A8127DDFA5"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Active"/>
                            <effectiveTime>
                                <low value="20091230000000.000-0600"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="C973A008-C48A-4C2E-9EE8-9F47A8C3B11E"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20091230000000.000-0600"/>
                                    </effectiveTime>
                                    <value code="419511003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Propensity to adverse reactions to drug" xsi:type="CD"/>
                                    <author>
                                    <time value="20170122141335.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code nullFlavor="UNK">
                                    <originalText>
                                    <reference value="#ALLERGEN4011821"/>
                                    </originalText>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4011821"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="MFST">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.9"/>
                                    <id root="B6FD93C0-D3BD-4B43-8539-75E7B5D7DDAC"/>
                                    <code nullFlavor="UNK"/>
                                    <text>
                                    <reference value="#REACTION4011823"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#REACTION4011823"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="B57B3021-8FAB-4B35-BB6B-FE7B72CE5091"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Active"/>
                            <effectiveTime>
                                <low value="19700310"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="E0481BEC-8300-49D9-A795-9DE3B2966A8C"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="19700310"/>
                                    </effectiveTime>
                                    <value code="419199007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Allergy to substance" xsi:type="CD"/>
                                    <author>
                                    <time value="20170122163409.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code nullFlavor="UNK">
                                    <originalText>
                                    <reference value="#ALLERGEN4011835"/>
                                    </originalText>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4011835"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="MFST">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.9"/>
                                    <id root="3EEABB3D-D856-4735-82DB-A5B2A1F59D9E"/>
                                    <code nullFlavor="UNK"/>
                                    <text>
                                    <reference value="#REACTION4011837"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#REACTION4011837"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.8"/>
                                    <code code="SEV"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Severity Observation"/>
                                    <text>
                                    <reference value="#ALLSEV4011835"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value code="6736007"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CD">
                                    <originalText>
                                    <reference value="#ALLSEV4011835"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <act classCode="ACT" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.30"/>
                            <id root="10BE6944-6543-4DFD-9908-6FBF29A897AC"/>
                            <code code="48765-2"
                                codeSystem="2.16.840.1.113883.6.1"
                                codeSystemName="LOINC" displayName="Allergies, adverse reactions, alerts"/>
                            <statusCode code="Active"/>
                            <effectiveTime>
                                <low value="20100326000000.000-0500"/>
                            </effectiveTime>
                            <entryRelationship
                                contextConductionInd="true" typeCode="SUBJ">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.7"/>
                                    <id root="66E7AB16-6624-4A6B-BF05-54BD4220A093"/>
                                    <code code="ASSERTION"
                                    codeSystem="2.16.840.1.113883.5.4"
                                    codeSystemName="HL7 ActCode" displayName="Assertion"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime>
                                    <low value="20100326000000.000-0500"/>
                                    </effectiveTime>
                                    <value code="419511003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT"
                                    displayName="Propensity to adverse reactions to drug" xsi:type="CD"/>
                                    <author>
                                    <time value="20170122141335.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <participant contextControlCode="OP" typeCode="CSM">
                                    <participantRole classCode="MANU">
                                    <playingEntity classCode="MMAT">
                                    <code nullFlavor="UNK">
                                    <originalText>
                                    <reference value="#ALLERGEN4011817"/>
                                    </originalText>
                                    </code>
                                    </playingEntity>
                                    </participantRole>
                                    </participant>
                                    <entryRelationship
                                    inversionInd="true" typeCode="SUBJ">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.28"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value code="55561003"
                                    codeSystem="2.16.840.1.113883.6.96"
                                    codeSystemName="SNOMED CT" xsi:type="CE">
                                    <originalText>
                                    <reference value="#ALLSTAT4011817"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                    <entryRelationship
                                    inversionInd="true" typeCode="MFST">
                                    <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.9"/>
                                    <id root="31E08455-DE4C-4E83-8560-86765FF95165"/>
                                    <code nullFlavor="UNK"/>
                                    <text>
                                    <reference value="#REACTION4011819"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#REACTION4011819"/>
                                    </originalText>
                                    </value>
                                    </observation>
                                    </entryRelationship>
                                </observation>
                            </entryRelationship>
                        </act>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.1"/>
                    <templateId root="2.16.840.1.113883.10.20.22.2.1.1"/>
                    <code code="10160-0"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="History of Medication Use"/>
                    <title>Medications</title>
                    <text>
                        <paragraph ID="MEDICATION122257111">
                            <content ID="MEDPROD122257111" styleCode="Bold">acetaminophen 120 mg rectal suppository</content>
                            <content ID="MEDSIG122257111">
                                <br/>See Instructions, PRN fever, 2 supp Rectal every 4 hr, # 12 supp, 0 Refill(s), 05/19/2017, DoD pharmacy dispense (Rx)</content>
                            <br/>Start Date: 5/18/17<br/>Stop Date: 5/19/17<br/>Status: Completed</paragraph>
                    </text>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <substanceAdministration classCode="SBADM" moodCode="INT">
                            <templateId root="2.16.840.1.113883.10.20.22.4.16"/>
                            <id root="CDB50DFA-EEB3-4DBE-99CA-024BBA3E485D"/>
                            <text>
                                <reference value="#MEDSIG122257111"/>
                            </text>
                            <statusCode code="Completed"/>
                            <effectiveTime xsi:type="IVL_TS">
                                <low value="20170518154700.000-0700"/>
                                <high value="20170519000000.000-0700"/>
                            </effectiveTime>
                            <routeCode nullFlavor="NI"/>
                            <administrationUnitCode nullFlavor="UNK">
                                <originalText>Supp-Rectal</originalText>
                            </administrationUnitCode>
                            <consumable typeCode="CSM">
                                <manufacturedProduct classCode="MANU">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.23"/>
                                    <manufacturedMaterial
                                    classCode="MMAT" determinerCode="KIND">
                                    <code nullFlavor="OTH">
                                    <originalText>
                                    <reference value="#MEDPROD122257111"/>
                                    </originalText>
                                    <translation code="d00049"
                                    codeSystem="2.16.840.1.113883.6.314" codeSystemName="multum-drug-id"/>
                                    <translation code="23348"
                                    codeSystem="2.16.840.1.113883.6.312" codeSystemName="multum-drug-synonym-id"/>
                                    <translation code="198434"
                                    codeSystem="2.16.840.1.113883.6.88"
                                    codeSystemName="RxNorm" displayName="Acetaminophen 120 MG Rectal Suppository"/>
                                    </code>
                                    </manufacturedMaterial>
                                </manufacturedProduct>
                            </consumable>
                            <author>
                                <time value="20170519020106.000-0500"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                            <entryRelationship typeCode="REFR">
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.1.47"/>
                                    <templateId root="2.16.840.1.113883.10.20.1.57"/>
                                    <code code="33999-4"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="Status"/>
                                    <statusCode code="completed"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>Completed</originalText>
                                    </value>
                                </observation>
                            </entryRelationship>
                            <entryRelationship typeCode="REFR">
                                <supply classCode="SPLY" moodCode="INT">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.17"/>
                                    <id root="BE406E62-F67B-4EA9-940F-F7FD9F195F7E"/>
                                    <statusCode code="completed"/>
                                    <effectiveTime xsi:type="IVL_TS">
                                    <high value="20170519000000.000-0700"/>
                                    </effectiveTime>
                                    <repeatNumber value="1"/>
                                    <quantity unit="1" value="12.0">
                                    <translation value="12.0">
                                    <originalText>supp</originalText>
                                    </translation>
                                    </quantity>
                                    <product typeCode="PRD">
                                    <manufacturedProduct classCode="MANU">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.23"/>
                                    <manufacturedMaterial
                                    classCode="MMAT" determinerCode="KIND">
                                    <code nullFlavor="OTH">
                                    <originalText>
                                    <reference value="#MEDPROD122257111"/>
                                    </originalText>
                                    <translation
                                    code="d00049"
                                    codeSystem="2.16.840.1.113883.6.314" codeSystemName="multum-drug-id"/>
                                    <translation
                                    code="23348"
                                    codeSystem="2.16.840.1.113883.6.312" codeSystemName="multum-drug-synonym-id"/>
                                    <translation
                                    code="198434"
                                    codeSystem="2.16.840.1.113883.6.88"
                                    codeSystemName="RxNorm" displayName="Acetaminophen 120 MG Rectal Suppository"/>
                                    </code>
                                    </manufacturedMaterial>
                                    </manufacturedProduct>
                                    </product>
                                </supply>
                            </entryRelationship>
                        </substanceAdministration>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.3"/>
                    <templateId root="2.16.840.1.113883.10.20.22.2.3.1"/>
                    <code code="30954-2"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="Relevant diagnostic tests and/or laboratory data"/>
                    <title>Results</title>
                    <text>
                        <paragraph styleCode="Bold Underline">Hematology</paragraph>
                        <table border="1" width="95%">
                            <colgroup>
                                <col width="20%"/>
                                <col width="40%"/>
                                <col width="40%"/>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th align="right">Most recent to oldest [Reference Range]:</th>
                                    <th>1</th>
                                    <th>2</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>WBC [3.5-11.0 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480673">6.0 10^3/uL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>WBC [3.6-11.1 K/mcL]</td>
                                    <td>
                                    <content ID="RESEVN7071752">3.5 K/mcL <br/>*LOW*<br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>RBC [4.63-6.08 10^6/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480675">5.00 10^6/uL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>RBC [4.27-5.73 x10^6/mcL]</td>
                                    <td>
                                    <content ID="RESEVN7071754">4.32 x10^6/mcL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Hemoglobin [13.7-17.5 g/dL]</td>
                                    <td>
                                    <content ID="RESEVN7480677">15.0 g/dL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td>
                                    <content ID="RESEVN7409853">14.0 g/dL <br/>(1/28/17 6:42 AM) </content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Hemoglobin [12.9-16.1 g/dL]</td>
                                    <td>
                                    <content ID="RESEVN7071756">14.0 g/dL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Hematocrit [40.1-51.0 %]</td>
                                    <td>
                                    <content ID="RESEVN7480679">45.0 % <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td>
                                    <content ID="RESEVN7409855">41.0 % <br/>(1/28/17 6:42 AM) </content>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Hematocrit [37.7-51.3 %]</td>
                                    <td>
                                    <content ID="RESEVN7071758">38.0 % <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>MCV [79.0-92.2 fL]</td>
                                    <td>
                                    <content ID="RESEVN7480681">88.0 fL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>MCV [79-99 fL]</td>
                                    <td>
                                    <content ID="RESEVN7071760">81 fL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>MCH [25.7-32.2 pg]</td>
                                    <td>
                                    <content ID="RESEVN7480683">30.0 pg <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>MCH [28.0-32.0 pg]</td>
                                    <td>
                                    <content ID="RESEVN7071762">30.0 pg <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>MCHC [32.3-36.5 g/dL]</td>
                                    <td>
                                    <content ID="RESEVN7480685">33.0 g/dL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>MCHC [32.0-36.0 g/dL]</td>
                                    <td>
                                    <content ID="RESEVN7071764">33.0 g/dL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>RDW [11.6-14.4 %]</td>
                                    <td>
                                    <content ID="RESEVN7480687">14.0 % <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>RDW [11.5-14.5 units]</td>
                                    <td>
                                    <content ID="RESEVN7071766">12.0 units <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Platelets [163-337 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480689">225 10^3/uL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Platelets [150-450 K/mcL]</td>
                                    <td>
                                    <content ID="RESEVN7071768">151 K/mcL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>MPV [9.4-12.4 fL]</td>
                                    <td>
                                    <content ID="RESEVN7480691">12.0 fL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>MPV</td>
                                    <td>
                                    <content ID="RESEVN7071770">10.0 fL <br/>*NA*<br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Differential? [Auto]</td>
                                    <td>
                                    <content ID="RESEVN7480693">Auto <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Neutrophil % Auto [34.0-67.9 %]</td>
                                    <td>
                                    <content ID="RESEVN7480697">55.0 % <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Neutrophil % Auto [35.0-75.0 %]</td>
                                    <td>
                                    <content ID="RESEVN7071774">2.5 % <br/>*LOW*<br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Lymphocyte % Auto [21.8-53.1 %]</td>
                                    <td>
                                    <content ID="RESEVN7480699">44.0 % <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Lymphocyte % Auto [15.0-49.0 %]</td>
                                    <td>
                                    <content ID="RESEVN7071776">7.0 % <br/>*LOW*<br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Monocyte % Auto [4.0-12.5 %]</td>
                                    <td>
                                    <content ID="RESEVN7480701">1.0 % <br/>*LOW*<br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Monocyte % Auto [1.0-10.0 %]</td>
                                    <td>
                                    <content ID="RESEVN7071778">6.0 % <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Eosinophil % Auto [0.0-6.0 %]</td>
                                    <td>
                                    <content ID="RESEVN7480703">0.0 % <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Eosinophil % Auto [0.0-5.0 %]</td>
                                    <td>
                                    <content ID="RESEVN7071780">5.0 % <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Basophil % Auto [0.2-1.2 %]</td>
                                    <td>
                                    <content ID="RESEVN7480705">0.0 % <br/>*LOW*<br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Basophil % Auto [0.0-2.0 %]</td>
                                    <td>
                                    <content ID="RESEVN7071782">2.0 % <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Neutro Absolute [1.78-7.00 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480709">4.00 10^3/uL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Neutro Absolute [2.0-8.0 K/mcL]</td>
                                    <td>
                                    <content ID="RESEVN7071784">5.0 K/mcL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Lymph Absolute [1.32-3.57 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480711">3.00 10^3/uL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Lymph Absolute [0.6-4.8 K/mcL]</td>
                                    <td>
                                    <content ID="RESEVN7071786">3.0 K/mcL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Mono Absolute [0.30-0.90 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480713">0.30 10^3/uL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Mono Absolute [0.1-2.0 K/mcL]</td>
                                    <td>
                                    <content ID="RESEVN7071788">2.0 K/mcL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Eos Absolute [0.04-0.54 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480715">0.00 10^3/uL <br/>*LOW*<br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Eos Absolute [0.0-0.7 K/mcL]</td>
                                    <td>
                                    <content ID="RESEVN7071790">0.5 K/mcL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Baso Absolute [0.01-0.30 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480717">0.00 10^3/uL <br/>*LOW*<br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Baso Absolute [0.0-0.2 K/mcL]</td>
                                    <td>
                                    <content ID="RESEVN7071792">0.3 K/mcL <br/>*HI*<br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>nRBC % Auto [0.0-0.2 /100 WBC]</td>
                                    <td>
                                    <content ID="RESEVN7480719">0.0 /100 WBC <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>nRBC % Auto</td>
                                    <td>
                                    <content ID="RESEVN7071796">1 <br/>*NA*<br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>nRBC Absolute [0.000-0.012 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7480721">0.000 10^3/uL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>nRBC Absolute [0-0 10^3/uL]</td>
                                    <td>
                                    <content ID="RESEVN7071794">0 10^3/uL <br/>(1/22/17 6:09 PM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                            </tbody>
                        </table>
                        <paragraph styleCode="Bold Underline">Chemistry</paragraph>
                        <table border="1" width="95%">
                            <colgroup>
                                <col width="20%"/>
                                <col width="40%"/>
                                <col width="40%"/>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th align="right">Most recent to oldest [Reference Range]:</th>
                                    <th>1</th>
                                    <th>2</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Glucose Lvl [65-99 mg/dL]</td>
                                    <td>
                                    <content ID="RESEVN7480731">88 mg/dL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>BUN [9.00-20.00 mg/dL]</td>
                                    <td>
                                    <content ID="RESEVN7480733">18.00 mg/dL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Creatinine Level [0.70-1.30 mg/dL]</td>
                                    <td>
                                    <content ID="RESEVN7480745">2.00 mg/dL <br/>*HI*<br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Calcium [8.4-10.2 mg/dL]</td>
                                    <td>
                                    <content ID="RESEVN7480747">10.0 mg/dL <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Sodium [135-147 mmol/L]</td>
                                    <td>
                                    <content ID="RESEVN7480735">143 mmol/L <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Potassium Lvl [3.5-5.3 mmol/L]</td>
                                    <td>
                                    <content ID="RESEVN7480737">5.0 mmol/L <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>Chloride [98.0-107.0 mmol/L]</td>
                                    <td>
                                    <content ID="RESEVN7480739">99.0 mmol/L <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>CO2 [22.00-30.00 mmol/L]</td>
                                    <td>
                                    <content ID="RESEVN7480741">29.00 mmol/L <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>AGAP [10-20 mmol/L]</td>
                                    <td>
                                    <content ID="RESEVN7480743">20 mmol/L <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>eGFR Non-AA [&gt;=60 mL/min/1.73 m2]</td>
                                    <td>
                                    <content ID="RESEVN7480758">35 mL/min/1.73 m2 <br/>*LOW*<br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>eGFR AA [&gt;=60 mL/min/1.73 m2]</td>
                                    <td>
                                    <content ID="RESEVN7480756">42 mL/min/1.73 m2 <br/>*LOW*<br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>BUN/Creat Ratio [7-25]</td>
                                    <td>
                                    <content ID="RESEVN7480749">9 <br/>(2/8/17 7:18 AM) </content>
                                    </td>
                                    <td> </td>
                                </tr>
                            </tbody>
                        </table>
                    </text>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.1"/>
                            <id root="0FDCD942-4385-41F4-A953-526D18E0AF46"/>
                            <code nullFlavor="UNK" xsi:type="CD">
                                <originalText>Hematology</originalText>
                            </code>
                            <statusCode code="completed"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="92F3D029-77F2-4BC0-A229-26787BA3290F"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Platelets</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071768"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="151" xsi:type="PQ">
                                    <translation value="151">
                                    <originalText>K/mcL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>150-450 K/mcL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="A814C65F-48F9-413D-96A7-D9848E2F3D6F"/>
                                    <code nullFlavor="UNK">
                                    <originalText>MCHC</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071764"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="g/dL" value="33.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>32.0-36.0 g/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="BD619360-2462-415B-A427-E4189569BD7C"/>
                                    <code nullFlavor="UNK">
                                    <originalText>MCH</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071762"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="pg" value="30.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>28.0-32.0 pg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="3298E235-E0D3-4F22-950D-537BBAE51507"/>
                                    <code nullFlavor="UNK">
                                    <originalText>MCV</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071760"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="fL" value="81" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>79-99 fL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="BB5AE235-26D0-4D41-813C-7969297A979B"/>
                                    <code code="20570-8"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="HEMATOCRIT:VFR:PT:BLD:QN:">
                                    <originalText>Hematocrit</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071758"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="%" value="38.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>37.7-51.3 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="6C30229E-F3C3-4039-B0A1-39943BA69736"/>
                                    <code nullFlavor="UNK">
                                    <originalText>RDW</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071766"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="12.0" xsi:type="PQ">
                                    <translation value="12.0">
                                    <originalText>units</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>11.5-14.5 units</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="0C35FDE5-8E55-4F39-B832-F0E0BBFB6DA7"/>
                                    <code nullFlavor="UNK">
                                    <originalText>WBC</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071752"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="3.5" xsi:type="PQ">
                                    <translation value="3.5">
                                    <originalText>K/mcL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>3.6-11.1 K/mcL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="69AD19FF-2AFB-44B6-A8E1-FEBFDBB322F7"/>
                                    <code code="20509-6"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="HEMOGLOBIN:MCNC:PT:BLD:QN:CALCULATED">
                                    <originalText>Hemoglobin</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071756"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="g/dL" value="14.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>12.9-16.1 g/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="2C7E8A48-A1DF-4585-AC57-D672958CE52C"/>
                                    <code nullFlavor="UNK">
                                    <originalText>RBC</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071754"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="4.32" xsi:type="PQ">
                                    <translation value="4.32">
                                    <originalText>x10^6/mcL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>4.27-5.73 x10^6/mcL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="0D46EBE5-2C99-4461-B00B-CA28804C7691"/>
                                    <code nullFlavor="UNK">
                                    <originalText>MPV</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071770"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="fL" value="10.0" xsi:type="PQ"/>
                                    <interpretationCode nullFlavor="UNK">
                                    <originalText>NA</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.1"/>
                            <id root="EA8A3CA6-8A4F-4A13-86C9-536D86E0D950"/>
                            <code nullFlavor="UNK" xsi:type="CD">
                                <originalText>Hematology</originalText>
                            </code>
                            <statusCode code="completed"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="6D352D5B-0E72-41C3-B23D-87326EB27411"/>
                                    <code nullFlavor="UNK">
                                    <originalText>nRBC % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071796"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value value="1" xsi:type="REAL"/>
                                    <interpretationCode nullFlavor="UNK">
                                    <originalText>NA</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="32EAD3B4-925D-4955-B025-6577665DE6D5"/>
                                    <code nullFlavor="UNK">
                                    <originalText>nRBC Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071794"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="0" xsi:type="PQ">
                                    <translation value="0">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0-0 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="4DF5F3BF-4C6E-4AAA-952C-26375CFB77CC"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Baso Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071792"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="0.3" xsi:type="PQ">
                                    <translation value="0.3">
                                    <originalText>K/mcL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="H"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>HI</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.0-0.2 K/mcL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="F2C3B49B-C1FD-4E5A-A8B8-C8ABD5ED3065"/>
                                    <code code="26449-9"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="EOSINOPHILS:NCNC:PT:BLD:QN:">
                                    <originalText>Eos Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071790"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="0.5" xsi:type="PQ">
                                    <translation value="0.5">
                                    <originalText>K/mcL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.0-0.7 K/mcL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="B133B964-BDAE-4357-9747-FCE6447B5917"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Lymph Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071786"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="3.0" xsi:type="PQ">
                                    <translation value="3.0">
                                    <originalText>K/mcL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.6-4.8 K/mcL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="A30DE7D5-F874-4A17-B641-B2CA73A98266"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Basophil % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071782"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="%" value="2.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.0-2.0 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="57ACF935-8C30-44AD-BD96-D163E0216799"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Eosinophil % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071780"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="%" value="5.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.0-5.0 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="D5601F06-DE08-40AC-809B-BC642454724E"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Mono Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071788"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="2.0" xsi:type="PQ">
                                    <translation value="2.0">
                                    <originalText>K/mcL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.1-2.0 K/mcL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="96F1143D-51F6-403E-9615-28833A61444C"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Neutro Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071784"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="1" value="5.0" xsi:type="PQ">
                                    <translation value="5.0">
                                    <originalText>K/mcL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>2.0-8.0 K/mcL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="6537EFED-03AE-4C92-BE09-BC1CD6032237"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Monocyte % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071778"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="%" value="6.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>1.0-10.0 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="9CC4E405-00FC-4895-B175-0AAB3EDB0EBF"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Lymphocyte % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071776"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="%" value="7.0" xsi:type="PQ"/>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>15.0-49.0 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="947F0DFA-554E-4A39-B0BB-AD6896CF31C8"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Neutrophil % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7071774"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170122180900.000-0500"/>
                                    <value unit="%" value="2.5" xsi:type="PQ"/>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170122172917.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>35.0-75.0 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.1"/>
                            <id root="D05F63E1-8220-47A2-B7F3-6445299F3A28"/>
                            <code nullFlavor="UNK" xsi:type="CD">
                                <originalText>Chemistry</originalText>
                            </code>
                            <statusCode code="completed"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="DEDCDC16-7CA4-4488-8578-122CC78349DC"/>
                                    <code nullFlavor="UNK">
                                    <originalText>eGFR Non-AA</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480758"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="35" xsi:type="PQ">
                                    <translation value="35">
                                    <originalText>mL/min/1.73 m2</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170208072526.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>SYSTEM</given>
                                    <given>Cerner</given>
                                    <family>SYSTEM</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>&gt;=60 mL/min/1.73 m2</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="B4B9A044-FF7D-4D5C-AA41-9AECA46EF604"/>
                                    <code nullFlavor="UNK">
                                    <originalText>eGFR AA</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480756"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="42" xsi:type="PQ">
                                    <translation value="42">
                                    <originalText>mL/min/1.73 m2</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170208072525.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>SYSTEM</given>
                                    <given>Cerner</given>
                                    <family>SYSTEM</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>&gt;=60 mL/min/1.73 m2</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.1"/>
                            <id root="29C22ACE-CCAD-4793-936B-76A05EF6C35A"/>
                            <code nullFlavor="UNK" xsi:type="CD">
                                <originalText>Hematology</originalText>
                            </code>
                            <statusCode code="completed"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="D644FB69-D2DA-4C0F-BD06-79AC8C508368"/>
                                    <code nullFlavor="UNK">
                                    <originalText>nRBC Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480721"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="0.000" xsi:type="PQ">
                                    <translation value="0.000">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.000-0.012 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="DDFFEFFB-A492-45E7-9F0E-C7D15ED26F98"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Neutro Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480709"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="4.00" xsi:type="PQ">
                                    <translation value="4.00">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>1.78-7.00 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="1A8E9361-CBCC-4E84-9D59-BF0E1D6E47B7"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Monocyte % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480701"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="%" value="1.0" xsi:type="PQ"/>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>4.0-12.5 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="B5AE3015-838F-4247-9FA1-3E660DC073A2"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Basophil % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480705"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="%" value="0.0" xsi:type="PQ"/>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.2-1.2 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="300607A4-A2AA-4BCB-A0DD-C090A544D0CD"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Eosinophil % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480703"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="%" value="0.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.0-6.0 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="80204BB5-C73F-4816-966C-C95C322C1C7B"/>
                                    <code nullFlavor="UNK">
                                    <originalText>nRBC % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480719"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="0.0" xsi:type="PQ">
                                    <translation value="0.0">
                                    <originalText>/100 WBC</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.0-0.2 /100 WBC</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="EEE49F3B-0DD9-44CD-8133-E9DF7EFF9ACE"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Mono Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480713"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="0.30" xsi:type="PQ">
                                    <translation value="0.30">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.30-0.90 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="E97CD7A8-EAA8-420F-A3A6-DB33DD576A1A"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Lymph Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480711"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="3.00" xsi:type="PQ">
                                    <translation value="3.00">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>1.32-3.57 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="BA149285-C1EA-4475-8C77-2AF16C278E67"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Baso Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480717"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="0.00" xsi:type="PQ">
                                    <translation value="0.00">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.01-0.30 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="2949465C-7E5A-47F8-B723-11AF2932D816"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Eos Absolute</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480715"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="0.00" xsi:type="PQ">
                                    <translation value="0.00">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="L"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>LOW</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.04-0.54 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="CABC6471-57FD-422F-B5D0-A805116453EF"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Neutrophil % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480697"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="%" value="55.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>34.0-67.9 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="59A719F7-51AD-4DBC-A2E4-932DB14D920E"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Lymphocyte % Auto</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480699"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="%" value="44.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>21.8-53.1 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.1"/>
                            <id root="64F6138D-32E7-4700-A0E4-A46927EA4DA4"/>
                            <code nullFlavor="UNK" xsi:type="CD">
                                <originalText>Hematology</originalText>
                            </code>
                            <statusCode code="completed"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="B022748B-77B7-482E-8B64-332DCE170EF1"/>
                                    <code nullFlavor="UNK">
                                    <originalText>WBC</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480673"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="6.0" xsi:type="PQ">
                                    <translation value="6.0">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>3.5-11.0 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="C885D8D8-C864-4899-92D3-A8371B4EC737"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Hemoglobin</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480677"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="g/dL" value="15.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>13.7-17.5 g/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="7BFFEC77-4C36-4188-968D-31D93523533C"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Hematocrit</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480679"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="%" value="45.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>40.1-51.0 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="8C7BB010-9C4E-4373-9267-320D89C0BF42"/>
                                    <code nullFlavor="UNK">
                                    <originalText>RBC</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480675"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="5.00" xsi:type="PQ">
                                    <translation value="5.00">
                                    <originalText>10^6/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>4.63-6.08 10^6/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="1FA533E6-B464-4076-9D39-2A91A6223F72"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Platelets</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480689"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="1" value="225" xsi:type="PQ">
                                    <translation value="225">
                                    <originalText>10^3/uL</originalText>
                                    </translation>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>163-337 10^3/uL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="6CBC0ACF-2423-4EF6-8AAE-8D62AB2BB34E"/>
                                    <code nullFlavor="UNK">
                                    <originalText>RDW</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480687"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="%" value="14.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>11.6-14.4 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="B24264D9-C8F5-4A01-92BC-8040A53E9366"/>
                                    <code nullFlavor="UNK">
                                    <originalText>MCV</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480681"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="fL" value="88.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>79.0-92.2 fL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="B96CDE56-687D-4BF3-A645-D511D0CA6CE8"/>
                                    <code nullFlavor="UNK">
                                    <originalText>MPV</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480691"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="fL" value="12.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>9.4-12.4 fL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="712509F5-4E1C-4748-9C3B-822427FC88BC"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Differential?</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480693"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value nullFlavor="UNK" xsi:type="CD">
                                    <originalText>
                                    <reference value="#RESEVN7480693"/>
                                    </originalText>
                                    </value>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>Auto</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="2F185CA9-27AB-47A3-9572-498E7E8B27D7"/>
                                    <code nullFlavor="UNK">
                                    <originalText>MCHC</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480685"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="g/dL" value="33.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>32.3-36.5 g/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="023E341F-8448-4149-9CF7-DE82B428D5CA"/>
                                    <code nullFlavor="UNK">
                                    <originalText>MCH</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480683"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="pg" value="30.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072422.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>25.7-32.2 pg</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.1"/>
                            <id root="CF218DA6-D0D5-41D8-8D43-149E63A699D1"/>
                            <code nullFlavor="UNK" xsi:type="CD">
                                <originalText>Chemistry</originalText>
                            </code>
                            <statusCode code="completed"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="5FF0E2E7-6380-40CE-A03B-57705949B333"/>
                                    <code code="74774-1"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="GLUCOSE:MCNC:PT:SER/PLAS/BLD:QN:">
                                    <originalText>Glucose Lvl</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480731"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mg/dL" value="88" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>65-99 mg/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="C3B77B11-A437-41D5-9FA4-F601CBA0564B"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Sodium</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480735"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mmol/L" value="143" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>135-147 mmol/L</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="F19DA6A3-DBCF-4AE9-9E18-E93537A13EFC"/>
                                    <code code="14937-7"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="UREA NITROGEN:SCNC:PT:SER/PLAS:QN:">
                                    <originalText>BUN</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480733"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mg/dL" value="18.00" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>9.00-20.00 mg/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="2B827A18-6AA9-49E4-ABE0-917D1B5C4B11"/>
                                    <code code="2075-0"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="CHLORIDE:SCNC:PT:SER/PLAS:QN:">
                                    <originalText>Chloride</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480739"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mmol/L" value="99.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>98.0-107.0 mmol/L</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="026B17F8-E9FF-46C6-B1A8-9D0DC8D6178F"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Potassium Lvl</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480737"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mmol/L" value="5.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>3.5-5.3 mmol/L</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="7927E43D-C9B4-42D5-9F35-FB1DE883C3DA"/>
                                    <code code="2000-8"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="CALCIUM:SCNC:PT:SER/PLAS:QN:">
                                    <originalText>Calcium</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480747"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mg/dL" value="10.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>8.4-10.2 mg/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="B57E4C8C-A29A-4C99-8BD1-F4C55D9836D8"/>
                                    <code code="2028-9"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="CARBON DIOXIDE:SCNC:PT:SER/PLAS:QN:">
                                    <originalText>CO2</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480741"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mmol/L" value="29.00" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>22.00-30.00 mmol/L</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="EEDC1A13-A64D-4F7E-A76D-6C484A5E4DC1"/>
                                    <code code="14682-9"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="CREATININE:SCNC:PT:SER/PLAS:QN:">
                                    <originalText>Creatinine Level</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480745"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mg/dL" value="2.00" xsi:type="PQ"/>
                                    <interpretationCode code="H"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation">
                                    <originalText>HI</originalText>
                                    </interpretationCode>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>0.70-1.30 mg/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="C33B7EF6-EADF-4B38-9118-7B65CED45926"/>
                                    <code code="33037-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="ANION GAP:SCNC:PT:SER/PLAS:QN:">
                                    <originalText>AGAP</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480743"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value unit="mmol/L" value="20" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>10-20 mmol/L</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="5A143A39-3E8A-47EF-8EA2-620304DBB1C0"/>
                                    <code code="3097-3"
                                    codeSystem="2.16.840.1.113883.6.1"
                                    codeSystemName="LOINC" displayName="UREA NITROGEN/CREATININE:MCRTO:PT:SER/PLAS:QN:">
                                    <originalText>BUN/Creat Ratio</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7480749"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170208071800.000-0800"/>
                                    <value value="9" xsi:type="REAL"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170208072523.000-0800"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Kyle</given>
                                    <given>Cerner</given>
                                    <family>Harrison</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>7-25</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <organizer classCode="BATTERY" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.1"/>
                            <id root="A3001DF2-7E8B-4920-84BE-ABF96D0A0BE0"/>
                            <code nullFlavor="UNK" xsi:type="CD">
                                <originalText>Hematology</originalText>
                            </code>
                            <statusCode code="completed"/>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="06B44BF5-D92E-456F-AC00-72299EC24C7F"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Hemoglobin</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7409853"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170128064200.000-0800"/>
                                    <value unit="g/dL" value="14.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170128084612.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Tina</given>
                                    <given>Test</given>
                                    <family>Morgan</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>13.7-17.5 g/dL</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                            <component>
                                <observation classCode="OBS" moodCode="EVN">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.2"/>
                                    <id root="EF5C25AF-609F-4F8E-9B90-A63323B63E4E"/>
                                    <code nullFlavor="UNK">
                                    <originalText>Hematocrit</originalText>
                                    </code>
                                    <text>
                                    <reference value="#RESEVN7409855"/>
                                    </text>
                                    <statusCode code="completed"/>
                                    <effectiveTime value="20170128064200.000-0800"/>
                                    <value unit="%" value="41.0" xsi:type="PQ"/>
                                    <interpretationCode code="N"
                                    codeSystem="2.16.840.1.113883.5.83" codeSystemName="ObservationInterpretation"/>
                                    <author typeCode="AUT">
                                    <time value="20170128084612.000-0600"/>
                                    <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson
                                    classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Tina</given>
                                    <given>Test</given>
                                    <family>Morgan</family>
                                    </name>
                                    </assignedPerson>
                                    </assignedAuthor>
                                    </author>
                                    <referenceRange typeCode="REFV">
                                    <observationRange>
                                    <text>40.1-51.0 %</text>
                                    </observationRange>
                                    </referenceRange>
                                </observation>
                            </component>
                        </organizer>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.2"/>
                    <templateId root="2.16.840.1.113883.10.20.22.2.2.1"/>
                    <code code="11369-6"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="History of immunizations"/>
                    <title>Immunizations</title>
                    <text>
                        <paragraph styleCode="Bold">Given and Recorded</paragraph>
                        <table border="1" width="95%">
                            <colgroup>
                                <col width="50%"/>
                                <col width="20%"/>
                                <col width="15%"/>
                                <col width="15%"/>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>Vaccine</th>
                                    <th>Date</th>
                                    <th>Status</th>
                                    <th>Refusal Reason</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                    <content ID="IMMUN7411534">cholera vaccine</content>
                                    </td>
                                    <td>1/31/17</td>
                                    <td>Given</td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="IMMUN7071748">zoster vaccine live</content>
                                    </td>
                                    <td>1/22/17</td>
                                    <td>Given</td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="IMMUN7071682">influenza, injectable, quadrivalent-pf</content>
                                    </td>
                                    <td>11/29/16</td>
                                    <td>Given</td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="IMMUN7071686">influenza,trivalent, recombinant, inj-pf</content>
                                    </td>
                                    <td>11/28/16</td>
                                    <td>Given</td>
                                    <td> </td>
                                </tr>
                                <tr>
                                    <td>
                                    <content ID="IMMUN7071690">pneumococcal 13-valent conjugate (PCV13)</content>
                                    </td>
                                    <td>12/13/13</td>
                                    <td>Given</td>
                                    <td> </td>
                                </tr>
                            </tbody>
                        </table>
                    </text>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <substanceAdministration classCode="SBADM"
                            moodCode="EVN" negationInd="false">
                            <templateId root="2.16.840.1.113883.10.20.22.4.52"/>
                            <id root="BFD4F474-1494-4FD9-B062-0C73549BC26D"/>
                            <text>
                                <reference value="#IMMUN7071690"/>
                            </text>
                            <statusCode code="completed"/>
                            <effectiveTime value="20131213000000.000-0600"/>
                            <routeCode code="C28161"
                                codeSystem="2.16.840.1.113883.3.26.1.1" codeSystemName="NCI Thesaurus">
                                <originalText>IntraMuscular</originalText>
                            </routeCode>
                            <approachSiteCode nullFlavor="UNK">
                                <originalText>Right Thigh</originalText>
                            </approachSiteCode>
                            <doseQuantity unit="mL" value="0.5"/>
                            <consumable typeCode="CSM">
                                <manufacturedProduct classCode="MANU">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.54"/>
                                    <manufacturedMaterial
                                    classCode="MMAT" determinerCode="KIND">
                                    <code code="133"
                                    codeSystem="2.16.840.1.113883.12.292"
                                    codeSystemName="CVX" displayName="pneumococcal 13-valent conjugate (PCV13)">
                                    <originalText>
                                    <reference value="#IMMUN7071690"/>
                                    </originalText>
                                    </code>
                                    <lotNumberText>H07344</lotNumberText>
                                    </manufacturedMaterial>
                                    <manufacturerOrganization>
                                    <name>Merck &amp; Company Inc</name>
                                    </manufacturerOrganization>
                                </manufacturedProduct>
                            </consumable>
                            <author>
                                <time value="20131213000000.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </substanceAdministration>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <substanceAdministration classCode="SBADM"
                            moodCode="EVN" negationInd="false">
                            <templateId root="2.16.840.1.113883.10.20.22.4.52"/>
                            <id root="3A42C071-24AC-4A2E-B64C-54F69C4E27CC"/>
                            <text>
                                <reference value="#IMMUN7071686"/>
                            </text>
                            <statusCode code="completed"/>
                            <effectiveTime value="20161128000000.000-0600"/>
                            <routeCode nullFlavor="UNK">
                                <originalText>Not Applicable</originalText>
                            </routeCode>
                            <approachSiteCode nullFlavor="UNK">
                                <originalText>Right Thigh</originalText>
                            </approachSiteCode>
                            <consumable typeCode="CSM">
                                <manufacturedProduct classCode="MANU">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.54"/>
                                    <manufacturedMaterial
                                    classCode="MMAT" determinerCode="KIND">
                                    <code code="155"
                                    codeSystem="2.16.840.1.113883.12.292"
                                    codeSystemName="CVX" displayName="influenza,trivalent, recombinant, inj-pf">
                                    <originalText>
                                    <reference value="#IMMUN7071686"/>
                                    </originalText>
                                    </code>
                                    <lotNumberText>123</lotNumberText>
                                    </manufacturedMaterial>
                                    <manufacturerOrganization>
                                    <name>Seqirus</name>
                                    </manufacturerOrganization>
                                </manufacturedProduct>
                            </consumable>
                            <author>
                                <time value="20161128000000.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </substanceAdministration>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <substanceAdministration classCode="SBADM"
                            moodCode="EVN" negationInd="false">
                            <templateId root="2.16.840.1.113883.10.20.22.4.52"/>
                            <id root="4708D5AC-742D-4867-9043-0EB7810C3391"/>
                            <text>
                                <reference value="#IMMUN7071682"/>
                            </text>
                            <statusCode code="completed"/>
                            <effectiveTime value="20161129000000.000-0600"/>
                            <routeCode code="C28161"
                                codeSystem="2.16.840.1.113883.3.26.1.1" codeSystemName="NCI Thesaurus">
                                <originalText>IntraMuscular</originalText>
                            </routeCode>
                            <approachSiteCode nullFlavor="UNK">
                                <originalText>Right Thigh</originalText>
                            </approachSiteCode>
                            <doseQuantity unit="mL" value="0.5"/>
                            <consumable typeCode="CSM">
                                <manufacturedProduct classCode="MANU">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.54"/>
                                    <manufacturedMaterial
                                    classCode="MMAT" determinerCode="KIND">
                                    <code code="150"
                                    codeSystem="2.16.840.1.113883.12.292"
                                    codeSystemName="CVX" displayName="influenza, injectable, quadrivalent-pf">
                                    <originalText>
                                    <reference value="#IMMUN7071682"/>
                                    </originalText>
                                    </code>
                                    <lotNumberText>MN5CS</lotNumberText>
                                    </manufacturedMaterial>
                                    <manufacturerOrganization>
                                    <name>GlaxoSmithKline</name>
                                    </manufacturerOrganization>
                                </manufacturedProduct>
                            </consumable>
                            <author>
                                <time value="20161129000000.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </substanceAdministration>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <substanceAdministration classCode="SBADM"
                            moodCode="EVN" negationInd="false">
                            <templateId root="2.16.840.1.113883.10.20.22.4.52"/>
                            <id root="2AC0DBCA-7643-4633-9F17-01CB0ECBDE53"/>
                            <text>
                                <reference value="#IMMUN7411534"/>
                            </text>
                            <statusCode code="completed"/>
                            <effectiveTime value="20170131172900.000-0800"/>
                            <routeCode code="C28161"
                                codeSystem="2.16.840.1.113883.3.26.1.1" codeSystemName="NCI Thesaurus">
                                <originalText>IntraMuscular</originalText>
                            </routeCode>
                            <approachSiteCode nullFlavor="UNK">
                                <originalText>Left Deltoid</originalText>
                            </approachSiteCode>
                            <doseQuantity unit="mL" value="0.5"/>
                            <consumable typeCode="CSM">
                                <manufacturedProduct classCode="MANU">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.54"/>
                                    <manufacturedMaterial
                                    classCode="MMAT" determinerCode="KIND">
                                    <code nullFlavor="UNK">
                                    <originalText>
                                    <reference value="#IMMUN7411534"/>
                                    </originalText>
                                    </code>
                                    <lotNumberText>0123456</lotNumberText>
                                    </manufacturedMaterial>
                                    <manufacturerOrganization>
                                    <name>Novartis Pharmaceuticals</name>
                                    </manufacturerOrganization>
                                </manufacturedProduct>
                            </consumable>
                            <performer typeCode="PRF">
                                <assignedEntity classCode="ASSIGNED">
                                    <id
                                    assigningAuthorityName="National Provider Identifier"
                                    extension="2450453636" root="2.16.840.1.113883.3.4.6"/>
                                    <addr use="WP">
                                    <streetAddressLine>2800 Rockcreek Parkway</streetAddressLine>
                                    <city>Kansas City</city>
                                    <state>MO</state>
                                    <postalCode>64117-    </postalCode>
                                    <country>US</country>
                                    </addr>
                                    <telecom use="WP" value="tel:(816)111-1111"/>
                                    <assignedPerson classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>KARL</given>
                                    <given>L.</given>
                                    <family>BROWN</family>
                                    </name>
                                    </assignedPerson>
                                </assignedEntity>
                            </performer>
                            <author>
                                <time value="20170131172900.000-0800"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </substanceAdministration>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <substanceAdministration classCode="SBADM"
                            moodCode="EVN" negationInd="false">
                            <templateId root="2.16.840.1.113883.10.20.22.4.52"/>
                            <id root="B810CA44-96D3-4682-AE78-A41897CE113F"/>
                            <text>
                                <reference value="#IMMUN7071748"/>
                            </text>
                            <statusCode code="completed"/>
                            <effectiveTime value="20170122190100.000-0500"/>
                            <routeCode code="C38299"
                                codeSystem="2.16.840.1.113883.3.26.1.1" codeSystemName="NCI Thesaurus">
                                <originalText>SubCutaneous</originalText>
                            </routeCode>
                            <approachSiteCode nullFlavor="UNK">
                                <originalText>Left Deltoid</originalText>
                            </approachSiteCode>
                            <doseQuantity unit="mL" value="0.65"/>
                            <consumable typeCode="CSM">
                                <manufacturedProduct classCode="MANU">
                                    <templateId root="2.16.840.1.113883.10.20.22.4.54"/>
                                    <manufacturedMaterial
                                    classCode="MMAT" determinerCode="KIND">
                                    <code code="121"
                                    codeSystem="2.16.840.1.113883.12.292"
                                    codeSystemName="CVX" displayName="zoster vaccine live">
                                    <originalText>
                                    <reference value="#IMMUN7071748"/>
                                    </originalText>
                                    </code>
                                    <lotNumberText>24567</lotNumberText>
                                    </manufacturedMaterial>
                                    <manufacturerOrganization>
                                    <name>Merck &amp; Company Inc</name>
                                    </manufacturerOrganization>
                                </manufacturedProduct>
                            </consumable>
                            <performer typeCode="PRF">
                                <assignedEntity classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <telecom nullFlavor="NI"/>
                                    <assignedPerson classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>Christen</given>
                                    <given>ASMR</given>
                                    <family>Burkeen</family>
                                    </name>
                                    </assignedPerson>
                                </assignedEntity>
                            </performer>
                            <author>
                                <time value="20170122190100.000-0500"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </substanceAdministration>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.7.1"/>
                    <code code="47519-4"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="History of Procedures"/>
                    <title>Procedures</title>
                    <text>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <colgroup>
                                <col width="45%"/>
                                <col width="10%"/>
                                <col width="25%"/>
                                <col width="20%"/>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>Procedure</th>
                                    <th>Date</th>
                                    <th>Related Diagnosis</th>
                                    <th>Body Site</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr ID="ITEM_PROCEDURE116176125">
                                    <td>
                                    <content ID="PROCEDURE116176125">Online assessment and management service provided by a qualified nonphysician health care professional to an established patient or guardian, not originating from a related assessment and management service provided within the previous 7 days, using the I</content>
                                    </td>
                                    <td>10/29/13</td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                                <tr ID="ITEM_PROCEDURE116176129">
                                    <td>
                                    <content ID="PROCEDURE116176129">Doppler echocardiography color flow velocity mapping (List separately in addition to codes for echocardiography)</content>
                                    </td>
                                    <td>6/2/13</td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                                <tr ID="ITEM_PROCEDURE116176127">
                                    <td>
                                    <content ID="PROCEDURE116176127">Doppler echocardiography, pulsed wave and/or continuous wave with spectral display (List separately in addition to codes for echocardiographic imaging); complete</content>
                                    </td>
                                    <td>6/2/13</td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                                <tr ID="ITEM_PROCEDURE116176133">
                                    <td>
                                    <content ID="PROCEDURE116176133">Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report</content>
                                    </td>
                                    <td>6/2/13</td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                                <tr ID="ITEM_PROCEDURE116176131">
                                    <td>
                                    <content ID="PROCEDURE116176131">Transthoracic echocardiography for congenital cardiac anomalies; complete</content>
                                    </td>
                                    <td>6/2/13</td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                                <tr ID="ITEM_PROCEDURE116176135">
                                    <td>
                                    <content ID="PROCEDURE116176135">Arthrocentesis, aspiration and/or injection, major joint or bursa (eg, shoulder, hip, knee, subacromial bursa); without ultrasound guidance</content>
                                    </td>
                                    <td>3/29/13</td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                                <tr ID="ITEM_PROCEDURE116176177">
                                    <td>
                                    <content ID="PROCEDURE116176177">Tonsillectomy and adenoidectomy; younger than age 12</content>
                                    </td>
                                    <td>6/20/68</td>
                                    <td> </td>
                                    <td> </td>
                                </tr>
                            </tbody>
                        </table>
                    </text>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <procedure classCode="PROC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.14"/>
                            <id root="2393E112-3B47-4F4F-AB3B-070DE0E7AADB"/>
                            <code code="20610"
                                codeSystem="2.16.840.1.113883.6.12"
                                codeSystemName="cpt-4" displayName="Arthrocentesis, aspiration and/or injection; major joint or bursa (eg, shoulder, hip, knee joint, subacromial bursa)">
                                <originalText>
                                    <reference value="#PROCEDURE116176135"/>
                                </originalText>
                            </code>
                            <statusCode code="completed"/>
                            <effectiveTime value=""/>
                            <author>
                                <time value="20170122141335.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </procedure>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <procedure classCode="PROC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.14"/>
                            <id root="0D76A66B-767C-4466-AE2F-CC211383252A"/>
                            <code code="93325"
                                codeSystem="2.16.840.1.113883.6.12"
                                codeSystemName="cpt-4" displayName="Doppler echocardiography color flow velocity mapping (List separately in addition to codes for echocardiography)">
                                <originalText>
                                    <reference value="#PROCEDURE116176129"/>
                                </originalText>
                            </code>
                            <statusCode code="completed"/>
                            <effectiveTime value="20130602000000.000-0500"/>
                            <author>
                                <time value="20170122141335.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </procedure>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <procedure classCode="PROC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.14"/>
                            <id root="0253797B-01BE-4316-A9CB-342F62D21A01"/>
                            <code code="93320"
                                codeSystem="2.16.840.1.113883.6.12"
                                codeSystemName="cpt-4" displayName="Doppler echocardiography, pulsed wave and/or continuous wave with spectral display (List separately in addition to codes for echocardiographic imaging); complete">
                                <originalText>
                                    <reference value="#PROCEDURE116176127"/>
                                </originalText>
                            </code>
                            <statusCode code="completed"/>
                            <effectiveTime value="20130602000000.000-0500"/>
                            <author>
                                <time value="20170122141335.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </procedure>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <procedure classCode="PROC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.14"/>
                            <id root="DF655E01-3D74-4BC4-ADD7-75427D1A47AB"/>
                            <code code="93000"
                                codeSystem="2.16.840.1.113883.6.12"
                                codeSystemName="cpt-4" displayName="Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report">
                                <originalText>
                                    <reference value="#PROCEDURE116176133"/>
                                </originalText>
                            </code>
                            <statusCode code="completed"/>
                            <effectiveTime value="20130602000000.000-0500"/>
                            <author>
                                <time value="20170122141335.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </procedure>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <procedure classCode="PROC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.14"/>
                            <id root="0DBAB04E-C941-4715-AD85-3E1E6ED9B429"/>
                            <code code="98969"
                                codeSystem="2.16.840.1.113883.6.12"
                                codeSystemName="cpt-4" displayName="NONPHYSICIAN ONLINE ASSESSMENT AND MANAGEMENT">
                                <originalText>
                                    <reference value="#PROCEDURE116176125"/>
                                </originalText>
                            </code>
                            <statusCode code="completed"/>
                            <effectiveTime value="20131029000000.000-0500"/>
                            <author>
                                <time value="20170122141335.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </procedure>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <procedure classCode="PROC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.14"/>
                            <id root="70EBB82D-D1EB-4026-94AE-BAE999631661"/>
                            <code code="42820"
                                codeSystem="2.16.840.1.113883.6.12"
                                codeSystemName="cpt-4" displayName="Tonsillectomy and adenoidectomy; under age 12">
                                <originalText>
                                    <reference value="#PROCEDURE116176177"/>
                                </originalText>
                            </code>
                            <statusCode code="completed"/>
                            <effectiveTime value="19680620000000.000-0500"/>
                            <author>
                                <time value="20170122163832.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </procedure>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <procedure classCode="PROC" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.14"/>
                            <id root="49B47924-AF76-4834-9F58-13C475487F00"/>
                            <code code="93303"
                                codeSystem="2.16.840.1.113883.6.12"
                                codeSystemName="cpt-4" displayName="Transthoracic echocardiography for congenital cardiac anomalies; complete">
                                <originalText>
                                    <reference value="#PROCEDURE116176131"/>
                                </originalText>
                            </code>
                            <statusCode code="completed"/>
                            <effectiveTime value="20130602000000.000-0500"/>
                            <author>
                                <time value="20170122141335.000-0600"/>
                                <assignedAuthor classCode="ASSIGNED">
                                    <id nullFlavor="NI"/>
                                    <addr nullFlavor="UNK"/>
                                    <assignedPerson>
                                    <name>
                                    <given nullFlavor="NA"/>
                                    <family nullFlavor="NA"/>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </procedure>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.17"/>
                    <code code="29762-2"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="Social History"/>
                    <title>Social History</title>
                    <text>
                        <table border="1" width="95%">
                            <colgroup>
                                <col width="25%"/>
                                <col width="75%"/>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>Social History Type</th>
                                    <th>Response</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                    <content ID="SHXT93">Tobacco</content>
                                    </td>
                                    <td>
                                    <content ID="SHXR93">Smoking tobacco use: 10 or more cigs(1/2 pack or more)/day in last 30 days.  Type: Cigarettes.  Smokeless tobacco use: Never.  Exposure to Secondhand Smoke: Yes.  Previous treatment: None.  Ready to change: No.  No  14. Patient successfully completed smoking cessation education within last year:.  No Smoking/Tobacco Cessation Teaching completed.  Patient refused instruction  Reasons Smoking/Tobacco Cessation Teaching not yet completed:.</content>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </text>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <observation classCode="OBS" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.38"/>
                            <id root="5FC6A978-B199-46B9-B8A6-D36C883D4AB1"/>
                            <code nullFlavor="UNK" xsi:type="CD">
                                <originalText>
                                    <reference value="#SHXT93"/>
                                </originalText>
                            </code>
                            <statusCode code="completed"/>
                            <effectiveTime>
                                <low nullFlavor="UNK"/>
                            </effectiveTime>
                            <value xsi:type="ED">
                                <reference value="#SHXR93"/>
                            </value>
                            <author>
                                <time value="20170411170238.000-0500"/>
                                <assignedAuthor>
                                    <id
                                    assigningAuthorityName="National Provider Identifier"
                                    extension="1467668400" root="2.16.840.1.113883.3.4.6"/>
                                    <addr use="WP">
                                    <streetAddressLine>701 Hospital Loop</streetAddressLine>
                                    <city>FAIRCHILD AIR FORCE BASE</city>
                                    <state>WA</state>
                                    <postalCode>99011-    </postalCode>
                                    </addr>
                                    <telecom use="WP" value="tel:(247)273-1"/>
                                    <assignedPerson classCode="PSN" determinerCode="INSTANCE">
                                    <name>
                                    <given>SETH</given>
                                    <given>P</given>
                                    <family>WILSON</family>
                                    </name>
                                    </assignedPerson>
                                </assignedAuthor>
                            </author>
                        </observation>
                    </entry>
                    <entry contextConductionInd="true" typeCode="DRIV">
                        <observation classCode="OBS" moodCode="EVN">
                            <templateId root="2.16.840.1.113883.10.20.22.4.78"/>
                            <id root="3CDD32B7-B0B4-4A11-BD34-DD8BDE6F637B"/>
                            <code code="ASSERTION"
                                codeSystem="2.16.840.1.113883.5.4" codeSystemName="HL7 ActCode"/>
                            <statusCode code="completed"/>
                            <effectiveTime>
                                <low nullFlavor="UNK"/>
                            </effectiveTime>
                            <value nullFlavor="NI" xsi:type="ST"/>
                        </observation>
                    </entry>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.14"/>
                    <code code="47420-5"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="Functional Status"/>
                    <title>Functional Status</title>
                    <text>
                        <paragraph>
                            <content styleCode="Bold">FUNCTIONAL</content>
                        </paragraph>
                        <paragraph>4/11/17</paragraph>
                        <br/>
                        <table border="0" width="95%">
                            <colgroup>
                                <col width="25%"/>
                                <col width="75%"/>
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td>Home Dietary Supplements Captured</td>
                                    <td>Unable to obtain</td>
                                </tr>
                            </tbody>
                        </table>
                        <paragraph>1/31/17</paragraph>
                        <br/>
                        <table border="0" width="95%">
                            <colgroup>
                                <col width="25%"/>
                                <col width="75%"/>
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td>ADLs</td>
                                    <td>Minimal assistance</td>
                                </tr>
                            </tbody>
                        </table>
                        <paragraph>1/22/17</paragraph>
                        <br/>
                        <table border="0" width="95%">
                            <colgroup>
                                <col width="25%"/>
                                <col width="75%"/>
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td>Activity Status ADL</td>
                                    <td>Ambulating in hall,<br/>Ambulating in room,<br/>Bathroom privileges</td>
                                </tr>
                            </tbody>
                        </table>
                    </text>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.9"/>
                    <code code="51847-2"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="Assessment and Plan"/>
                    <title>Assessment and Plan</title>
                    <text>
                        <content>Extracted from:</content>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <colgroup>
                                <col width="35%"/>
                                <col width="35%"/>
                                <col width="30%"/>
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td align="left">
                                    <content styleCode="Bold">Title: </content>BH Note- Not in Pt Portal- TEST</td>
                                    <td align="left">
                                    <content styleCode="Bold">Author: </content>Bonner (Cerner), Anna</td>
                                    <td align="left">
                                    <content styleCode="Bold">Date: </content>4/4/17</td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <tbody>
                                <tr>
                                    <td>      Assessment/Plan <br/>      TEST        <br/>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <br/>
                        <content>Extracted from:</content>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <colgroup>
                                <col width="35%"/>
                                <col width="35%"/>
                                <col width="30%"/>
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td align="left">
                                    <content styleCode="Bold">Title: </content>Note in Paient Portal #2</td>
                                    <td align="left">
                                    <content styleCode="Bold">Author: </content>Burkeen (LPDH), Christen</td>
                                    <td align="left">
                                    <content styleCode="Bold">Date: </content>3/27/17</td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <tbody>
                                <tr>
                                    <td>      Assessment/Plan <br/>
                                    <br/>   Not in Patient Portal #2     <br/>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <br/>
                        <content>Extracted from:</content>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <colgroup>
                                <col width="35%"/>
                                <col width="35%"/>
                                <col width="30%"/>
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td align="left">
                                    <content styleCode="Bold">Title: </content>Not in Patient Portal - Behavioral Health Note</td>
                                    <td align="left">
                                    <content styleCode="Bold">Author: </content>Burkeen (LPDH), Christen</td>
                                    <td align="left">
                                    <content styleCode="Bold">Date: </content>3/27/17</td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <tbody>
                                <tr>
                                    <td>      Assessment/Plan <br/>
                                    <br/>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <br/>
                        <content>Extracted from:</content>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <colgroup>
                                <col width="35%"/>
                                <col width="35%"/>
                                <col width="30%"/>
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td align="left">
                                    <content styleCode="Bold">Title: </content>Office Clinic Note</td>
                                    <td align="left">
                                    <content styleCode="Bold">Author: </content>Dascanio, Sunny Cerner</td>
                                    <td align="left">
                                    <content styleCode="Bold">Date: </content>2/7/17</td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="1" width="95%">
                            <tbody>
                                <tr>
                                    <td>      Assessment/Plan     <br/>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <paragraph>
                            <content styleCode="Bold Underline">Future Appointments </content>
                        </paragraph>
                        <paragraph>
                            <content styleCode="Bold">Appointment Date: </content>06/30/2017 10:00:00 am<br/>
                            <content styleCode="Bold">Scheduled Provider: </content>ACAR, TANSEL<br/>
                            <content styleCode="Bold">Location: </content>FCCL Dental<br/>
                            <content styleCode="Bold">Appointment Type: </content>Dental Visit<br/>
                        </paragraph>
                        <br/>
                        <paragraph>
                            <content styleCode="Bold Underline">Diagnostic Tests Pending</content>
                        </paragraph>
                        <list>
                            <item>Culture,Blood 1/22/17 7:03 PM</item>
                            <item>Hemagram 1/22/17 6:05 PM</item>
                        </list>
                        <br/>
                        <br/>
                    </text>
                </section>
            </component>
            <component contextConductionInd="true" typeCode="COMP">
                <section classCode="DOCSECT" moodCode="EVN">
                    <templateId root="2.16.840.1.113883.10.20.22.2.41"/>
                    <code code="8653-8"
                        codeSystem="2.16.840.1.113883.6.1"
                        codeSystemName="LOINC" displayName="Hospital Discharge Instructions"/>
                    <title>Hospital Discharge Instructions</title>
                    <text>
                        <content ID="SCRIPT.XR_CUST_DISCH_INFO_TITLE"/>
                        <content ID="SCRIPT.XR_CUST_FOLLOWUP_TXT"/>
                        <paragraph>No data available for this section</paragraph>
                    </text>
                </section>
            </component>
        </structuredBody>
    </component>
</ClinicalDocument>
"""
