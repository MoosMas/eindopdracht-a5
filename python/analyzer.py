import pandas as pd
from datetime import datetime
from datetime import timedelta
import lib_bamboo as bamboo
import os

os.system("cls")
print("Working...")

matches = pd.read_excel("../files/Hockey_Tweede_klasse_tussenstand.xlsx")
matches["datum"] = pd.to_datetime(matches["datum"], format="%d/%m/%Y")
matches = matches.sort_values("datum")

#Informatievraag 1: Totaal aantal overtredingen
sumFile = open("../files/sum.txt", "w", encoding="UTF-8")
totalViolations = matches["overtredingen"].sum()
sumFile.write(str(totalViolations))
sumFile.close()

#Informatievraag 2: Gemiddelde aantal overtredingen
averageFile = open("../files/average.txt", "w", encoding="UTF-8")
meanViolations = matches["overtredingen"].mean()
averageFile.write(str(round(meanViolations)))
averageFile.close()

#Informatievraag 3: Zwartboek (wedstrijden met meeste overtredingen)
zwartBoekFile = open("../files/zwartboek.txt", "w", encoding="UTF-8")
zwartBoekSorted = matches.sort_values("overtredingen", ascending=False)
zwartBoek = zwartBoekSorted.head(5)
zwartBoekFile.write(bamboo.prettify(zwartBoek, type="zwartboek"))
zwartBoekFile.close()

#Informatievraag 4: Eregalerij (wedstrijden met minder dan 2 overtredingen in de afgelopen 14 dagen)
eregalerijFile = open("../files/eregalerij.txt", "w", encoding="UTF-8")
checkDays = 14
date_check = datetime.now() - timedelta(days=checkDays)
print(date_check)

eregalerijSorted = matches.sort_values("datum", ascending=True)

filter1 = (matches["overtredingen"] < 2)
matches_filtered = matches[filter1]
filter2 = (matches_filtered["datum"] > date_check)
eregalerij = matches_filtered[filter2]

eregalerijFile.write(bamboo.prettify(eregalerij, type="eregalerij"))
eregalerijFile.close()

os.system("cls")

print("Done!")
