$masterlist = @()

foreach($line in Get-content .\freq.txt)
{
    $masterlist += $line
}
foreach($item in $masterlist)
{
    foreach($compare in $masterlist)
    {
        $result = Compare-Object -ReferenceObject $item.ToCharArray() -DifferenceObject $compare.ToCharArray()
        
        if($result.Length -eq 0)
        {
            continue
        }
        if($result.Length -eq 2)
        {
            Write-Host "Found boxes"
            Write-Host "Boxes are $item and $compare"
        }
    }
}
