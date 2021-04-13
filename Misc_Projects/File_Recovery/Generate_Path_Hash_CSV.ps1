# The CSV used to hold file path and MD5 Hash for the set of recovered files
if ((Test-Path 'Recovered_Files.csv') -eq $False)
{
    New-Item 'Recovered_Files.csv' -ItemType "File" | Out-Null
    Add-Content -Path 'Recovered_Files.csv' -Value '"FullPath","MD5Hash"'
}

$files = Get-ChildItem 'Recovered_Files\' -Recurse -File | Select FullName
Write-Host "WRITING TO FILE"
foreach($file in $files)
{
    $name = $file.FullName
    $hash = (Get-FileHash -Algorithm MD5 -Path $name).Hash
    Add-Content -Path 'Recovered_Files.csv' -Value "$name,$hash"
}

# The CSV used to hold file path and MD5 Hash for the set of known files, in the file storage area
if ((Test-Path 'Known_Files.csv') -eq $False)
{
    New-Item 'Known_Files.csv' -ItemType "File" | Out-Null
    Add-Content -Path 'Known_Files.csv' -Value '"FullPath","MD5Hash"'
}
$files = Get-ChildItem 'Known_Files\' -Recurse -File | Select FullName
Write-Host "WRITING TO FILE"
foreach($file in $files)
{
    $name = $file.FullName
    $hash = (Get-FileHash -Algorithm MD5 -Path $name).Hash
    Add-Content -Path 'Known_Files.csv' -Value "$name,$hash"
}
