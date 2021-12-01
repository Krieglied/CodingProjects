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
