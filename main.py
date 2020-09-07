import re
import sys

TCNO = input("Enter TC ID: ")

ResultRegex = re.fullmatch("^[1-9]{1}[0-9]{9}[02468]{1}$", TCNO)

if ResultRegex:
    ResultRegex = True
else:
    ResultRegex = False
    print("NON-Valid Turkish NID!!!")
    sys.exit()

dizi = list(map(int, TCNO))

toplam = 0
for i in range(0, 10):
    toplam += dizi[i]

if dizi[10] == toplam % 10:
    ResultLastDigit = True
else:
    ResultLastDigit = False

SumY1 = 0
for x in range(0, 10, 2):
    SumY1 += dizi[x]
SumY2 = 0
for y in range(1, 9, 2):
    SumY2 += dizi[y]

Result10thDigit = dizi[9] == ((SumY1 * 7) - SumY2) % 10

Result = ResultLastDigit & Result10thDigit & ResultRegex

if Result:
    print("Valid Turkish NID")
else:
    print("NON-Valid Turkish NID!!!")
