function New-BingoCards{
    param(
        $data
    )
    $bingo_cards = @()
    $bingo_card = @{1=@();2=@();3=@();4=@();5=@();sum=0;name=0}
    $index = 0
    $id = 1
    # The process of the cards starts on the third line
    # at index 2 of the array
    $last = $data[$data.Length-1]
    foreach($line in $data[2..($data.Length-1)])
    {
        # If the line is not empty, the card starts getting built
        if($line -ne "")
        {
            $numbers = [object]$line.Split(" +") | Where-Object {$_ -ne ""}
            $bingo_card.($index+1) += $numbers
            # The sum for the card starts with all the values
            # at the beginning.  As values get drawn, those values
            # will be subtracted from the sum
            foreach($number in $line.Split())
            {
                $bingo_card.sum += [int]$number
            }
            $bingo_card.name = $id
            $index++
        }
        else {
            $bingo_cards += $bingo_card
            $bingo_card = @{1=@();2=@();3=@();4=@();5=@();sum=0;name=0}
            $index = 0
            $id++
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
    $no_column = $False
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
    $times_drawn = 0
    foreach($number in $draw_numbers.Split(','))
    {
        $index = -1
        for($i = 1; $i -le 5; $i++)
        {
            if($card[$i].Contains($number))
            {
                $card.sum -= $number
                $index = $card[$i].indexof($number)
                $card[$i][$index] = ""
                if(Test-WinCondition -card $card -row $i -index $index)
                {
                    $result = $card.sum, $number, $card.name
                    return $result
                }
            }
        }
        $times_drawn++
    }
    $result = 0, 0, 0
    return $result
}

$bingo = Get-Content .\day4_input.txt
$bingo_draws = $bingo[0].Split(',')
$bingo_cards = New-BingoCards -data $bingo
$results = @()
foreach($card in $bingo_cards)
{
    $result = Search-BingoCard -draw_number $bingo_draws -card $card
    $results += $result
    $result = @()
}
foreach($draw in $bingo_draws)
{
    for($i = 1; $i -lt $results.Length; $i += 3)
    {
        if($draw -eq $results[$i])
        {
            Write-Host $results[$i+1] " card to win has sum " $results[$i-1] " the drawing card was " $results[$i] " and answer is " ($results[$i-1] * [int]$results[$i])
            break
        }
    }
}