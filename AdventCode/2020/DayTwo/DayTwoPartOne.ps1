# Get the input from the provided file and start the counter at 0
$input = Get-Content -Path .\input2.txt
$count = 0
foreach($item in $input){
    # The lines from the file will need to be processed
    $line = $item.Split(' ')
    # The max, min and the character to be found need to be stored
    $min = $line[0].Split('-')[0]
    $max = $line[0].Split('-')[1]
    $charSelected = $line[1][0]    
    
    # The line will then be separated into the different character groups
    $pline = $item.ToCharArray() | group
    foreach($element in $pline){
        # Once the character group that matches our character is found,
        # then it needs to be determined if the password matches the criteria
        if($element.Name -eq $charSelected)
        {
            # For some reason, the Count property is off by 1, so that is adjusted here
            $value = $element.Count - 1
            if($value -le $max -and $value -ge $min)
            {
                $count = $count + 1
            }
            break
        }
    }
}
$count
