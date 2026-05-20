$TransactionResponse = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items?expand=fields"

$TransactionResponse.value[0] | Format-List *





$TransactionResponse.value[0].fields | Format-List *.




$BaselineResponse = Invoke-MgGraphRequest `
-Method GET `
-Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$MasterListId/items?expand=fields"

$BaselineResponse.value[0].fields | Format-List *




