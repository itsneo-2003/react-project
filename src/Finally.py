# Get current deletion threshold value
$CurrentDeletionThreshold = $Data.value.configuration.accidentalDeletionPrevention.alertThreshold

# Get transaction list items
$TransactionItems = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items?expand=fields"

# Find BP-001 row in transaction list
$DeletionThresholdItem = $TransactionItems.value |
Where-Object {
    $_.fields.AdditionalProperties.field_2 -eq "BP-001"
} |
Select-Object -First 1

# Get baseline list items
$BaselineItems = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$MasterListId/items?expand=fields"

# Find BP-001 row in baseline list
$BaselineItem = $BaselineItems.value |
Where-Object {
    $_.fields.AdditionalProperties.field_2 -eq "BP-001"
} |
Select-Object -First 1

# Get baseline threshold
$BaselineDeletionThreshold = [int]$BaselineItem.fields.AdditionalProperties.field_5

# Compare values
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
    fields = @{
        field_5 = "$CurrentDeletionThreshold"
        Status = $ComplianceStatus
    }
} | ConvertTo-Json -Depth 5

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
