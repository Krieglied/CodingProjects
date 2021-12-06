$field =@()
foreach($i in 0..999)
{
    $row = @()
    foreach($j in 0..999)
    {
        $row += "."
    }
    $field += $row
}
$field



$coords = Get-Content .\day5_input.txt
$coords = $coords.replace('->', ' ')
$coords = $coords.Split('  ') | Where-Object {$_ -ne ''}
$coords