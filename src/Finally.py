# Get current deletion threshold value
$CurrentDeletionThreshold = $Data.value.configuration.accidentalDeletionPrevention.alertThreshold

# Get BP-001 row from transaction list
$DeletionThresholdItem = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items?expand=fields" |
Select-Object -ExpandProperty value |
Where-Object {
    $_.fields.AdditionalProperties.field_2 -eq "BP-001"
}

# Get BP-001 row from baseline list
$BaselineItem = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$MasterListId/items?expand=fields" |
Select-Object -ExpandProperty value |
Where-Object {
    $_.fields.AdditionalProperties.field_2 -eq "BP-001"
}

# Get baseline threshold value
$BaselineDeletionThreshold = [int](
    $BaselineItem |
    Select-Object -First 1 |
    ForEach-Object {
        $_.Fields.AdditionalProperties.field_5
    }
)

# Compare current vs baseline
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
