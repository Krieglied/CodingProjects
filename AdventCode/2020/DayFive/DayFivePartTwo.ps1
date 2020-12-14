$input = Get-Content -Path .\input5.txt
$seatIDs = @()
#Processes each line in the file
foreach($item in $input)
{
    $min, $max = 0, 127
    # The formula for processing is similiar to using the merge sort algorithm
    foreach($element in $item[0..($item.Length-4)])
    {
        if($element -eq 'F')
        {
            $max = [Math]::Floor($max - (($max - $min) / 2))
        }
        else
        {
            $min = [Math]::Ceiling($max - (($max - $min) / 2))
        }
    }
    $row = $max
    $min, $max = 0, 7
    # Repeat the processing for the last three items
    foreach($element in $item[($item.Length-3)..($item.Length-1)])
    {
        if($element -eq 'L')
        {
            $max = [Math]::Floor($max - (($max - $min) / 2))
        }
        else
        {
            $min = [Math]::Ceiling($max - (($max - $min) / 2))
        }
    }
    $seatID = $row * 8 + $max
    $seatIDs += $seatID
}
$seatIDs = $seatIDs | Sort-Object
$prevSeat = $seatIDs[0]
# The actual answer is the prevSeat, not the output
foreach($seat in $seatIDs[1..($seatIDs.Length-1)])
{
    if($prevSeat -ne ($seat - 1))
    {
        $seat
        break
    }
    $prevSeat = $seat
}
