# -----------------------------------------
# GET TRACKER LIST ID
# -----------------------------------------

$TrackerList = Get-MgSiteList -SiteId $SiteId |
Where-Object { $_.DisplayName -eq "EntraConnect-TIP-Automation-Tracker" }

$TrackerListId = $TrackerList.Id


# -----------------------------------------
# GET TRACKER ITEM (ONLY 1 ROW)
# -----------------------------------------

$TrackerItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TrackerListId `
    -ExpandProperty "fields"

$TrackerFields = $TrackerItem.Fields.AdditionalProperties


# -----------------------------------------
# GET LAST RUN VALUE SAFELY
# -----------------------------------------

if ([string]::IsNullOrWhiteSpace($TrackerFields.LastRun)) {
    $LastRun = 0
}
else {
    $LastRun = [int]$TrackerFields.LastRun
}

$NewRun = $LastRun + 1


# -----------------------------------------
# GET SAME TIMESTAMP FOR ALL ROWS
# -----------------------------------------

$CurrentDateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"


# -----------------------------------------
# GET ALL TRANSACTION LIST ITEMS
# -----------------------------------------

$TransactionItems = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TransactionListId `
    -ExpandProperty "fields" `
    -All


# -----------------------------------------
# UPDATE ALL TRANSACTION ROWS
# -----------------------------------------

foreach ($Item in $TransactionItems) {

    $Body = @{
        Review = $NewRun
        LastRunDateTime = $CurrentDateTime
    } | ConvertTo-Json

    Invoke-MgGraphRequest `
        -Method PATCH `
        -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($Item.Id)/fields" `
        -Body $Body `
        -ContentType "application/json"
}


# -----------------------------------------
# UPDATE TRACKER LIST
# -----------------------------------------

$TrackerBody = @{
    LastRun = $NewRun
    LastReviewDate = $CurrentDateTime
} | ConvertTo-Json

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TrackerListId/items/$($TrackerItem.Id)/fields" `
    -Body $TrackerBody `
    -ContentType "application/json"


Write-Host "Completed successfully"
Write-Host "Review Number: $NewRun"
Write-Host "LastRunDateTime: $CurrentDateTime"











Get-MgSiteListColumn `
    -SiteId $SiteId `
    -ListId $TrackerListId |
Select Name, DisplayName





        
# ------------------------------------------------
# GET TRACKER LIST ID
# ------------------------------------------------

$TrackerList = Get-MgSiteList -SiteId $SiteId |
Where-Object { $_.DisplayName -eq "EntraConnect-TIP-Automation-Tracker" }

$TrackerListId = $TrackerList.Id


# ------------------------------------------------
# GET TRACKER ITEM (ONLY 1 ROW)
# ------------------------------------------------

$TrackerItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TrackerListId `
    -ExpandProperty "fields"

$TrackerFields = $TrackerItem.Fields.AdditionalProperties


# ------------------------------------------------
# GET LAST RUN SAFELY
# ------------------------------------------------

if ([string]::IsNullOrWhiteSpace($TrackerFields.LastRun)) {
    $LastRun = 0
}
else {
    $LastRun = [int]$TrackerFields.LastRun
}

$NewRun = $LastRun + 1


# ------------------------------------------------
# SAME TIMESTAMP FOR ALL ROWS
# ------------------------------------------------

$CurrentDateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"


# ------------------------------------------------
# GET ALL TRANSACTION LIST ITEMS
# ------------------------------------------------

$TransactionItems = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TransactionListId `
    -ExpandProperty "fields" `
    -All


# ------------------------------------------------
# UPDATE ALL TRANSACTION LIST ROWS
# ------------------------------------------------

foreach ($Item in $TransactionItems) {

    $Body = @{
        Review = $NewRun
        LastRunDateTime = $CurrentDateTime
    } | ConvertTo-Json

    Invoke-MgGraphRequest `
        -Method PATCH `
        -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($Item.Id)/fields" `
        -Body $Body `
        -ContentType "application/json"
}


# ------------------------------------------------
# UPDATE TRACKER LIST
# ------------------------------------------------
# ReviewReference = internal name for LastReviewDate

$TrackerBody = @{
    LastRun = $NewRun
    ReviewReference = $CurrentDateTime
} | ConvertTo-Json

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TrackerListId/items/$($TrackerItem.Id)/fields" `
    -Body $TrackerBody `
    -ContentType "application/json"


# ------------------------------------------------
# SUCCESS MESSAGE
# ------------------------------------------------

Write-Host "Completed Successfully"
Write-Host "Review Number: $NewRun"
Write-Host "LastRunDateTime: $CurrentDateTime"
