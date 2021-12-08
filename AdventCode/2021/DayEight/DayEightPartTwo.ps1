function Get-SignalOutput
{
    param(
        $input_line_items,
        $output_line_items
    )
    $input_line_items = $input_line_items |  Where-Object {[String]::IsNullOrEmpty($_) -ne $True} | Sort-Object -Property Length 
    $lookup_table = [ordered]@{
        zero="";
        one=$input_line_items[0];
        two="";
        three="";
        four=$input_line_items[2];
        five="";
        six="";
        seven=$input_line_items[1];
        eight=$input_line_items[9];
        nine="";
    }
    foreach($item in $input_line_items)
    {
        if($item.Length -eq 5) 
        {
            $contained_in_seven = 0
            $contained_in_four = 0
            for($i = 0; $i -lt $lookup_table.four.Length; $i++)
            {
                if($i -lt $lookup_table.seven.Length -and $item.Contains($lookup_table.seven.toString()[$i]))
                {
                    $contained_in_seven++
                }
                if($item.Contains($lookup_table.four.toString()[$i])){
                    $contained_in_four++
                }
            }
            if($contained_in_seven -eq 3)
            {
                $lookup_table.three = $item
            }
            elseif($contained_in_four -eq 2)
            {
                $lookup_table.two = $item
            }
            else {
                $lookup_table.five = $item
            }
        }
        elseif($item.Length -eq 6) 
        {
            $contained_in_one = 0
            $contained_in_four = 0
            for($i = 0; $i -lt $lookup_table.four.Length; $i++)
            {
                if($i -lt $lookup_table.one.Length -and $item.Contains($lookup_table.one.toString()[$i]))
                {
                    $contained_in_one++
                }
                if($item.Contains($lookup_table.four.toString()[$i])){
                    $contained_in_four++
                }
            }
            if($contained_in_one -eq 2)
            {
                if($contained_in_four -eq 4)
                {
                    $lookup_table.nine = $item
                }
                else {
                    $lookup_table.zero = $item
                }
            }
            else {
                $lookup_table.six = $item
            }
        }
    }
    $value = ""
    foreach($item in $output_line_items)
    {
        if($item.Length -eq 2)
        {
            $value += "1"
            continue
        }
        if ($item.Length -eq 3)
        {
            $value += "7"
            continue
        }
        if ($item.Length -eq 4) 
        {
            $value += "4"
            continue
        }
        if ($item.Length -eq 7) 
        {
            $value += "8"
            continue
        }
        foreach($lookup in $lookup_table.GetEnumerator())
        {
            $found = $True
            if($lookup.Value.Length -ne $item.Length)
            {
                continue
            }
            for($i = 0; $i -lt $item.Length; $i++)
            {
                if($item.Contains($lookup.Value[$i]) -eq $False)
                {
                    $found = $False
                    break
                }
            }
            if($found)
            {
                if($lookup.Name -eq "two")
                {
                    $value += "2"
                }
                elseif($lookup.Name -eq "three")
                {
                    $value += "3"
                }
                elseif($lookup.Name -eq "five")
                {
                    $value += "5"
                }
                elseif($lookup.Name -eq "six")
                {
                    $value += "6"
                }
                elseif($lookup.Name -eq "nine")
                {
                    $value += "9"
                }
            }
        }

    }
    if($value -eq "")
    {
        return 0
    }
    return [Convert]::ToInt32($value)
}

$entries = Get-Content .\day8_input_Graham.txt
$input_values = @()
$output_values = @()
$total_sum = 0
foreach($entry in $entries)
{
    $input_values += @($entry.Split('|')[0])
    $output_values += @($entry.Split('|')[1])
}
for($i = 0; $i -lt $entries.Length; $i++)
{
    $sum = Get-SignalOutput -input_line_items $input_values[$i].Split() -output_line_items $output_values[$i].Split()
    $total_sum += $sum
    Write-Host "Line output is " $sum "and the new sum: " $total_sum
}