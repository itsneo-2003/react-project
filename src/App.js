# Get TLS row from baseline list
$BaselineItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_3 -eq "TLS"
}

# Get TLS baseline value
$BaselineTLS = $BaselineItem.Fields.AdditionalProperties.field_5

# Test output
Write-Host $BaselineTLS




# Normalize both values
$CurrentTLS = $FormattedTLS.Trim()
$BaselineTLS = $BaselineTLS.Trim()

# Compare
if ($CurrentTLS -eq $BaselineTLS) {
    Write-Host "TLS is Compliant" -ForegroundColor Green
}
else {
    Write-Host "TLS is Non Compliant" -ForegroundColor Red
}
