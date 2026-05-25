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





<p>Hi Team,</p>

<p>Below is the TIP scanning report for Entra Connect.</p>

@{outputs('composeCssStyle')}

@{body('Create_HTML_table')}

<p>Regards,<br>
Automation Team</p>








<p>Below is the TIP scanning report for Entra Connect</p>

@{outputs('ComposeCssStyle')}

@{body('Create_HTML_table')}




<p>Below is the TIP scanning report for Entra Connect</p>

[ComposeCssStyle Output]

[Create HTML Table Output]









if(
equals(item()?['Status'],'Compliant'),
'🟢 Compliant',
'🔴 Non Compliant'
)






if(
equals(item()?['Status'],'Compliant'),
'<span style="color:green;font-weight:bold;">Compliant</span>',
'<span style="color:red;font-weight:bold;">Non Compliant</span>'
)






concat(
'SCB - Entra Connect Configuration Validation Report - ',
formatDateTime(utcNow(),'MMMM dd, yyyy')
)







<p><strong>INTERNAL</strong></p>

<br>

<p>Dear Team,</p>

<p>
Below is the TIP scanning report for Entra Connect as of date
<strong>@{formatDateTime(utcNow(),'MMMM dd, yyyy')}</strong>.
</p>

@{outputs('ComposeCssStyle')}

@{body('Create_HTML_table')}
