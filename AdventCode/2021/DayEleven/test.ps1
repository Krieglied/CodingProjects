$test_list = [System.Collections.ArrayList]@()
$test_tuple = New-Object 'Tuple[int, int]' 0, 0
$test_list.add($test_tuple)
(New-Object 'Tuple[int, int]' 0, 0) -in $test_list