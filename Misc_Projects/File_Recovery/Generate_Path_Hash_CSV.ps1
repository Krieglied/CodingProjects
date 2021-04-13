# The CSV used to hold file path and MD5 Hash for the set of recovered files
if ((Test-Path E:\Recovered_Files_List.csv) -eq $False)
{
    New-Item E:\Recovered_Files_List.csv -ItemType "File" | Out-Null
    Add-Content -Path E:\Recovered_Files_List.csv -Value '"FullPath","MD5Hash"'
}

$files = Get-ChildItem 'E:\Recovered_Files\' -Recurse -File | Select FullName
Write-Host "WRITING TO FILE"
foreach($file in $files)
{
    $name = $file.FullName
    $hash = (Get-FileHash -Algorithm MD5 -Path $name).Hash
    Add-Content -Path E:\Recovered_Files_List.csv -Value "$name,$hash"
}

# The CSV used to hold file path and MD5 Hash for the set of known files, in the file storage area
if ((Test-Path E:\Known_Files_List.csv) -eq $False)
{
    New-Item E:\Known_Files_List.csv -ItemType "File" | Out-Null
    Add-Content -Path E:\Known_Files_List.csv -Value '"FullPath","MD5Hash"'
}
$files = Get-ChildItem '\\192.168.86.80\Network Share\Content\' -Recurse -File | Select FullName
Write-Host "WRITING TO FILE"
foreach($file in $files)
{
    $name = $file.FullName
    $hash = (Get-FileHash -Algorithm MD5 -Path $name).Hash
    Add-Content -Path E:\Known_Files_List.csv -Value "$name,$hash"
}
