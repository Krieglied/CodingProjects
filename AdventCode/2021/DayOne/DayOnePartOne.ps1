$layers = Get-Content .\day1_input.txt
$counter = 1
$previous = $layers[0]
foreach ($layer in $layers)
{
    if($layer -gt $previous)
    {
        $counter++
    }
    $previous = $layer
}
$counter