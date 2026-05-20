# Get TLS row from baseline list
$BaselineItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.fields.field_3 -eq "TLS"
}

# Get TLS baseline value
$BaselineTLS = $BaselineItem.fields.field_5

# Test output
Write-Host $BaselineTLS
