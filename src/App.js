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






Write-Host "Current Length: $($CurrentTLS.Length)"
Write-Host "Baseline Length: $($BaselineTLS.Length)"

Compare-Object `
    ($CurrentTLS -split "`r?`n") `
    ($BaselineTLS -split "`r?`n")






# Normalize current TLS
$CurrentTLS = (
    $FormattedTLS.ToLower() `
    -replace '\r\n', "`n" `
    -replace '\s+', ' '
).Trim()

# Normalize baseline TLS
$BaselineTLS = (
    $BaselineTLS.ToLower() `
    -replace '\r\n', "`n" `
    -replace '\s+', ' '
).Trim()

# Compare
if ($CurrentTLS -eq $BaselineTLS) {
    Write-Host "TLS is Compliant" -ForegroundColor Green
}
else {
    Write-Host "TLS is Non Compliant" -ForegroundColor Red
}
