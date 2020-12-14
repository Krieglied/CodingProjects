Given an executable, doing some reverse engineering on the file.

REtroll 1
	To find the plaintext password, opened the exe in Ghidra.  Once the main function was found, there is a variable == int check, that is checking for a password
REtroll 2
	Simply the hex value found during the check
REtroll 3
	The address when the cmp happens, simply the value on the left, no adjustment for relativity needed
REtroll	4
	Look at address mentioned, and its the string there
