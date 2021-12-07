$crab_pos = Get-Content .\day7_input.txt
$crab_pos = $crab_pos.Split(',')
$max_pos = $crab_pos | Measure-Object -Maximum

$crab_pos = $crab_pos | Sort-Object
if ($crab_pos.count %2 ) {
    #odd
    $median = $crab_pos[[math]::Floor($crab_pos.count / 2)]
}
else {
    #even
    $median = ($crab_pos[$crab_pos.Count / 2], $crab_pos[$crab_pos.count / 2 - 1] |Measure-Object -Average).average
}

$answer_sum = -1
$range = 10
$found = $False
$previous_sum = -1
while($found -eq $False)
{
    foreach($align in ($median - 30)..($median + 30))
    {
        $current_sum = 0
        foreach($crab in $crab_pos)
        {
            $current_sum += [Math]::Abs([int]$crab - $align)
        }
        if($answer_sum -eq -1)
        {
            $answer_sum = $current_sum
            continue
        }
        if($current_sum -lt $answer_sum)
        {
            $answer_sum = $current_sum
        }
    }

    if($previous_sum -eq -1)
    {
        $previous_sum = $answer_sum
        $range += 10
        continue
    }
    if($previous_sum -eq $answer_sum)
    {
        $found = $True
    }
    $range += 10
}
$answer_sum
