<style>
table {
    border-collapse: collapse;
    width: 100%;
    font-family: Arial, sans-serif;
    font-size: 12px;
}

th {
    background-color: #0070A0;
    color: white;
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

td {
    border: 1px solid #ddd;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}
</style>




if(equals(item()?['Status'],'Compliant'),
'<span style="color:green;font-weight:bold;">Compliant</span>',
'<span style="color:red;font-weight:bold;">Non Compliant</span>')
