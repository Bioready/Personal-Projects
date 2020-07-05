$email = "Bioready@gmail.com"
$secpassword = ConvertTo-SecureString "zlgbqpyimonokskz" -AsPlainText -Force

$credentials = New-Object Management.Automation.PSCredential ($email, $secpassword)

Send-MailMessage -SmtpServer smtp.gmail.com -Port 587  -UseSSL -Credential $credentials -To logan.delafosse@eatel.com -Cc lyman.abadie@eatel.com -From $email -Subject "Clarion Inn Report" -Body "Clarion Inn Report" -Verbose -Attachments C:\Users\Office\Documents\GitHub\Personal-Projects\ClarionInnReport\ClarionInnBandwidthReport.txt
