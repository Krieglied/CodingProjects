#Since I've had to rebuild my Windows media server a few times, I figured it was time to build a default clean Windows script, mostly to remove unnecessary Microsoft items, but also to get some default configurations done as well.

#Windows Default Clean Script

#Setting up the IP for the new machine
Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notmatch 'Loopback'} | Select-Object -Property InterfaceIndex | New-NetIPAddress -IPAddress $newIP -PrefixLength 24
Get-NetConnectionProfile | Set-NetConnectionProfile -NetworkCategory "Private"
Rename-Computer -NewName $hostname
Get-Printer | Where Name -Match $brand | Set-Printer -Shard $True
Start-Process .\Printer_Scan_Program_Install.exe
Start-Process .\ChromeSetup.exe "/Silent /Install"
#Removal of alot of the Microsoft Default Bloatware
Get-AppxPackage Microsoft.Microsoft3DViewer | Remove-AppxPackage
Get-AppxPackage Microsoft.549981C3F5F10 | Remove-AppxPackage
Get-AppxPackage Microsoft.WindowsFeedbackHub | Remove-AppxPackage
Get-AppxPackage Microsoft.ZuneVideo | Remove-AppxPackage
Get-AppxPackage Microsoft.ZuneMusic | Remove-AppxPackage
Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage
Get-AppxPackage Microsoft.WindowsMaps | Remove-AppxPackage
Get-AppxPackage Microsoft.WindowsCamera | Remove-AppxPackage
Get-AppxPackage Microsoft.MicrosoftSolitaireCollection | Remove-AppxPackage
Get-AppxPackage Microsoft.WindowsStore | Remove-AppxPackage
Get-AppxPackage Microsoft.MixedReality.Portal | Remove-AppxPackage
Get-AppxPackage *Office* | Remove-AppxPackage
Get-AppxPackage Microsoft.People | Remove-AppxPackage
Get-AppxPackage Microsoft.SkypeApp | Remove-AppxPackage
Get-AppxPackage SpotifyAB.SpotifyMusic | Remove-AppxPackage
Get-AppxPackage Microsoft.Getstarted | Remove-AppxPackage
Get-AppxPackage Microsoft.WindowsSoundRecorder | Remove-AppxPackage
Get-AppxPackage Microsoft.BingWeather | Remove-AppxPackage
Get-AppxPackage *xboxapp* | Remove-AppxPackage
Get-AppxPackage Microsoft.Xbox.TCUI | Remove-AppxPackage
Get-AppxPackage Microsoft.XboxGameOverlay | Remove-AppxPackage
Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage
Get-AppxPackage Microsoft.XboxIdentityProvider | Remove-AppxPackage
Get-AppxPackage Microsoft.XboxSpeechToTextOverlay | Remove-AppxPackage
Get-AppxPackage Microsoft.YourPhone | Remove-AppxPackage
#Removal of OneDrive
taskkill /f /im OneDrive.exe
C:\Windows\SysWOW64\OneDriveSetup.exe /uninstall
#This is to remove the Quick Access section for File Explorer
New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ -Name HubMode -PropertyType DWORD -Value 1
#Remember to change default browser
