$layers = Get-Content .\day1_input.txt
$counter = 0
$previous = $layers[0]
foreach ($layer in $layers)
{
    if([int]$layer -gt [int]$previous)
    {
        $counter++
    }
    $previous = $layer
}
$counter
