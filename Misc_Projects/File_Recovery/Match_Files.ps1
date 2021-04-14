# This text file will list any file found in the known good list
if ((Test-Path 'Match_File.txt') -eq $False)
{
    New-Item 'Match_File.txt' -ItemType "File" | Out-Null
}
# This CSV was created from the set of recovered files
$recovered_files = Import-Csv -Path 'Recovered_Files.csv'
# This CSV was created from the set of known files, in the storage area
$known_files = Import-Csv -Path 'Known_Files.csv'

foreach($rfile in $recovered_files)
{
    foreach($kfile in $known_files)
    {
        if($rfile.MD5Hash -eq $kfile.MD5Hash)
        {
            # Once the files were matched using MD5 (i figued that would be good enough for comparison purposes,
            # The locations would be added to the text file, and the loop would move onto the next item to check
            $message = $rfile.FullPath + " is also located at " + $kfile.FullPath
            Add-Content -Path 'Match_List.txt' -Value $message
            break
        }
    }
}
