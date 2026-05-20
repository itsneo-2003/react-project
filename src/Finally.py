# Deletion Threshold Control (BP-001)

# Get current deletion threshold value
$CurrentDeletionThreshold =
$Data.value.configuration.accidentalDeletionPrevention.alertThreshold

# Get BP-001 row from transaction list
$DeletionThresholdItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TransactionListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq "BP-001"
}

# Get baseline value from master list
$BaselineItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq "BP-001"
}

$BaselineDeletionThreshold =
$BaselineItem.Fields.AdditionalProperties.field_5

# Compare current vs baseline
if ([int]$CurrentDeletionThreshold -eq [int]$BaselineDeletionThreshold) {

    $ComplianceStatus = "Compliant"

    Write-Host "Deletion Threshold compliant" `
    -ForegroundColor Green
}
else {

    $ComplianceStatus = "Non Compliant"

    Write-Host "Deletion Threshold mismatch found" `
    -ForegroundColor Red

    Write-Host "Current: $CurrentDeletionThreshold" `
    -ForegroundColor Yellow

    Write-Host "Baseline: $BaselineDeletionThreshold" `
    -ForegroundColor Yellow
}

# Update transaction list
$Body = @{
    Status = $ComplianceStatus
    field_5 = "$CurrentDeletionThreshold"
} | ConvertTo-Json -Depth 5

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($DeletionThresholdItem.Id)/fields" `
    -Body $Body `
    -ContentType "application/json"

Write-Host ""
Write-Host "BP-001 Updated Successfully" `
-ForegroundColor Cyan

Write-Host "Status: $ComplianceStatus"
Write-Host "Deletion Threshold: $CurrentDeletionThreshold"
