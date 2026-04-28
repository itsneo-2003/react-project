ID	Fraud Scheme	Threat Event	Issue	Description
1	ATM_Fraud	-	Skimming present in UI but not in Excel	UI shows an extra threat event not present in source Excel
2	ATM_Fraud	-	Duplicate Counterfeit values in Excel	Same threat event exists twice with different naming formats
4	Card_Fraud	Customer_authorised_scam	Training and awareness missing in UI	Control exists in Excel but not displayed in UI
6	Card_Fraud	Social_Engineering	UI truncation issue	Recommended control values are truncated in UI (e.g., "Client awareness and education" shown as "Client awareness and y…")
8	Card_Fraud	Social_Engineering	Training and awareness added extra in UI	Control appears in UI though not expected as per mapping context
10	Staff_Fraud	Unauthorised_Fund_Transfers_or_Payments	Duplicate + truncation issue	"Signature & mandate verification" appears twice in Excel and one instance is truncated in UI
11	Staff_Fraud	Unauthorised_Account_Activity___Account_Amendments	Duplicate + truncation issue	"Signature & mandate verification" duplication in Excel and truncation observed in UI
12	Staff_Fraud	Unauthorised_Account_Activity___Dormant_Unclaimed_Accounts	Duplicate + truncation issue	"Signature & mandate verification" duplication in Excel and truncation observed in UI
13	Credit_Fraud (Retail Banking)	-	Missing fraud scheme in UI	Fraud scheme exists in Excel but not available in UI dropdown (only Business Banking variant present)
14	Credit_Fraud_CIB	Misappropriation_of_Loan_Funds	Duplicate + truncation issue	"Drawdown - Signature Checks" appears twice and is truncated in UI
15	New_Account_Fraud_Liabilities	-	Missing fraud scheme in UI	Fraud scheme present in Excel but not available in UI
16	Payment_Fraud_WRB	-	Missing fraud scheme in UI	Fraud scheme present in Excel but not available in UI
17	Payment_Fraud_CIB	-	Missing fraud scheme in UI	Fraud scheme present in Excel but not available in UI
18	Rogue_Trading	-	Missing fraud scheme in UI	Fraud scheme present in Excel but not available in UI
19	Credit_Fraud (Business_Banking)	Financial_Statement_Fraud	Naming mismatch	Excel has "Financial_Statement_Fraud" but UI shows it as "Deal_Statement_Fraud"
20	Credit_Fraud (Business_Banking)	Syndicate_Fraud	Naming mismatch	Excel has "Syndicate_Fraud" but UI shows it as "Kite_Fraud"
