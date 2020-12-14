Given a set of text files that had obfuscated powershell code, figure out what the code does.

May-FlowerShell-1
	The text file has a pretty short powershell (invoke-expression that stores the flag with the variable $turkey). Some character replace makes the full line
	'$turkey=fivectf{turkeys_go_gobble_gobble}'
May-FlowerShell-2
	Running Get-Variable lists all variables in shell.  With the command is run, a new variable baste is created with the flag
