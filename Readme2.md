🔹 1. Use Case Name

Review and Submit RFO Decision (Endorse / Refer Back)

⸻

🔹 2. Description

RFO users should be able to navigate through the assessment stages in read-only mode, review the responses provided by the PM, and submit their decision by either endorsing or referring back the assessment with mandatory comments.

The system should ensure:
	•	Stage visibility control:
	•	Stage 3a → only for RFOs
	•	Stage 3b → only for PM/1LOD
	•	UI shows as “Stage 3” for all users
	•	Users can view but not edit PM responses
	•	Users can enter comments
	•	Users can take action via:
	•	Endorse
	•	Refer Back (with mandatory comment)

System should also enforce:
	•	Independent decision making by each RFO
	•	No auto-decision based on other RFO actions
	•	Status logic:
	•	Remains Pending Endorsement until all RFOs act
	•	If all endorse → Endorsed by RFO
	•	If any refer back → Referred Back

All actions must be recorded in audit logs.

⸻

🔹 3. Target Output
	•	RFO is able to:
	•	Navigate all relevant stages (read-only)
	•	View assessment responses
	•	Provide comments
	•	Submit decision (Endorse / Refer Back)
	•	System updates:
	•	Displays confirmation popup on endorse
	•	Validates mandatory comments for refer back
	•	Updates assessment status based on RFO decisions
	•	Routes case:
	•	To PM (if referred back)
	•	To next stage (if endorsed by all)
	•	Audit:
	•	All actions (endorse, refer back, comments) are logged with user and timestamp
✅ USE CASE DETAILS

🔹 1. Use Case Name

RFO Review and Decision Submission (Endorse / Refer Back)

⸻

🔹 2. Description

The Risk Framework Owner (RFO) reviews the Conflict of Interest (COI) risk assessment submitted by the PM in a read-only mode and provides a decision by either endorsing or referring back the assessment with mandatory comments.

The system ensures:
	•	RFO can navigate through all assessment stages without editing
	•	RFO can view responses submitted by PM
	•	RFO can enter comments (mandatory for refer back)
	•	Two actions are available:
	•	Endorse
	•	Refer Back

System behavior:
	•	On clicking Endorse, a confirmation popup appears with options:
	•	Submit
	•	Cancel
	•	On clicking Refer Back, user must provide mandatory comments before submission
	•	Each RFO must independently review and submit decision
	•	System must not auto-endorse or auto-refer based on other RFO actions

Status logic:
	•	Default → Pending Endorsement
	•	If all RFOs endorse → Endorsed by RFO
	•	If any RFO refers back → Referred Back

Additional rules:
	•	Comment limit: 5000 characters
	•	All actions (comments, endorse, refer back) are captured in audit log
	•	If endorsement has conditions → RFO should refer back instead of endorsing

⸻

🔹 3. Target Output
	•	RFO is able to:
	•	Navigate assessment stages in read-only mode
	•	View PM responses
	•	Provide comments
	•	Submit decision (Endorse / Refer Back)
	•	System ensures:
	•	Confirmation popup for endorse action
	•	Mandatory comment validation for refer back
	•	Independent decision handling per RFO
	•	Correct status update:
	•	Pending Endorsement
	•	Endorsed by RFO
	•	Referred Back
	•	Workflow outcome:
	•	If endorsed → moves to PM queue for final completion
	•	If referred back → routed back to PM with comments
	•	Audit:
	•	All user actions are logged with timestamp and user details
