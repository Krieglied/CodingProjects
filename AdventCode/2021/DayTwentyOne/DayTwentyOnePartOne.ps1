$stats = Get-Content .\AdventCode\2021\DayTwentyOne\day21_input_Graham.txt
$player1 = 0
$player2 = 0
$player1_score = 0
$player2_score = 0
$turns = 0
$player = 1
$die = 1
$die_rolls = 0
foreach($line in $stats)
{
    if($line -match "Player 1")
    {
        $player1 = [int]$line[-1] - 48
    }
    else {
        $player2 = [int]$line[-1] - 48
    }
}

while($player1_score -lt 1000 -and $player2_score -lt 1000)
{
    $move = 0
    for($i = 0; $i -lt 3; $i++)
    {
        $move += $die++
        if($die -gt 100)
        {
            $die = 1
        }
        $die_rolls++
    }
    if($player -eq 1)
    {
        $player1 = ($player1 + $move) % 10
        if($player1 -eq 0)
        {
            $player1 = 10
        }
        $player1_score += $player1
        $player = 2
    }
    else {
        $player2 = ($player2 + $move) % 10
        if($player2 -eq 0)
        {
            $player2 = 10
        }
        $player2_score += $player2
        $player = 1
    }
    $turns++
}
$loser = IF($player1_score -gt $player2_score) {$player2_score} ELSE {$player1_score}
Write-Host "Loser Score " $loser "multiplied by Die Rolls " $die_rolls " : " ($die_rolls * $loser)