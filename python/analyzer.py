import pandas as pd
from datetime import datetime
from datetime import timedelta
import lib_bamboo as bamboo
import os

os.system("cls") #Deze regel nog invullen! Hoe maak je het scherm leeg?
print("Working...")

data = pd.read_excel("Hockey_Tweede_klasse_tussenstand.xlsx")
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
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
checkDays = 14
date_check = datetime.now() - timedelta(days=14)

eregalerijSorted = data.sort_values("datum", ascending=True)

filter = ((data["overtredingen"] < 2) & (data["datum"] > date_check))
eregalerij = eregalerijSorted[filter]

eregalerijFile.write(bamboo.prettify(eregalerij, type="eregalerij"))
eregalerijFile.close()






print("Done!")
