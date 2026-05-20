# Get current deletion threshold
$CurrentDeletionThreshold = $Data.value.configuration.accidentalDeletionPrevention.alertThreshold

# Get transaction list items
$TransactionResponse = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items?expand=fields"

# Find BP-001 in transaction list
$DeletionThresholdItem = $TransactionResponse.value |
Where-Object {
    $_.fields.additionalProperties.field_2 -eq "BP-001"
} |
Select-Object -First 1

# Debug transaction row
Write-Host ""
Write-Host "Transaction Item ID: $($DeletionThresholdItem.id)" `
-ForegroundColor Yellow

# Get baseline list items
$BaselineResponse = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$MasterListId/items?expand=fields"

# Find BP-001 in baseline list
$BaselineItem = $BaselineResponse.value |
Where-Object {
    $_.fields.additionalProperties.field_2 -eq "BP-001"
} |
Select-Object -First 1

# Debug baseline row
Write-Host "Baseline Ref#: $($BaselineItem.fields.additionalProperties.field_2)" `
-ForegroundColor Yellow

Write-Host "Baseline Value: $($BaselineItem.fields.additionalProperties.field_5)" `
-ForegroundColor Yellow

# Get baseline threshold
$BaselineDeletionThreshold = [int]$BaselineItem.fields.additionalProperties.field_5

# Compare
if (
    [int]$CurrentDeletionThreshold -eq
    $BaselineDeletionThreshold
) {

    $ComplianceStatus = "Compliant"

    Write-Host "Deletion Threshold compliant" `
    -ForegroundColor Green
}
else {

    $ComplianceStatus = "Non Compliant"

    Write-Host "Deletion Threshold mismatch found" `
    -ForegroundColor Red

    Write-Host "Current: $CurrentDeletionThreshold"
    Write-Host "Baseline: $BaselineDeletionThreshold"
}

# Update transaction list
$Body = @{
    field_5 = "$CurrentDeletionThreshold"
    Status = $ComplianceStatus
} | ConvertTo-Json

Invoke-MgGraphRequest `
-Method PATCH `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($DeletionThresholdItem.id)/fields" `
-Body $Body `
-ContentType "application/json"

Write-Host ""
Write-Host "BP-001 Updated Successfully" `
-ForegroundColor Cyan

Write-Host "Status: $ComplianceStatus"
Write-Host "Deletion Threshold: $CurrentDeletionThreshold"
