Use Case Name:

COI Workflow Enhancements – Admin Amendments & MS Review Control

Description:

This use case enables COI Admin to amend RFO assignments, Business/Function details, and trigger notifications with amendments. If RFOs have already endorsed, the system restricts further amendments accordingly. Additionally, an optional MS Review step is introduced before 2LOD review, where an additional reviewer can be selected at the PM (Maker) stage. The assessment status is updated based on the selected workflow path, and reminder/alert functionality is enabled for managed services.

Target Output:

COI Admin can amend permitted fields based on endorsement status, notifications reflect updated assignments, optional MS Review is executed before 2LOD when selected, status transitions correctly reflect the review stage, and reminder/alert mechanisms function as configured



Use Case Name:

COI Admin – Initiate and Amend In-Progress Assessment

Description:

This use case enables the COI Admin to initiate a risk assessment on behalf of the PM and amend RFO and Business/Function details while the assessment is in progress. Amendments trigger notifications to relevant stakeholders. The system restricts amendments if all RFOs have already endorsed. If partial endorsements exist, amendments follow defined validation rules. COI Admin can also switch role to PM to initiate and complete the assessment when required.

Target Output:

COI Admin can successfully initiate and amend eligible in-progress assessments, notifications reflect updated details, amendment restrictions are enforced based on endorsement status, and workflow continuity is maintained without errors.




Use Case Name:

FRA_MS Review Before 2LOD Endorsement

Description:

This use case enables the FRA_MS user to review the risk assessment when the FRA review checklist is selected. The FRA_MS can navigate through all stages of the assessment in read-only mode, view responses provided by the PM, and add review comments. Upon clicking “Review,” the assessment status is updated to “Reviewed by FRA_MS” and routed to the 2LOD queue for endorsement.

Target Output:

FRA_MS completes the review without modifying assessment responses, records necessary comments, and the system updates the status to “Reviewed by FRA_MS” before progressing the assessment to the 2LOD endorsement stage.





Use Case Name:

FRA_Admin Assessment Amendment and Initiation

Description:

This use case enables the FRA_Admin to initiate a risk assessment on behalf of the PM and amend RFO, Business, and Function details in an in-progress assessment. Any amendments trigger updated notifications. If all RFOs are already endorsed, amendments are restricted. In cases of partial endorsement, amendments are controlled as per endorsement status. The FRA_Admin can also switch role to PM to initiate and complete the assessment.

Target Output:

FRA_Admin successfully amends or initiates the assessment where permitted, system enforces endorsement-based restrictions, sends notifications for amendments, and allows role switch to complete the assessment without workflow errors.





Use Case Name:

COI Plugin & Role Access Request via ServiceNow

⸻

Description:

This use case enables users to request access to COI plugins and related roles through a ServiceNow self-service portal. Based on the approved role (Admin, Project Manager/1LOD, Group RFO, Country RFO, Plugin User), the system grants appropriate permissions such as initiating assessments, reviewing, endorsing, exporting reports, configuring templates, and managing users. Access is controlled strictly as per the defined role-permission matrix to ensure proper governance and segregation of duties.

⸻

Target Output:

Approved users receive role-based access to COI functionalities as per the defined permission matrix, allowing them to perform only the actions permitted for their role while maintaining compliance and controlled access within the COI assessment workflow.





Use Case Name:

FRA Plugin Access and Role-Based Permission Management

Description:

This use case enables users to request access to FRA plugins and associated roles through ServiceNow. Upon approval, the system assigns role-based permissions (Admin, Project Manager/1LOD, Group RFO, Country RFO, Plugin User) that control what actions the user can perform within the FRA risk assessment workflow.

Permissions include initiating assessments, saving drafts, submitting for review, reviewing, endorsing, referring back, completing assessments, exporting reports, viewing country/business scope, configuring templates, cloning assessments, and user/role management — based strictly on assigned role and scope.

The system ensures that users can only access and perform activities permitted for their role and assigned Business/Function or Country.

Target Output:
	•	Users can request FRA plugin access via ServiceNow.
	•	Approved users receive predefined role-based permissions.
	•	System enforces strict access control by role and scope.
	•	Users can only perform actions enabled for their assigned role.
	•	Assessment visibility is restricted to authorized country/business scope




Use Case Name:

FRA Plugin & Role Access Request via ServiceNow

⸻

Description:

This use case enables users to request access to FRA plugins and related roles through a ServiceNow self-service portal. Based on the approved role (Admin, Project Manager/1LOD, Group RFO, Country RFO, Plugin User), the system grants appropriate permissions such as initiating assessments, reviewing, endorsing, exporting reports, configuring templates, and managing users. Access is controlled strictly as per the defined role-permission matrix to ensure proper governance and segregation of duties.

⸻

Target Output:

Approved users receive role-based access to FRA functionalities as per the defined permission matrix, allowing them to perform only the actions permitted for their role while maintaining compliance and controlled access within the FRA assessment workflow.






