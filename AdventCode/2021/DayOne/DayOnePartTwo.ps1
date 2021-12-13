# The original problem talked about three entry
# windows.  This is unnecessary, as the two compared
# windows will share two out of threee elements.
# In that case, you only need to compare the index
# and index + 3 position

$layers = Get-Content .\day1_input.txt
$counter = 0
$index = 0
foreach($layer in $layers[0..($layers.Length-3)])
{
    $top = [int]$layers[$index]
    $bottom = [int]$layers[$index+3]
    if($bottom -gt $top)
    {
        $counter++        
    }
    $index++
}
$counter
