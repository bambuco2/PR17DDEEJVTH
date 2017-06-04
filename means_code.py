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
    if (relat != "Unknown"):
        if year in years_relat:
            years_relat[year].append(relat)
        else:
            years_relat[year] = [relat]
    if (weapon != "Unknown"):
        if year in years_weapon:
            years_weapon[year].append(weapon)
        else:
            years_weapon[year] = [weapon]
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


mean_city = dict()
var_city = dict()
for key, val in dcity.items():
    mean_city[key] = np.mean(val)
    var_city[key] = np.var(val)

a = list()
for x, y in mean_city.items():
    a.append(y)
means = np.asarray(a)

plt.subplot(1, 1, 1)
plt.hist(means)
plt.xlabel("Variance of victim ages by city")

plt.tight_layout()
plt.show()

n = len(means)
mu = np.mean(means)
sigma2 = (n-1)/n * np.var(means)

plt.figure()
counts, bins, _ = plt.hist(means, normed=True, label="Sample")
pdf = [mvn.pdf(x, mu, sigma2) for x in bins]
plt.plot(bins, pdf, "-", label="Model", linewidth=2.0)
plt.xlabel("Variance of movie ratings")
plt.ylabel("P(X)")

plt.legend(loc=2)
plt.show()

qx = 1.3621

xr = np.linspace(-0.5, 2.5, 30)
width = xr[1] - xr[0]
Px = [mvn.pdf(x, mu, sigma2) * (xr[1] - xr[0]) for x in xr]

ltx = xr[xr > qx]

P_ltx = [mvn.pdf(x, mu, sigma2) * width for x in ltx]

p_value = np.sum(P_ltx)
plt.figure()
plt.plot(xr, Px, linewidth=2.0, )
plt.fill_between(ltx, 0, P_ltx, alpha=0.2, )
plt.text(qx, mvn.pdf(qx, mu, sigma2) * width,
         "p=%f" % p_value,
         horizontalalignment="right",
         verticalalignment="center", )

plt.xlabel("Variance of movie ratings")
plt.ylabel("P(X)")
plt.legend()
plt.show()