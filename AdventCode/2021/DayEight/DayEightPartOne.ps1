$entries = Get-Content .\day8_input_Graham.txt
$output = @()
foreach($entry in $entries)
{
    $output += @($entry.Split('|')[1])
}
$sum = 0
for($i = 0; $i -lt ($output.Length); $i++)
{
    $line_items = $output[$i].Split()
    foreach($item in $line_items)
    {
        # Detecting the ones
        if($item.Length -eq 2)
        {
            $sum++
        }
        # Detecting the sevens
        if($item.Length -eq 3)
        {
            $sum++
        }
        # Detecting the fours
        if($item.Length -eq 4)
        {
            $sum++
        }
        # Detecting the eights
        if($item.Length -eq 7)
        {
            $sum++
        }
    }
}
$sum