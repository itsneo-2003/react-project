Test Scenario

Verify Conduct Areas are displayed

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click Conduct Risk Assessment plugin.
4. Click on Initiate Risk Assessment.
5. Select Project ID and impacted business functions with RFO.
6. Click Submit.

Expected Result

1. User will see all 10 Conduct Risk Areas displayed.
2. Each Conduct Risk Area contains Applicability and Conduct Risk options.

⸻

Test Scenario

Verify Applicability field is answerable

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click on Initiate Risk Assessment.
4. Select Project ID and impacted business functions with RFO.
5. Click Submit.
6. Select Yes and No for Applicability across different Conduct Risk Areas.

Expected Result

1. User is able to select either Yes or No for Applicability.
2. Selected value is retained.

⸻

Test Scenario

Verify Conduct Risk field is answerable

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click on Initiate Risk Assessment.
4. Select Project ID and impacted business functions with RFO.
5. Click Submit.
6. Select Applicability = Yes.
7. Select Yes and No for Conduct Risk.

Expected Result

1. User is able to select either Yes or No for Conduct Risk.
2. Selected value is retained.

⸻

Test Scenario

Verify Conduct Risk Description visibility

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click on Initiate Risk Assessment.
4. Select Project ID and impacted business functions with RFO.
5. Click Submit.
6. Select Applicability = Yes.
7. Select Conduct Risk = Yes.

Expected Result

1. Conduct Risk Description field is displayed.
2. User is able to enter Conduct Risk Description.

⸻

Test Scenario

Verify Conduct Risk Description mandatory validation

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click on Initiate Risk Assessment.
4. Select Project ID and impacted business functions with RFO.
5. Click Submit.
6. Select Applicability = Yes.
7. Select Conduct Risk = Yes.
8. Leave Conduct Risk Description blank.
9. Click Next.

Expected Result

1. Validation message is displayed.
2. User cannot proceed without entering Conduct Risk Description.

⸻

Test Scenario

Verify Conduct Risk Description character limit

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click on Initiate Risk Assessment.
4. Select Project ID and impacted business functions with RFO.
5. Click Submit.
6. Select Applicability = Yes.
7. Select Conduct Risk = Yes.
8. Enter maximum allowed characters in Conduct Risk Description.

Expected Result

1. User is able to enter description within allowed limit.
2. System prevents entry beyond configured limit.

⸻

Test Scenario

Verify Applicability = No behavior

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click on Initiate Risk Assessment.
4. Select Project ID and impacted business functions with RFO.
5. Click Submit.
6. Select Applicability = No.

Expected Result

1. Conduct Risk Description field is not displayed.
2. Conduct Risk Area is excluded from downstream stages.
3. No record is created in Part 2 for that Conduct Risk Area.
4. No record is created in Mitigation Plan for that Conduct Risk Area.

⸻

Test Scenario

Verify Conduct Risk = No behavior

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click on Initiate Risk Assessment.
4. Select Project ID and impacted business functions with RFO.
5. Click Submit.
6. Select Applicability = Yes.
7. Select Conduct Risk = No.

Expected Result

1. Conduct Risk Description field is not displayed.
2. Conduct Risk Area is excluded from downstream stages.
3. No record is created in Part 2 for that Conduct Risk Area.
4. No record is created in Mitigation Plan for that Conduct Risk Area.

⸻

Test Scenario

Verify Conduct Risk = Yes behavior

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Click on Initiate Risk Assessment.
4. Select Project ID and impacted business functions with RFO.
5. Click Submit.
6. Select Applicability = Yes.
7. Select Conduct Risk = Yes.
8. Enter Conduct Risk Description.

Expected Result

1. Conduct Risk Description field is displayed.
2. User is able to provide Conduct Risk Description.
3. Conduct Risk Area is eligible for downstream processing.

⸻

Test Scenario

Verify only valid Conduct Risks proceed to downstream stages

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Complete multiple Conduct Risk Areas using different combinations.
4. Select:
    * Applicability = No
    * Applicability = Yes and Conduct Risk = No
    * Applicability = Yes and Conduct Risk = Yes
5. Enter Conduct Risk Description for applicable areas.
6. Click Next.

Expected Result

1. Only Conduct Risk Areas with Applicability = Yes and Conduct Risk = Yes are displayed in Part 2.
2. Remaining Conduct Risk Areas are excluded from downstream stages.

⸻

Test Scenario

Verify Save as Draft functionality

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Enter responses for one or more Conduct Risk Areas.
4. Click Save as Draft.

Expected Result

1. Assessment is saved successfully.
2. Status remains In Progress.
3. Saved responses are retained when reopened.

⸻

Test Scenario

Verify Next button navigation

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Complete all mandatory fields.
4. Click Next.

Expected Result

1. User is navigated to Risk Assessment Part 2.

⸻

Test Scenario

Verify Back button warning message

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Modify responses.
4. Click Back.

Expected Result

1. Warning message is displayed.
2. User can Confirm or Cancel navigation.

⸻

Test Scenario

Verify Clear All button functionality

Test Steps

1. Login to Service Bench application.
2. Navigate to Conduct Risk Assessment plugin.
3. Enter responses for multiple Conduct Risk Areas.
4. Click Clear All.

Expected Result

1. All questionnaire responses are cleared.
2. Auto-populated project details remain unchanged.
3. User can re-enter responses.

⸻

Test Scenario

Verify system allow for 2LOD review

Test Steps

1. Login to Service Bench application.
2. Complete all mandatory Conduct Risk Assessment fields.
3. Click Next.

Expected Result

1. System allows assessment to proceed for downstream review process.
2. No mandatory field validation errors are displayed.

⸻

Test Scenario

Verify export to Word format

Test Steps

1. Login to Service Bench application.
2. Complete Conduct Risk Assessment.
3. Click Export → Word.

Expected Result

1. Assessment is exported successfully.
2. Exported document is readable and complete.

⸻

Test Scenario

Verify export to xlsx format

Test Steps

1. Login to Service Bench application.
2. Complete Conduct Risk Assessment.
3. Click Export → xlsx.

Expected Result

1. Assessment is exported successfully.
2. Exported spreadsheet is readable and complete.
