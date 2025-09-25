class Prompts:
    def __init__(self):
        """Prevents instantiation of this constants class."""
        raise NotImplementedError("This class is not meant to be instantiated.")
    
    DODI: str = """
Your Goal: Analyze a patient's clinical note against specific U.S. Department of Defense medical standards (DODI 6130.03, Volume 1, Section 5) to determine if the patient has medical conditions that would disqualify or potentially disqualify them from military service.
Source Documents:
1.	The Clinical Note provided below.
2.	DoD Instruction 6130.03, Volume 1: You must use the standards found only in Section 5: DISQUALIFYING CONDITIONS. (Assume you have access to this document).
Instructions (Follow these steps precisely):
Step 1: Read the Clinical Note Carefully.
•	Understand the patient's current health issues, past medical history, and any diagnoses mentioned.
Step 2: Identify Relevant Medical Information.
•	Look for any specific medical diagnoses (like "diabetes mellitus" or "ulcerative colitis").
•	Look for any history of significant medical events (like "psychotic episode" or "surgery").
•	Look for any symptoms or findings mentioned that might relate to a disqualifying condition.
Step 3: Compare with DODI Section 5 Standards.
•	For each piece of relevant medical information identified in Step 2, check if it matches any of the disqualifying conditions listed in Section 5 of DODI 6130.03, Volume 1.
Step 4: Determine the Correct Flag Type (DISQUALIFYING or POTENTIALLY DISQUALIFYING).
•	DISQUALIFYING: Assign the flag [FLAG - DISQUALIFYING] if the clinical note confirms that the patient currently has or has a history of a condition that is listed as disqualifying in DODI Section 5.
o	Example: If the note says "Patient has history of asthma after age 13" and DODI Section 5.10.e says "History of airway hyper responsiveness including asthma...after the 13th birthday," this is DISQUALIFYING. It's a confirmed history matching the standard.
•	POTENTIALLY DISQUALIFYING: Assign the flag [FLAG - POTENTIALLY DISQUALIFYING] ONLY IF the clinical note explicitly states there is uncertainty about a diagnosis (using words like "possible," "suspected," "rule out," "differential diagnosis includes") AND that specific condition, if it were confirmed, is listed as disqualifying in DODI Section 5.
o	Example: If the note says "Impression: Possible sleep apnea, requires sleep study for confirmation" and DODI Section 5.27.b lists "sleep-related breathing disorders, including but not limited to sleep apnea" as disqualifying, this is POTENTIALLY DISQUALIFYING. The diagnosis is uncertain in the note, but would be disqualifying if confirmed.
o	IMPORTANT: Do not use this flag for conditions that are confirmed in the note, even if they happened in the past or are currently managed. If a confirmed condition matches a DODI standard, it is DISQUALIFYING, not potentially disqualifying.
•	NO FLAG: If a condition mentioned in the note is not listed in DODI Section 5, or if it clearly meets an exception described within a standard in Section 5, do not create a flag for it.
Step 5: Determine the Overall Eligibility Status.
•	Look at all the flags you created in Step 4.
•	If there is at least one [FLAG - DISQUALIFYING] flag, the overall status for the patient is DISQUALIFIED.
•	If there are only [FLAG - POTENTIALLY DISQUALIFYING] flags (and zero DISQUALIFYING flags), the overall status is POTENTIALLY DISQUALIFIED.
•	If there are no flags created at all, the overall status is QUALIFIED.
•	Write this overall status at the very beginning of your response, after a placeholder name like "Doe, Jane".
Step 6: Format Your Response Using Markdown EXACTLY Like the Example Below.
•	Start with the placeholder name and the overall eligibility status (bolded).
•	Use the heading "Military Eligibility Medical Flags:".
•	For each flag you created in Step 4, use the following Markdown structure:
o	Start with the flag type (e.g., [FLAG - DISQUALIFYING] or [FLAG - QUALIFY]) on its own line.
o	Condition: [Name of the Condition]
o	Clinical Encounter Text: "[Exact quote from the clinical note related to that condition]"
o	DODI 6130.03, Vol 1 - Section [Section Number, e.g., 5.XX.y.(z)] Text: "[Exact quote of the disqualifying standard from the DODI document]"
o	Add a blank line between each complete flag entry.
"""