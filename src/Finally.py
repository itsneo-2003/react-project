# Get transaction list items
$TransactionResponse = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items?expand=fields"

# Get baseline list items
$BaselineResponse = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$MasterListId/items?expand=fields"

# Find BP-001 in transaction list
$DeletionThresholdItem = $TransactionResponse.value | Where-Object {
    $_.fields.field_2 -eq "BP-001"
}

# Find BP-001 in baseline list
$BaselineItem = $BaselineResponse.value | Where-Object {
    $_.fields.field_2 -eq "BP-001"
}

# Debugging
Write-Host ""
Write-Host "Transaction Item ID: $($DeletionThresholdItem.id)"
Write-Host "Baseline Ref#: $($BaselineItem.fields.field_2)"
Write-Host "Baseline Value: $($BaselineItem.fields.field_5)"

# Current deletion threshold
$CurrentDeletionThreshold = [int]$Data.value.configuration.accidentalDeletionPrevention.alertThreshold

# Baseline threshold
$BaselineDeletionThreshold = [int]$BaselineItem.fields.field_5

# Compare
if ($CurrentDeletionThreshold -eq $BaselineDeletionThreshold) {
    $ComplianceStatus = "Compliant"
}
else {
    $ComplianceStatus = "Non Compliant"

    Write-Host ""
    Write-Host "Deletion Threshold mismatch found" -ForegroundColor Red
    Write-Host "Current: $CurrentDeletionThreshold"
    Write-Host "Baseline: $BaselineDeletionThreshold"
}

# Update transaction list
$Body = @{
    Status = $ComplianceStatus
    field_5 = "$CurrentDeletionThreshold"
} | ConvertTo-Json

Invoke-MgGraphRequest `
-Method PATCH `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($DeletionThresholdItem.id)/fields" `
-Body $Body `
-ContentType "application/json"

Write-Host ""
Write-Host "BP-001 Updated Successfully" -ForegroundColor Cyan
Write-Host "Status: $ComplianceStatus"
Write-Host "Deletion Threshold: $CurrentDeletionThreshold"




