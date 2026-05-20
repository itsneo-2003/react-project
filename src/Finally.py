# BP-003 - AD Sync Scheduler

$RefNumber = "BP-003"

# Get current AD Sync Scheduler
$ADSync = Get-ADSyncScheduler

# Fields to ignore (dynamic values)
$IgnoreFields = @(
    "NextSyncCycleStartTimeInUTC",
    "SyncCycleInProgress"
)

# Convert current scheduler to hashtable
$CurrentScheduler = @{}

$ADSync.PSObject.Properties | ForEach-Object {
    if ($IgnoreFields -notcontains $_.Name) {
        $CurrentScheduler[$_.Name] = "$($_.Value)".Trim()
    }
}

# Format current value for transaction list
$FormattedADSync = (
    $CurrentScheduler.GetEnumerator() |
    Sort-Object Name |
    ForEach-Object {
        "$($_.Key) : $($_.Value)"
    }
) -join "`r`n"

# Get BP-003 transaction row
$TransactionItem = $TransactionResponse.value | Where-Object {
    $_.fields.field_2 -eq $RefNumber
}

# Get BP-003 baseline row
$BaselineItem = $BaselineResponse.value | Where-Object {
    $_.fields.field_2 -eq $RefNumber
}

# Convert baseline into hashtable
$BaselineScheduler = @{}

$BaselineText = $BaselineItem.fields.field_5

$BaselineText -split "`r?`n" | ForEach-Object {

    if ($_ -match "^(.*?)\s*:\s*(.*)$") {

        $Name = $matches[1].Trim()
        $Value = $matches[2].Trim()

        if ($IgnoreFields -notcontains $Name) {
            $BaselineScheduler[$Name] = $Value
        }
    }
}

# Compliance check
$Mismatches = @()

foreach ($Key in $BaselineScheduler.Keys) {

    if (-not $CurrentScheduler.ContainsKey($Key)) {
        $Mismatches += "$Key missing in current scheduler"
        continue
    }

    if ($CurrentScheduler[$Key] -ne $BaselineScheduler[$Key]) {
        $Mismatches += "$Key mismatch"
        $Mismatches += "Current: $($CurrentScheduler[$Key])"
        $Mismatches += "Baseline: $($BaselineScheduler[$Key])"
    }
}

# Final compliance result
if ($Mismatches.Count -eq 0) {
    $ComplianceStatus = "Compliant"
}
else {
    $ComplianceStatus = "Non Compliant"
}

# Debug output
if ($Mismatches.Count -gt 0) {
    Write-Host ""
    Write-Host "AD Sync Scheduler mismatch found" -ForegroundColor Red
    $Mismatches | ForEach-Object {
        Write-Host $_ -ForegroundColor Yellow
    }
}

# Update transaction list
$Body = @{
    field_5 = $FormattedADSync
    Status = $ComplianceStatus
} | ConvertTo-Json

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($TransactionItem.id)/fields" `
    -Body $Body `
    -ContentType "application/json"

# Final output
Write-Host ""
Write-Host "BP-003 Updated Successfully" -ForegroundColor Cyan
Write-Host "Status: $ComplianceStatus"




