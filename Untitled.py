
# coding: utf-8

# In[2]:

import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

from csv import DictReader
from collections import defaultdict
import statistics


# In[5]:

fp = open("database.csv", "rt",encoding="utf8")
data = DictReader(fp)


# In[10]:

i=0
spol_umor = defaultdict()
for a in data:
    if(a['Perpetrator Sex']!="Unknown"):
        spol_umor[i] = a['Perpetrator Sex']
        i=i+1
    


# In[11]:

spol_umor[0]


# In[12]:

import csv
with open('data.csv', 'w', newline='') as fp:
    b = csv.writer(fp, delimiter=',')
    for key,value in spol_umor.items():
        b.writerow([key,value])


# In[6]:

q=0
w=0
b=0
asian=0
for a in data:
    if(a['Perpetrator Race']!="Unknown"):
        if(a['Perpetrator Race']=="White"):
            w = w+1
        elif(a['Perpetrator Race']=="Black"):
            b = b+1
        elif(a['Perpetrator Race']=="Native American/Alaska Native"):
            q = q+1
        else:
            asian = asian +1

w = round(w*0.276)
b = round(b*0.874)
asian = round(asian*0.952)
q = round(q*0.991)

import csv
with open('race_umor.csv', 'w', newline='') as fp:
    f = csv.writer(fp, delimiter=',')
    for i in range(w):
        f.writerow(["White"])
    for i in range(b):
        f.writerow(["Black"])
    for i in range(asian):
        f.writerow(["Asian/Pacific Islander"])
    for i in range(q):
        f.writerow(["Native American/Alaska Native"])


# In[18]:




# In[19]:




# In[45]:

agencija2 = defaultdict()
agencija = defaultdict()
for a in data:
    agencija[a['Agency Type']] = 0
    agencija2[a['Agency Type']] = 0


# In[27]:

len(agencija)


# In[50]:

for a in data:
    agencija[a['Agency Type']]=agencija[a['Agency Type']]+1
    if(a['Crime Solved'] == "Yes"):
        agencija2[a['Agency Type']] = agencija2[a['Agency Type']]+1


# In[51]:

agencija


# In[52]:

agencija2


# In[54]:

agencija_umor = defaultdict()
for key,value in agencija.items():
    agencija_umor[key]=agencija2[key]/value


# In[56]:

agencija_umor


# In[89]:

orozje_umor = defaultdict()
i = 0
for a in data:
    if(a['Weapon'] != "Unknown"):
        orozje_umor[i] = a['Weapon']
        i = i+1


# In[90]:

import csv
with open('orozje.csv', 'w', newline='') as fp:
    b = csv.writer(fp, delimiter=',')
    for key,value in orozje_umor.items():
        b.writerow([key,value])


# In[120]:

z_orozje = defaultdict()
for a in data:
    if(a['Perpetrator Race'] == "Native American/Alaska Native" and a['Weapon']!="Unknown"):
        z_orozje[a['Weapon']] = 0


# In[122]:

for a in data:
    if(a['Perpetrator Race'] == "Native American/Alaska Native" and a['Weapon']!="Unknown"):
        z_orozje[a['Weapon']] = z_orozje[a['Weapon']] + 1
    


# In[140]:

z_orozje = defaultdict()
j = 0
for a in data:
    if(a['Perpetrator Race'] == "Asian/Pacific Islander" and a['Weapon']!="Unknown"):
        z_orozje[j] = a['Weapon']
        j = j+1


# In[141]:

import csv
with open('orozje_asian.csv', 'w', newline='') as fp:
    b = csv.writer(fp, delimiter=',')
    for key,value in z_orozje.items():
        b.writerow([key,value])


# In[168]:

CT_F = defaultdict()
CT_M = defaultdict()
i=0
j=0
for a in data:
    if(a['Perpetrator Sex'] == "Male" and a['Relationship']!="Unknown" and a['Relationship']!="Acquaintance"):
        CT_M[i] = a['Relationship']
        i = i+1
    elif(a['Perpetrator Sex'] == "Female" and a['Relationship']!="Unknown" and a['Relationship']!="Acquaintance"):
        CT_F[j] = a['Relationship']
        j = j+1


# In[169]:

import csv
with open('odnos_male.csv', 'w', newline='') as fp:
    b = csv.writer(fp, delimiter=',')
    for key,value in CT_M.items():
        b.writerow([key,value])


# In[170]:

import csv
with open('odnos_female.csv', 'w', newline='') as fp:
    b = csv.writer(fp, delimiter=',')
    for key,value in CT_F.items():
        b.writerow([key,value])


# In[163]:

CT_F


# In[37]:

P_age = defaultdict()
V_age = defaultdict()
j=0
i=0
for a in data:
    if(a['Perpetrator Age'] !="Unknown" and a['Perpetrator Age'] !="0" and a['Perpetrator Age'] !=" " and a['Perpetrator Age'] !="" and a['Victim Age'] !="Unknown" and a['Victim Age'] != "0" and a['Victim Age'] != " " and a['Victim Age'] != "" and int(a['Victim Age']) < 100and int(a['Perpetrator Age']) < 100):
        P_age[a['Perpetrator Age']] = 0 
        j = j+1


# In[39]:

j = 0
for a in data:
    if(a['Perpetrator Age'] !="Unknown" and a['Perpetrator Age'] !="0" and a['Perpetrator Age'] !=" " and a['Perpetrator Age'] !="" and a['Victim Age'] !="Unknown" and a['Victim Age'] != "0" and a['Victim Age'] != " " and a['Victim Age'] != "" and int(a['Victim Age']) < 100and int(a['Perpetrator Age']) < 100):
        P_age[a['Perpetrator Age']] = P_age[a['Perpetrator Age']]+1 
        j = j+1


# In[41]:

import csv
with open('age.csv', 'w', newline='') as fp:
    b = csv.writer(fp, delimiter=',')
    for key,value in P_age.items():
        b.writerow([key,value])


# In[6]:

outlr = defaultdict()
j = 0
for a in data:
    if(a['Perpetrator Sex'] == "Male" or a['Perpetrator Sex'] == "Female"):
        if(a['Victim Count']!="Unknown" and a['Victim Count']!="0" and a['Victim Count']!=0):
            outlr[j] = [a['Perpetrator Sex']]
            outlr[j].append(a['Victim Count'])
            j = j+1


# In[7]:

import csv
with open('VC.csv', 'w', newline='') as fp:
    b = csv.writer(fp, delimiter=',')
    for key,value in outlr.items():
        b.writerow([key,value[0],value[1]])


# In[ ]:



