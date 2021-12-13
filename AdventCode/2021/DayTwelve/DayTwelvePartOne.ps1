$caves = Get-Content .\day12_test_data_A.txt
$spots = @()
foreach($cave in $caves)
{
    $spot = New-Object 'Tuple[string, string]' $cave.Split('-')[0] , $cave.Split('-')[1]
    $spots += $spot
}
$system = @{}
foreach($spot in $spots)
{
    if($system.Keys -notcontains $spot.Item1)
    {
        $system.($spot.Item1) = @()
    }
    $system.($spot.Item1) += $spot.Item2
}
$system