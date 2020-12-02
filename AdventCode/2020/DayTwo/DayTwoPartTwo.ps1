# Get the input from the provided file and start the counter at 0
$input = Get-Content -Path .\input2.txt
$count = 0
foreach($item in $input){
    # The lines from the file will need to be processed
    $line = $item.Split(' ')
    # The position numbers are grabbed from the beginning of the line, 
    # the numbers need to be adjusted since source doesn't start at index zero
    $position1 = $line[0].Split('-')[0] - 1
    $position2 = $line[0].Split('-')[1] - 1
    # Both the character to be looked at and the password itself need to be stored
    $charSelected = $line[1][0]
    $password = $line[2]

    # Check to see if one (and only one) of the positions in the password match the character
    if($password[$position1] -eq $charSelected -xor $password[$position2] -eq $charSelected)
    {
        $count = $count + 1
    }
}
$count
