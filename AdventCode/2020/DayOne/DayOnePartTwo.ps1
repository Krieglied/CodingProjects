# Grab all the numbers from the input file
# Sort the numbers to make processing quicker (as ints, in descending order)
$input = Get-Content -Path .\input.txt | Sort-Object {[int]$_} -Descending
$reverseinput = $input | Sort-Object {[int]$_}

# Iterate through each item in the number list
foreach ($item in $input) {

    # This checks to see if it's possible for the item with the lowest two other values
    # To be less than 2020 to speed up computation
    if (([int]$item + [int]$reverseinput[0] + [int]$reverseinput[1]) -gt 2020) {
        continue
    }
    # If three values could add up to 2020, now to process through them
    else {
        # These for loops will check the reverse input array, since that has the highest
        # likelihood of having the values that match the conditions
        foreach($element1 in $reverseinput){
            if(([int]$item + [int]$element1) -gt 2020){
            break
            }
            foreach($element2 in $reverseinput){
                if(([int]$item + [int]$element1 + [int]$element2) -gt 2020){
                    break
                }

                if(([int]$item + [int]$element1 + [int]$element2) -eq 2020){
                    $result = [int]$item * [int]$element1 * [int]$element2
                    $result
                }
            }
        }
    }
}
