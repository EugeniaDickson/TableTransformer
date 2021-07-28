# TableTransformer
This script transforms tables from a Master Loadsheet to LoadBoy-compatible.

The script will:
* find all .xlsx files that have “US-MTV-“ in file names
* transform them
* save them in a separate folder named “transformed” with adding a “_tf” suffix to the file names
* save a log in a separate file “log.txt” in the “transformed” folder (and print it in the terminal)

Prerequisites:
- numpy
- pandas

Instructions:
1.	First of all, we need to extract each sheet from the master loadsheet so we have separate excel file for each building.
I used this excel add-on to do this: https://www.extendoffice.com/download/kutools-for-excel.html
2.	Throw transform.py in a folder with those exported excel sheets.
3.	Run transform.py in an IDE (VS Code or whatever) terminal.

Notes:
For the “required” column the script will replace “MISSING” with “YES”, and all other different values with “NO”
