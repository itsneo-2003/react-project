# ==========================================
# TLS CONTROL (BP-002)
# ==========================================

# Get TLS row from transaction list
$TLSItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TransactionListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq "BP-002"
}

# ==========================================
# GET CURRENT REVIEW COUNT
# ==========================================

$CurrentReview = $TLSItem.Fields.AdditionalProperties.Review

if ([string]::IsNullOrWhiteSpace($CurrentReview)) {
    $NewReview = 1
}
else {
    $NewReview = [int]$CurrentReview + 1
}

# Current timestamp
$LastRunDateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# ==========================================
# GET BASELINE TLS ITEM
# ==========================================

$BaselineItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq "BP-002"
}

$BaselineText = $BaselineItem.Fields.AdditionalProperties.field_5

# ==========================================
# CONVERT CURRENT TLS TO HASH TABLE
# ==========================================

$IgnoreFields = @(
    "PSComputerName",
    "RunspaceId",
    "PSShowComputerName"
)

$CurrentTLSHash = @{}

$TLS.PSObject.Properties | ForEach-Object {

    if ($_.Name -notin $IgnoreFields) {

        $Key = $_.Name.Trim()
        $Value = "$($_.Value)".Trim()

        $CurrentTLSHash[$Key] = $Value
    }
}

# ==========================================
# CONVERT BASELINE TLS TO HASH TABLE
# ==========================================

$BaselineTLSHash = @{}

$BaselineText -split "`r?`n" | ForEach-Object {

    if ($_ -match "^(.*?)\s*:\s*(.*)$") {

        $Key = $matches[1].Trim()
        $Value = $matches[2].Trim()

        $BaselineTLSHash[$Key] = $Value
    }
}

# ==========================================
# COMPARE ALL TLS FIELDS
# ==========================================

$MismatchFound = $false
$MismatchDetails = @()

foreach ($Key in $BaselineTLSHash.Keys) {

    if ($CurrentTLSHash.ContainsKey($Key)) {

        $CurrentValue = $CurrentTLSHash[$Key]
        $BaselineValue = $BaselineTLSHash[$Key]

        if ($CurrentValue -ne $BaselineValue) {

            $MismatchFound = $true

            $MismatchDetails +=
            "$Key mismatch | Current: $CurrentValue | Baseline: $BaselineValue"
        }
    }
    else {

        $MismatchFound = $true
        $MismatchDetails += "$Key missing in current TLS"
    }
}

# ==========================================
# SET COMPLIANCE STATUS
# ==========================================

if ($MismatchFound) {

    $ComplianceStatus = "Non Compliant"

    Write-Host ""
    Write-Host "TLS mismatch found:" -ForegroundColor Red

    $MismatchDetails | ForEach-Object {
        Write-Host $_ -ForegroundColor Yellow
    }
}
else {

    $ComplianceStatus = "Compliant"

    Write-Host ""
    Write-Host "TLS fully compliant" -ForegroundColor Green
}

# ==========================================
# UPDATE TRANSACTION LIST
# ==========================================

$Body = @{
    Review          = $NewReview
    LastRunDateTime = $LastRunDateTime
    Status           = $ComplianceStatus
    field_5          = $FormattedTLS
} | ConvertTo-Json -Depth 5

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($TLSItem.Id)/fields" `
    -Body $Body `
    -ContentType "application/json"

# ==========================================
# FINAL OUTPUT
# ==========================================

Write-Host ""
Write-Host "TLS Updated Successfully" -ForegroundColor Cyan
Write-Host "Status: $ComplianceStatus"
Write-Host "Review Number: $NewReview"
Write-Host "LastRunDateTime: $LastRunDateTime"
