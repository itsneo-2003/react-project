System shall validate that at least one RFO endorsement is completed per Impacted Business/Function.
• Once one RFO endorses within a Business/Function, remaining RFO(s) under the same Business/Function shall no longer require endorsement.
• System shall update their status to “Not Required”.
• System shall trigger notification to remaining RFO(s) within that Business/Function informing that endorsement has been completed.

1️⃣ User Story: Service Bench – Email Notifications to RFO (Group Level)

Use Case Name:
Automated Email Notifications for RFO Endorsement (Group/Business Function Level)

Description:
This use case ensures that Risk Framework Owners (RFOs) receive automated email notifications during the COI risk assessment workflow. Notifications are triggered when a draft is submitted for RFO review, when the assessment is endorsed or referred back, and when the assessment is fully endorsed and completed.

Additionally, when multiple RFOs are assigned within the same Business/Function, the system validates that at least one RFO endorsement is completed. Once endorsed by one RFO, an alert is triggered to notify the other RFO(s) within the same Business/Function that no further endorsement is required.

Target Output:
Automated email notifications and alerts are successfully delivered to the relevant RFOs based on workflow events. If one RFO within a Business/Function endorses the assessment, the remaining RFO(s) are notified that additional endorsement is no longer required, ensuring efficient workflow progression without redundant actions.

⸻

2️⃣ User Story: Service Bench – Review and Endorse by RFO

Use Case Name:
RFO Review, Refer Back, and Endorse COI Risk Assessment

Description:
This use case enables the Risk Framework Owner (RFO) to review the submitted COI risk assessment, navigate through the completed sections in read-only mode, and provide comments before taking action. The RFO can either endorse the assessment or refer it back to the Project Manager (PM) with mandatory comments.

If multiple RFOs are assigned within the same Business/Function, the system ensures that at least one endorsement is sufficient to progress the workflow.

Target Output:
The RFO is able to review the assessment, provide comments, and take action (Endorse or Refer Back). The assessment status updates accordingly, routes to the appropriate queue, and enforces the rule that only one endorsement per Business/Function is required for workflow progression.
