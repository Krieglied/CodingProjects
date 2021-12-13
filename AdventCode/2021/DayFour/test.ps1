function New-BingoCards{
    param(
        $data
    )
    $bingo_cards = @()
    $bingo_card = @{1=@();2=@();3=@();4=@();5=@();sum=0}
    $index = 0
    # The process of the cards starts on the third line
    # at index 2 of the array
    $last = $data[$data.Length-1]
    foreach($line in $data[2..($data.Length-1)])
    {
        # If the line is not empty, the card starts getting built
        if($line -ne "")
        {
            $numbers = [object]$line.Split(" +") | Where-Object {$_ -ne ""}
            $bingo_card.(++$index) += $numbers
            # The sum for the card starts with all the values
            # at the beginning.  As values get drawn, those values
            # will be subtracted from the sum
            foreach($number in $line.Split())
            {
                $bingo_card.sum += [int]$number
            }
        }
        else {
            $bingo_cards += $bingo_card
            $bingo_card = @{1=@();2=@();3=@();4=@();5=@();sum=0}
            $index = 0
        }
        if($line -eq $last)
        {
            $bingo_cards += $bingo_card
        }
    }
    return $bingo_cards
}
function Test-WinCondition{
    param(
        $card,
        $row,
        $index
    )
    $no_row = $True
    $no_column = $True
    # Test to see if the row will all equal the same value, i.e. ""
    # If not, set variable to False
    for($i = 1; $i -lt 5; $i++)
    {
        if($card[$row][$i] -ne $card[$row][$i-1])
        {
            $no_row = $False
            break
        }
    }
    # Test to see if the column will all equal the same value, i.e. ""
    # If not, set variable to False
    for($i = 2; $i -le 5; $i++)
    {
        if($card[$i][$index] -ne $card[$i-1][$index])
        {
            $no_column = $False
            break
        }
    }
    # If both row test and column test fail, return False
    if($no_row -eq $False -and $no_column -eq $False)
    {
        return $False
    }
    return $True
}
function Search-BingoCard{
    param(
        $draw_numbers,
        $card
    )
    foreach($number in $draw_numbers.Split(','))
    {
        $index = -1
        for($i = 1; $i -le ($card.Count - 1); $i++)
        {
            if($card[$i].Contains($number))
            {
                $card.sum -= $number
                $index = $card[$i].indexof($number)
                $card[$i][$index] = ""
                if(Test-WinCondition -card $card -row $i -index $index)
                {
                    $result = New-Object 'Tuple[int, int]' $card.sum, $number
                    return $result
                }
            }
        }
    }
    $result = New-Object 'Tuple[int, int]' 0, 0
    return $result
}
$bingo = Get-Content .\AdventCode\2021\DayFour\day4_test_data.txt
$bingo_draws = $bingo[0].Split(',')
$bingo_cards = New-BingoCards -data $bingo
$results = @()
foreach($card in $bingo_cards)
{
    $result = Search-BingoCard -draw_number $bingo_draws -card $card
    $results += $result
    $result = @()
}
$last_result = New-Object 'Tuple[int, int]' 0, 0
$order = @()
foreach($current in $results)
{
    $index = 0
    foreach($draw in $bingo_draws)
    {
        if([int]$draw -eq $current.Item2)
        {
            $order += $index
        }
        $index++
    }
}
$top = 0
$bottom = $null
$index = 0
foreach($element in $order)
{
    if($top -lt $element)
    {
        $top = $element
    }
    if($bottom -eq $null -or $element -lt $bottom)
    {
        $bottom = $element
    }
    $index++
}
if($last_result -eq (New-Object 'Tuple[int, int]' 0, 0))
{
    Write-Host "First Sum " $current.Item1 " the drawing card was " $current.Item2 " and answer is " ($current.Item1 * $current.Item2)
}
Write-Host "Last Sum " $last_result.Item1 " the drawing card was " $last_result.Item2 " and answer is " ($last_result.Item1 * $last_result.Item2)