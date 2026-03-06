[3/6, 4:33 PM] Jp SCB: 12362623


Use Case Details

Use Case Name

COI Admin Assessment Amendment and Management

⸻

Description

This functionality allows the COI Admin to manage and amend in-progress COI risk assessments on behalf of Project Managers. The admin can edit specific fields such as RFO and impacted business function before endorsement is completed. The system enforces governance controls where edits are restricted after endorsements, ensures that changes reset endorsement status where required, and tracks all modifications through an audit trail.

⸻

Target Output

The COI Admin can successfully initiate or amend eligible risk assessments while maintaining endorsement-based restrictions. Any modifications trigger proper workflow updates, endorsement status resets where applicable, and all actions are recorded in the audit log to ensure governance and traceability.

⸻

Updated Acceptance Criteria

(Add these after your current ones, not replacing them.)
	•	COI Admin should be able to edit risk assessments through the Edit Risk Assessment action available in the action panel.
	•	The edit screen should follow the same layout as the Initiate Risk Assessment stage, but only the RFO and Impacted Business Function fields should be editable.
	•	The system should allow the COI Admin to rearrange or remove selected RFO or Business Function values before endorsement.
	•	The system should provide a search functionality to locate assessments using Case ID, Initiative ID, or Programme ID.
	•	Completed assessments must not appear in the edit search results.
	•	If the COI Admin modifies RFO or Business Function details after endorsement has occurred, the system should reset the endorsement status to Pending.
	•	When endorsement status is reset, the workflow should move back to the RFO endorsement stage and the Final Confirmation stage should be locked until endorsement is completed again.
	•	The system should allow the COI Admin to clone an existing risk assessment to create a new assessment with similar details.
	•	Any amendment performed by the COI Admin should be captured in the audit log including user, timestamp, and updated fields.
[3/6, 4:38 PM] Jp SCB: 12362698

Use Case Details

Use Case Name

FRA Admin Assessment Amendment and Management

⸻

Description

This functionality allows the Fraud Risk Assessment (FRA) Admin to manage and amend fraud risk assessments on behalf of Project Managers. The admin can initiate assessments and edit specific fields such as RFO, Business, and Function details for assessments that are still in progress. The system enforces endorsement-based governance controls where amendments are restricted once endorsements are completed. Any modification updates the workflow accordingly and ensures traceability through audit logging.

⸻

Target Output

FRA Admin users can initiate or amend eligible fraud risk assessments while maintaining endorsement governance rules. Any amendments trigger workflow updates, reset endorsement stages where necessary, and all administrative actions are recorded in the audit log.

⸻

Updated Acceptance Criteria

(Keep your existing ones and add these lines.)
	•	FRA Admin should be able to edit risk assessments using the Edit Risk Assessment option in the action panel.
	•	The edit screen should follow the same structure as the Initiate Risk Assessment stage, but only RFO, Business, and Function fields should be editable.
	•	FRA Admin should be able to rearrange or remove RFO, Business, or Function entries before endorsement is completed.
	•	The system should provide a search capability allowing FRA Admin to locate assessments using Case ID, Initiative ID, or Programme ID.
	•	Completed fraud risk assessments should not appear in the edit search results.
	•	If FRA Admin modifies RFO, Business, or Function details after endorsement has already occurred, the system should reset the endorsement status to Pending.
	•	When endorsement status resets, the workflow should return to the RFO endorsement stage and the Final Confirmation stage should be locked until endorsement is completed again.
	•	The system should allow FRA Admin to clone an existing fraud risk assessment to create a new assessment with similar details.
	•	Any amendment performed by FRA Admin should be recorded in the audit log including user ID, timestamp, and fields updated
[3/6, 5:22 PM] Jp SCB: 12362609
Use Case Details

Use Case Name

Managed Services Review of COI Risk Assessment

⸻

Description

This functionality enables Managed Services (COI_MS) users to review risk assessments submitted by Project Managers after the initial assessment stages are completed. The Managed Services team performs a validation check of the submitted responses before the assessment proceeds to the Second Line of Defense (2LoD) endorsement stage. The review is performed in read-only mode, allowing Managed Services users to validate responses and provide comments while ensuring that no modifications are made to the submitted assessment data.

⸻

Target Output

The COI risk assessment is reviewed by the Managed Services team and either forwarded to the 2LoD (RFO) endorsement stage or returned to the Project Manager for correction. Once reviewed, the workflow moves forward without allowing Managed Services users to modify assessment responses.

⸻

Acceptance Criteria (Add These)

Keep your existing criteria and add the following lines.
	•	Managed Services users should be able to access the Managed Services Review stage after the Project Manager submits the assessment.
	•	Managed Services users should be able to navigate through all assessment stages completed by the Project Manager in read-only mode.
	•	Managed Services users must not be able to edit any responses in the assessment.
	•	Managed Services users should be able to provide review comments during the Managed Services review stage.
	•	Upon clicking Review, the assessment status should update to “Reviewed by COI_MS” and the workflow should move to the 2LoD (RFO) endorsement queue.
	•	The 2LoD endorsement stage should contain two sub-steps:
	•	4a – RFO Comments
	•	4b – Offline Endorsement
	•	If the RFO refers the assessment back, the workflow should return directly to the Project Manager stage and must not return to the Managed Services review stage.
	•	Managed Services users should not be able to modify any data within the assessment during the review stage.
	•	The system should record the Managed Services review action and comments in the audit log.
[3/6, 5:28 PM] Jp SCB: Use Case Details

Use Case Name

Fraud Managed Services Review of Fraud Risk Assessment

⸻

Description

This functionality enables Fraud Managed Services (FRA_MS) users to review fraud risk assessments submitted by Project Managers before the assessment proceeds to the Second Line of Defense (2LoD) endorsement stage. FRA_MS users validate the completeness and quality of the submitted assessment responses in read-only mode and provide comments where required. The review ensures governance and quality control before the assessment is routed to the RFO for final endorsement.

⸻

Target Output

The fraud risk assessment is reviewed by FRA_MS and either:
	•	routed to the 2LoD (RFO) endorsement queue, or
	•	returned to the Project Manager for correction

The review action is recorded and the workflow proceeds according to governance rules without allowing FRA_MS users to modify assessment responses.

⸻

Updated Acceptance Criteria (Add These)

Keep your existing ones and add these lines.

⸻

	•	FRA_MS users should be able to access the Fraud Managed Services review stage after the Project Manager submits the fraud risk assessment.
	•	FRA_MS users should be able to navigate through all completed stages of the fraud risk assessment in read-only mode.
	•	FRA_MS users must not be able to edit any responses or fields within the assessment.
	•	FRA_MS users should be able to view all assessment responses submitted by the Project Manager.
	•	FRA_MS users should be able to provide review comments during the review stage.
	•	The system should display a “Review” action button for FRA_MS users during the review stage.
	•	When the user clicks Review, the assessment status should update to “Reviewed by FRA_MS” and the assessment should be routed to the 2LoD (RFO) endorsement queue.
	•	The 2LoD endorsement stage should contain the following sub-steps:
	•	4a – RFO Comments
	•	4b – Offline Endorsement
	•	If the RFO refers the assessment back, the workflow should return to the Project Manager stage and must not return to the FRA_MS review stage.
	•	FRA_MS users should not be able to modify any responses during the review stage.
	•	The system should record FRA_MS review actions and comments in the audit log.
