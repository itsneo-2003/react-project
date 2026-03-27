🔹 1. Use Case Name

Review and Submit RFO Decision by Country Coverage (Endorse / Refer Back)

⸻

🔹 2. Description

Risk Framework Owners (RFOs) assigned for different country coverages should be able to independently review the Conflict of Interest (COI) risk assessment submitted by the PM and provide their decision.

The system should ensure:
	•	Users can navigate through the assessment stages in read-only mode
	•	Users can view responses provided by PM
	•	Users can enter comments
	•	Users can take action via:
	•	Endorse
	•	Refer Back (with mandatory comment)

Stage visibility control:
	•	Stage 3a → visible only to RFOs (for review and comments)
	•	Stage 3b → visible only to PM/1LOD
	•	UI should display both as a single stage labeled “Stage 3” for all users

Decision behavior:
	•	Each RFO (per country coverage) must independently review and submit their decision
	•	System must not auto-trigger decisions based on other RFO actions

Status logic:
	•	Default → Pending Endorsement
	•	If all RFOs endorse → status updates to Endorsed by RFO
	•	If any RFO refers back → status updates to Referred Back

Action behavior:
	•	On clicking Endorse, a confirmation popup should appear (Submit / Cancel)
	•	On clicking Refer Back, mandatory comment validation must be enforced

Additional rules:
	•	If endorsement includes conditions → RFO must refer back instead of endorsing
	•	All actions must be captured in audit logs

⸻

🔹 3. Target Output
	•	RFO (country-specific) is able to:
	•	Navigate assessment stages in read-only mode
	•	View PM responses
	•	Provide comments
	•	Submit decision (Endorse / Refer Back)
	•	System ensures:
	•	Stage-based visibility (3a vs 3b)
	•	Independent decision submission by each RFO
	•	Confirmation popup for endorse
	•	Mandatory comment validation for refer back
	•	Workflow outcome:
	•	If all RFOs endorse → moves to next stage / PM queue
	•	If any RFO refers back → routed back to PM with comments
	•	Audit:
	•	All actions (endorse, refer back, comments) are logged with user and timestamp
