[2/13, 4:34 PM] Jp SCB: Use Case Name: Automated Email Notifications for Country Coverage Review

Description:
This use case ensures that Country Coverage representatives, Project Managers (PM), and Risk Framework Owners (RFO) receive automated email notifications at key stages of the COI risk assessment workflow. Notifications are triggered when a draft is submitted for review, when an assessment is endorsed or referred back, and when the assessment is fully endorsed and completed. The system also sends reminder and overdue emails to prevent delays and support timely governance actions.

Target Output:
Automated and timely email notifications are successfully delivered to the appropriate stakeholders based on workflow events, enabling prompt review, endorsement, or feedback and ensuring smooth progression of the risk assessment process without bottlenecks.
[2/13, 4:40 PM] Jp SCB: ✅ Conduct Risk Flow (Replace your COI copy with this)

1. Landing Page – Conduct Risk
→ User views all cases (In progress, Pending endorsement, Refer back, Completed)

⬇️

2. Initiate Conduct Risk Assessment (Project Manager / Risk Maker)
→ Enter scope, country, business function
→ Provide initiative / programme details
→ Add description of change

⬇️

3. Conduct Risk Questionnaire
→ User answers structured risk questions
→ System captures inherent risk indicators

⬇️

4. Perform Conduct Risk Assessment
→ Risk level determined based on responses
→ Key conduct risks identified

⬇️

5. Create Mitigation Plan
→ Add actions
→ Assign owners
→ Set target dates

⬇️

6. Submit for RFO / Coverage Review

Decision Node:

👉 Endorsed?

YES ↓

7. Final Endorsed Conduct Risk Assessment
→ Confirmation checks completed
→ Case marked completed

⸻

NO ↓

Refer Back to Project Manager
→ Reviewer provides feedback
→ PM updates assessment / mitigation
→ Resubmit for endorsement

(loop continues until endorsed)
