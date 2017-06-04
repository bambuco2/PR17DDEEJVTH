from builtins import print

from pylab import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from csv import DictReader
from collections import Counter
import scipy.cluster.hierarchy as sch
import scipy
import Orange
from sklearn.metrics import silhouette_score
from scipy.stats import multivariate_normal as mvn
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sympy.functions.special.error_functions import li
from NB import NaiveBayes


reader = DictReader(open("database.csv", "rt", encoding="utf -8"))
years_vage = dict()
years_page = dict()
years_relat = dict()
years_weapon = dict()
dcity = dict()
for row in reader:
    id = row["Record ID"]
    city = row["City"]
    state = row["State"]
    year = row["Year"]
    month = row["Month"]
    solved = row["Crime Solved"]
    v_sex = row["Victim Sex"]
    v_age = row["Victim Age"]
    v_race = row["Victim Race"]
    p_sex = row["Perpetrator Sex"]
    p_age = row["Perpetrator Age"]
    p_race = row["Perpetrator Race"]
    relat = row["Relationship"]
    weapon = row["Weapon"]
    if year in years_vage:
        years_vage[year].append(int(v_age))
    else:
        years_vage[year]= [(int(v_age))]
    if(p_age != '0' and p_age != " "):
        if year in years_page:
            years_page[year].append(int(p_age))
        else:
            years_page[year] = [(int(p_age))]
    if (int(year) >= 1980 and  int(year) <= 1989):
        if (relat != "Unknown"):
            if "1980s" in years_relat:
                years_relat["1980s"].append(relat)
            else:
                years_relat["1980s"] = [relat]
        if (weapon != "Unknown"):
            if "1980s" in years_weapon:
                years_weapon["1980s"].append(weapon)
            else:
                years_weapon["1980s"] = [weapon]
    elif (int(year) >= 1990 and  int(year) <= 1999):
        if (relat != "Unknown"):
            if "1990s" in years_relat:
                years_relat["1990s"].append(relat)
            else:
                years_relat["1990s"] = [relat]
        if (weapon != "Unknown"):
            if "1990s" in years_weapon:
                years_weapon["1990s"].append(weapon)
            else:
                years_weapon["1990s"] = [weapon]
    elif (int(year) >=2000):
        if (relat != "Unknown"):
            if "2000s" in years_relat:
                years_relat["2000s"].append(relat)
            else:
                years_relat["2000s"] = [relat]
        if (weapon != "Unknown"):
            if "2000s" in years_weapon:
                years_weapon["2000s"].append(weapon)
            else:
                years_weapon["2000s"] = [weapon]

    if(int(v_age)>0 and int(v_age)<120):
        if city in dcity:
            dcity[city].append(int(v_age))
        else:
            dcity[city] = [(int(v_age))]
numList = {x:len(y) for x,y in years_vage.items()}
avg_vage = {x:mean(y) for x,y in years_vage.items()}
avg_page = {x:mean(y) for x,y in years_page.items()}
relat_count = dict()
weapon_count = dict()

data = np.genfromtxt("database.csv", delimiter=",", skip_header=1, dtype=str)
#data = np.genfromtxt("titanic-training.csv", delimiter=",", skip_header=1, dtype=str)
transformed = data[-10000:, [10, 15, 16, 17, 18, 19]]
model = NaiveBayes()
model.fit(transformed)

#print(model.predict_instance(transformed[-1,:]))

predictions, confidences = model.predict(transformed)

for row, p, c in zip(transformed, predictions, confidences):
    print(row[0] == p)
    #print("Row=%s | predicted class=%s | confidence=%.5f" % (row, p, c))

learn, test = train_test_split(data)
learn_tar = learn[:,10]
test_tar = test[:,10]
model = LinearRegression()
model.fit(learn, learn_tar)

hx = model.predict(test)
mse_sum = mean_squared_error(hx, test_tar)
print(mse_sum)


listE = list()
listWea = list()
for key, val in years_relat.items():
    listE.append(Counter(val).most_common(6))

for key, val in years_weapon.items():
    listWea.append(Counter(val).most_common(6))

values = list()
text = list()
for i in listWea:
    for rel, num in i:
        values.append(num)
        text.append(rel)

colors = list()
for i in range(18):
    if i < 6:
        colors.append('r')
    elif i < 12:
        colors.append('b')
    else:
        colors.append('y')



bar1 = plt.bar(np.arange(18), values, color=colors)
plt.ylabel('Number of Murders')
plt.xlabel('Weapons')
plt.xticks(np.arange(18), text, rotation= 75)
red_patch = mpatches.Patch(color='red', label='1980s')
blue_patch = mpatches.Patch(color='blue', label='1990s')
yellow_patch = mpatches.Patch(color='yellow', label='2000s')
plt.legend(handles=[red_patch, blue_patch, yellow_patch])

plt.show()
