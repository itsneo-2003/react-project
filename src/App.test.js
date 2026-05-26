$outputpath =
"D:\Temp_transaction\Sync_rules_trans.txt"

$CurrentHash["Sync Rules"] |
Format-Table -AutoSize |
Out-String |
Set-Content $outputpath
