echo off

cls
echo Downloading Clarion Inn Monthly Graph
python3 C:\Users\Office\Documents\GitHub\Personal-Projects\ClarionInnReport\DownloadGraph.py

timeout 1 >nul

echo Moving File to Proper Directory..
move C:\Users\Office\Downloads\*traffic*.csv C:\Users\Office\Documents\GitHub\Personal-Projects\ClarionInnReport

timeout 1 >nul

echo Running Bandwidth Report
python3 C:\Users\Office\Documents\GitHub\Personal-Projects\ClarionInnReport\FindPeakBandwidth.py > ClarionInnBandwidthReport.txt

timeout 1 >nul

echo Removing CSV file
del C:\Users\Office\Documents\GitHub\Personal-Projects\ClarionInnReport\*traffic*.csv


timeout 1 >nul
echo Emailing Report

powershell.exe C:\Users\Office\Documents\GitHub\Personal-Projects\ClarionInnReport\SendReport.ps1

timeout 1>nul
echo Complete!

timeout 2 >nul
exit
