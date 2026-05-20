# Get all baseline items from SharePoint
$BaselineItems = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All

# Create hashtable
$BaselineHash = @{}

# Populate hashtable
foreach ($Item in $BaselineItems) {

    $ConfigName  = $Item.Fields.AdditionalProperties.field_3
    $ConfigValue = $Item.Fields.AdditionalProperties.field_5

    # Skip blank rows
    if (![string]::IsNullOrWhiteSpace($ConfigName)) {
        $BaselineHash[$ConfigName] = $ConfigValue
    }
}

# Test
Write-Host "TLS Baseline Value:" -ForegroundColor Cyan
$BaselineHash["TLS"]





# Get current deletion threshold
$CurrentDeletionThreshold =
$Data.value.configuration.accidentalDeletionPrevention.alertThreshold

# Get baseline value from hashtable
$BaselineDeletionThreshold =
$BaselineHash["DeletionThreshold"]

# Compare
if (
    [int]$CurrentDeletionThreshold -eq
    [int]$BaselineDeletionThreshold
) {

    Write-Host "Deletion Threshold is Compliant" `
    -ForegroundColor Green
}
else {

    Write-Host "Deletion Threshold is Non Compliant" `
    -ForegroundColor Red

    Write-Host "Current: $CurrentDeletionThreshold"
    Write-Host "Baseline: $BaselineDeletionThreshold"
}
