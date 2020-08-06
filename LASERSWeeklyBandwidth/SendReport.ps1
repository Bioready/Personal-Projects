$email = "Bioready@gmail.com"
$secpassword = ConvertTo-SecureString "zlgbqpyimonokskz" -AsPlainText -Force
$credentials = New-Object Management.Automation.PSCredential ($email, $secpassword)

Send-MailMessage -SmtpServer smtp.gmail.com -Port 587  -UseSSL -Credential $credentials -To logan.delafosse@eatel.com -From $email -Subject "LASERS Report" -Body "LASERS Weekly Report" -Verbose -Cc romi.jenks@eatel.com -Attachments C:\Users\Office\Documents\GitHub\Personal-Projects\LASERSWeeklyBandwidth\LASERSWeeklyReport.png
