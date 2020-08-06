echo off

cls
echo Downloading LASERS Weekly Graph
python3 C:\Users\Office\Documents\GitHub\Personal-Projects\LASERSWeeklyBandwidth\DownloadGraph.py

timeout 1 >nul

echo Emailing Report

powershell.exe C:\Users\Office\Documents\GitHub\Personal-Projects\LASERSWeeklyBandwidth\SendReport.ps1

timeout 1>nul
echo Complete!

timeout 2 >nul
exit
