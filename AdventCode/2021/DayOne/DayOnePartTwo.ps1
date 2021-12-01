$layers = Get-Content .\day1_input.txt
$counter = 0
$index = 0
foreach($layer in $layers)
{
    $top = [int]$layers[$index] + [int]$layers[$index+1] + [int]$layers[$index+2]
    $bottom = [int]$layers[$index+1] + [int]$layers[$index+2] + [int]$layers[$index+3]
    if($bottom -gt $top)
    {
        $counter++        
    }
    $index++
    if(($layers.Length - $index) -lt 2)
    {
        break
    }
}
$counter