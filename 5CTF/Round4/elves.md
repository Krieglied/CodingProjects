Given an input text file, some file searches for specific string patterns were done.

elves-1
	How many Dominoes were made? Unzip folder and ran 'ls -Recurse | Select-String -Pattern "Dominoes" | Measure-Object' within the folder, close to grep -R
elves-2
	How many Sound toys were made? ls -Recurse | Select-String -Pattern "Sound" | Measure-Object
elves-3
	How many toy trains were made? ls -Recurse | Select-String -Pattern "Toy Train" | Measure-Object
