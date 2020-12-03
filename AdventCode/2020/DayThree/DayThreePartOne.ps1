$input = Get-Content -Path .\input3.txt
$start = 0
$treesCount = 0
foreach($item in $input){
    # Since the grid provided repeats, the input doesn't really need to be modified
    # Just restart the coordinates if the value goes past the end of the string
    if($start -ge $item.Length)
    {
        $start = $start - $item.Length
    }
    # We hit a tree! Increment counter
    if($item[$start] -eq '#')
    {
        $treesCount = $treesCount + 1
    }
    $start = $start + 3
    
}
$treesCount
