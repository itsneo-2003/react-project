Get-MgSiteListColumn `
    -SiteId $SiteId `
    -ListId $TransactionListId |
Select Name, DisplayName




      
Get-MgSiteListColumn `
    -SiteId $SiteId `
    -ListId $MasterListId |
Select Name, DisplayName




        # ============================
# TLS Control (BP-002)
# ============================

$RefNumber = "BP-002"

# Get transaction item
$TransactionItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TransactionListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq $RefNumber
}

# Get baseline item
$BaselineItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq $RefNumber
}

# Current TLS value
$CurrentTLS = ($FormattedTLS).Trim()

# Baseline TLS value
$BaselineTLS = (
    $BaselineItem.Fields.AdditionalProperties.field_5
).Trim()

# Compliance check
if ($CurrentTLS -eq $BaselineTLS) {
    $ComplianceStatus = "Compliant"
}
else {
    $ComplianceStatus = "Non Compliant"
}

# Update transaction list
$Body = @{
    field_5 = $CurrentTLS
    Status = $ComplianceStatus
} | ConvertTo-Json

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($TransactionItem.Id)/fields" `
    -Body $Body `
    -ContentType "application/json"

Write-Host "TLS Updated Successfully"
Write-Host "Status: $ComplianceStatus"
