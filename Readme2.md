[3/11, 12:51 PM] Jp SCB: COI_MS Email Templates

1. COI_MS Review Request

Trigger:
PM submits COI assessment with MS review selected

Recipient:
COI_MS
Subject: Action Required: COI Risk Assessment Pending Review

Dear COI_MS,

A Conflict of Interest (COI) risk assessment has been submitted and requires your review.

Case ID: {{Case_ID}}

Please access the assessment to review the responses and proceed with the review.

Click HERE to access the COI assessment.

Regards  
COI System
2. COI_MS Refer Back Notification

Trigger:
COI_MS clicks Refer Back

Recipient:
Project Manager (Maker)
Subject: COI Risk Assessment Referred Back by COI_MS

Dear User,

The Conflict of Interest (COI) risk assessment has been referred back for updates.

Case ID: {{Case_ID}}

Please review the comments provided and update the assessment before resubmitting it for review.

Click HERE to access the COI assessment.

Regards  
COI System
3. COI_MS Review Completed Notification

Trigger:
COI_MS clicks Review

Recipient:
Assigned RFO(s)
Subject: COI Risk Assessment Pending RFO Review

Dear RFO,

A Conflict of Interest (COI) risk assessment has been reviewed by COI_MS and is now pending your review.

Case ID: {{Case_ID}}

Please access the assessment to review and provide your endorsement or refer it back with comments.

Click HERE to access the COI assessment.

Regards  
COI System
4. FRA_MS Review Request

Trigger:
PM submits FRA assessment with MS review selected

Recipient:
FRA_MS
Subject: Action Required: FRA Risk Assessment Pending Review

Dear FRA_MS,

A Fraud Risk Assessment (FRA) has been submitted and requires your review.

Case ID: {{Case_ID}}

Please access the assessment to review the responses and proceed with the review.

Click HERE to access the FRA assessment.

Regards  
FRA System
5. FRA_MS Refer Back Notification

Trigger:
FRA_MS clicks Refer Back

Recipient:
Project Manager (Maker)
Subject: FRA Risk Assessment Referred Back by FRA_MS

Dear User,

The Fraud Risk Assessment has been referred back for updates.

Case ID: {{Case_ID}}

Please review the comments and update the assessment before resubmitting it.

Click HERE to access the FRA assessment.

Regards  
FRA System
6. FRA_MS Review Completed Notification

Trigger:
FRA_MS clicks Review

Recipient:
Assigned RFO(s)
Subject: FRA Risk Assessment Pending RFO Review

Dear RFO,

A Fraud Risk Assessment has been reviewed by FRA_MS and is now pending your review.

Case ID: {{Case_ID}}

Please review the assessment and provide your endorsement or refer it back with comments.

Click HERE to access the FRA assessment.

Regards  
FRA System
COI_ADMIN Email Templates

7. COI Admin Assessment Amendment Notification

Trigger:
COI Admin edits RFO or Business/Function

Recipient:
Affected RFO(s) and PM
Subject: COI Risk Assessment Updated by Admin

Dear User,

The Conflict of Interest (COI) risk assessment has been updated by COI Admin.

Case ID: {{Case_ID}}

Updated details may include changes to Responsible Function Owner (RFO) or Business/Function assignments.

Please review the assessment if required.

Click HERE to access the COI assessment.

Regards  
COI System
FRA_ADMIN Email Templates

8. FRA Admin Assessment Amendment Notification

Trigger:
FRA Admin edits RFO or Business/Function

Recipient:
Affected RFO(s) and PM
Subject: FRA Risk Assessment Updated by Admin

Dear User,

The Fraud Risk Assessment has been updated by FRA Admin.

Case ID: {{Case_ID}}

Updated details may include changes to Responsible Function Owner (RFO) or Business/Function assignments.

Please review the assessment if required.

Click HERE to access the FRA assessment.

Regards  
FRA System
[3/11, 1:38 PM] Jp SCB: When RFO is changed while a case is already pending endorsement, should the previous endorsement (if already given) remain valid or be reset?
COI ADMIN EMAILS

⸻

1. COI – New RFO Assigned

Trigger
Admin updates the RFO list and a new RFO is added to the COI assessment.

Recipient
New R
d"}
Hello,

You have been assigned as the Responsible Function Owner (RFO) for the following Conflict of Interest (COI) assessment.

| Case ID | Reference Type | Reference |
|--------|---------------|-----------|
| {{caseId}} | {{referenceType}} | {{referenceName}} ({{referenceId}}) |

Please access the COI assessment in the system for further details.

Regards,  
COI Administration Team

Note: This is a system-generated email. Please do not rep
2. COI – Old RFO Removed

Trigger
Admin updates the RFO list and an existing RFO is removed.

Recipient
Removed R
d"}
Hello,

The Responsible Function Owner (RFO) assignment for the following Conflict of Interest (COI) assessment has been updated.

| Case ID | Reference Type | Reference |
|--------|---------------|-----------|
| {{caseId}} | {{referenceType}} | {{referenceName}} ({{referenceId}}) |

You are no longer assigned to this COI assessment.  
No further action is required.

Regards,  
COI Administration Team

Note: This is a system-generated email. Please do not rep
3. COI – PM Notification (RFO Updated)

Trigger
Admin updates the RFO list.

Recipient
Programme Manager / Initiative Ow
d"}
Hello,

The Responsible Function Owner (RFO) assignment for the following Conflict of Interest (COI) assessment has been updated by the COI Administrator.

| Case ID | Reference Type | Reference |
|--------|---------------|-----------|
| {{caseId}} | {{referenceType}} | {{referenceName}} ({{referenceId}}) |

Previous RFO: {{oldRfoName}}  
New RFO: {{newRfoName}}

This notification is for your information.

Regards,  
COI Administration Team

Note: This is a system-generated email. Please do not rep
4. COI – Impacted Business Function Updated

Trigger
Admin updates Impacted Business Function in the assessment.

Recipient
Programme Manager / Initiative Own
d"}
Hello,

The impacted Business Function for the following Conflict of Interest (COI) assessment has been updated by the COI Administrator.

| Case ID | Reference Type | Reference |
|--------|---------------|-----------|
| {{caseId}} | {{referenceType}} | {{referenceName}} ({{referenceId}}) |

Updated Business Function: {{businessFunction}}

This notification is for your information.

Regards,  
COI Administration Team

Note: This is a system-generated email. Please do not rep
1. FRA – New RFO Assigned

Trigger
Admin updates the RFO list and a new RFO is added to the FRA assessment.

Recipient
New RFO
Hello,

You have been assigned as the Responsible Function Owner (RFO) for the following Fraud Risk Assessment (FRA).

| Case ID | Reference Type | Reference |
|--------|---------------|-----------|
| {{caseId}} | {{referenceType}} | {{referenceName}} ({{referenceId}}) |

Please access the FRA assessment in the system for further details.

Regards,  
FRA Administration Team

Note: This is a system-generated email. Please do not reply.
2. FRA – Old RFO Removed

Trigger
Admin updates the RFO list and an existing RFO is removed.

Recipient
Removed RFO
Hello,

The Responsible Function Owner (RFO) assignment for the following Fraud Risk Assessment (FRA) has been updated.

| Case ID | Reference Type | Reference |
|--------|---------------|-----------|
| {{caseId}} | {{referenceType}} | {{referenceName}} ({{referenceId}}) |

You are no longer assigned to this FRA assessment.  
No further action is required.

Regards,  
FRA Administration Team

Note: This is a system-generated email. Please do not reply.
3. FRA – PM Notification (RFO Updated)

Trigger
Admin updates the RFO list.

Recipient
Programme Manager / Initiative Owner
Hello,

The Responsible Function Owner (RFO) assignment for the following Fraud Risk Assessment (FRA) has been updated by the FRA Administrator.

| Case ID | Reference Type | Reference |
|--------|---------------|-----------|
| {{caseId}} | {{referenceType}} | {{referenceName}} ({{referenceId}}) |

Previous RFO: {{oldRfoName}}  
New RFO: {{newRfoName}}

This notification is for your information.

Regards,  
FRA Administration Team

Note: This is a system-generated email. Please do not reply.
4. FRA – Impacted Business Function Updated

Trigger
Admin updates Impacted Business Function in the FRA assessment.

Recipient
Programme Manager / Initiative Owner
Hello,

The impacted Business Function for the following Fraud Risk Assessment (FRA) has been updated by the FRA Administrator.

| Case ID | Reference Type | Reference |
|--------|---------------|-----------|
| {{caseId}} | {{referenceType}} | {{referenceName}} ({{referenceId}}) |

Updated Business Function: {{businessFunction}}

This notification is for your information.

Regards,  
FRA Administration Team

Note: This is a system-generated email. Please do not reply.
