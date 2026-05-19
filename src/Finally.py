Get-MgSiteListColumn `
    -SiteId $SiteId `
    -ListId $TransactionListId |
Select Name, DisplayName




      
Get-MgSiteListColumn `
    -SiteId $SiteId `
    -ListId $MasterListId |
Select Name, DisplayName
