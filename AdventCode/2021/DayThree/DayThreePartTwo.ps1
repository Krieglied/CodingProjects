# This problem is the first for this year's challenges that I feel needs a write-up

# To handle computing both ratings, I built a function
# Parameters are the list to filter on, and the condition for how to handle an item
# if it matches the most common bit

function Get-Rating {
    
    param (
        $filtered_list,
        $equal_condition,
        $other_condition
    )
    $index = 0
    # Once the filtered list changes type to a string
    # The appropriate rating value has been found
    while($filtered_list.GetType().Name -notmatch "String")
    {
        $common_bit = 0
        # The commonality of the position bit has to be
        # recalculated after each filtering step
        foreach ($item in $filtered_list)
        {
            if($item[$index] -match "1")
            {
                $common_bit++
            }
        }
        # The filtering is based on three condition:
        # if the position bit matches the most common bit in the list
        # if there are an equal numbers of 0s and 1s
        # if the position bit matches the least common bit in the list
        if($common_bit -ge ($filtered_list.Length / 2))
        {
            $filtered_list = $filtered_list | Where-Object {$_[$index] -eq $equal_condition}
        }
        else
        {
            $filtered_list =$filtered_list | Where-Object {$_[$index] -eq $other_condition}
        }
        $index++
    }
    return [Convert]::ToInt32($filtered_list, 2)
}

$readings = Get-Content .\day3_input.txt

$o2_rating = Get-Rating -filtered_list $readings -equal_condition "1" -other_condition "0"
$co2_rating = Get-Rating -filtered_list $readings -equal_condition "0" -other_condition "1"

Write-Host ($o2_rating * $co2_rating)