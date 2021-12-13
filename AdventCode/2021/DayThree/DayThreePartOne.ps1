# The two rates are computed by finding the most common value
# at each bit
$readings = Get-Content .\day3_input.txt
$common_bits = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

foreach ($reading in $readings)
{
    for($i = 0; $i -lt $reading.Length; $i++)
    {
        if($reading[$i] -match "1")
        {
            $common_bits[$i]++
        }
    }
}
$gamma = ""
$epsilon = ""

foreach($pos in $common_bits)
{
    if($pos -gt ($readings.Length / 2))
    {
        $gamma += "1"
        $epsilon += "0"  
    }
    else
    {
        
        $gamma += "0"
        $epsilon += "1"  
    }
}
Write-Host (([Convert]::ToInt32($gamma, 2)) * ([Convert]::ToInt32($epsilon, 2)))