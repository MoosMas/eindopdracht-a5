import pandas as pd
from datetime import datetime
from datetime import timedelta
import lib_bamboo as bamboo
import os

os.system("cls")
print("Working...")

data = pd.read_excel("../files/Hockey_Tweede_klasse_tussenstand.xlsx")
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
data = data.sort_values("datum")

#Informatievraag 1
sumFile = open("../files/sum.txt", "w", encoding="UTF-8")
totalViolations = data["overtredingen"].sum()
sumFile.write(str(totalViolations))
sumFile.close()

#Informatievraag 2
averageFile = open("../files/average.txt", "w", encoding="UTF-8")
meanViolations = data["overtredingen"].mean()
averageFile.write(str(round(meanViolations)))
averageFile.close()

#Informatievraag 3
zwartBoekFile = open("../files/zwartboek.txt", "w", encoding="UTF-8")
zwartBoekSorted = data.sort_values("overtredingen", ascending=False)
zwartBoek = zwartBoekSorted.head(5)
zwartBoekFile.write(bamboo.prettify(zwartBoek, type="zwartboek"))
zwartBoekFile.close()

#Informatievraag 4
eregalerijFile = open("../files/eregalerij.txt", "w", encoding="UTF-8")
checkDays = 14
date_check = datetime.now() - timedelta(days=checkDays)
print(date_check)

eregalerijSorted = data.sort_values("datum", ascending=True)

filter1 = (data["overtredingen"] < 2)
data_filtered = data[filter1]
filter2 = (data_filtered["datum"] > date_check)
eregalerij = data_filtered[filter2]

eregalerijFile.write(bamboo.prettify(eregalerij, type="eregalerij"))
eregalerijFile.close()

print("Done!")
