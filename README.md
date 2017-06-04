# PR17DDEEJVTH
Seminarska naloga, Podatkovno rudarjenje

## Problem

Determining the next possible victim in the US and the likelihood of the case being solved, by analyzing a data from previous homicide reports from 1980-2014.

## Data

We got data from [Kaggle](https://www.kaggle.com/murderaccountability/homicide-reports), it has reports about murders commited in US between 1980 and 2014. <br/>
Data comes in a csv file, it is presented in a table with rows and columns, each row describes a murder and columns represent "attributes" about that murder, such as victim and perpetrators sex, weapon used, agency that tried to solve this murder, was it solved or not... <br/>
In this data there were also unknown values, always marked as "Unknown", for some atributs like weapons we tried to "calculate" which weapon was used, for this we used attributes such as victim and perpetrators sex.<br/>


## Findings

We tried to find some interesting things in the data.<br/>

### Which sex and which race commits more murders in US.<br/>
![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/spol_umor.png)

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/race_umr.png)
<br/>
So from this two graphs we can see that when it comes to sex murders are not even close. Males commit way more murders than Females.<br/>
And for race, black and whites are usually the perpetrators, even though blacks are a minority in the US, population of blacks in US is at about 12.6%. We got stats about Race and ethnicity in US from [Wikipedia](https://en.wikipedia.org/wiki/Race_and_ethnicity_in_the_United_States), so take those numbers with a grain of salt. 

### Which agencies are the most effective when it comes to murder solving .<br/>

'County Police': 0.66<br/>
'Municipal Police': 0.68<br/>
'Special Police': 0.71<br/>
'Sheriff': 0.78<br/>
'Regional Police': 0.79<br/>
'State Police': 0.82<br/>
'Tribal Police': 0.92<br/>
<br/>
From this we can see that Tribal and State police are the most effective when it comes to murder solving, but this is also effected by number of the cases they have to solve.<br/>
Tribal police has only had about 50 murders between 1980 and 2014, thus giving them more time to solve each murder.<br/>

### Frequency of weapons used.<br/>
![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/orozja.png)

From this graph we can see, that handgun is the most popular weapon when it comes to murders. No suprise there, since pretty much anyone can get a handgun in US. They are cheap, easy to use and also distances you from your victim.

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/orozje_native.png)

But if we look at weapon used and we devide them in groups by races, we can see an interesting result for Native Americans, they 
prefer knife over handguns unlike other races.

### Relationship between perpetrator and victim.<br/>

When we look at relationship between victim and perpetrator we see nothing interesting, victims know their perpetrators, "Acquaintance" is the most common relationship.
But if we devide relationship into two groups by sex of the perpetrators, we can see some very interesting things.


![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/odnos_male.png)
The first graph represents males, they seem to murder complete strangers.<br/>
![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/odnos_female.png)
If we look at this graph, that represents females, we can see, that their victims are usually very personal, like husband and boyfriend.

### Ranking attributes based on how much information they provide, when it comes to classifying crimes as being solvable or not.<br/>
We have used measures such as Information Gain and Information gain ratio, to see, which attributes contribute the most when it comes to determining whether a random crime can be solved or not, based on presented attributes for that crime. 
<br/>
![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/atributi.jpg)<br/>
From this picture, we can see that Perpetrators sex and Perpetrators race are the strongest attributes. Based on our calculations, these two attributes are the strongest, when it comes to determining whether a random crime can/will be solved or not. 
In other words, if Perpetrators sex and Perpetrators race are known for a random crime, there is a high chance that we already know whether this crime can be solved or not.


### Finding similarities between years

#### Average age of victims and perpetrators
For each year, I've calculated the average ages of both victims and perpetrators, to see are there any diffrences between them. As show by the data, the victims are 3-4 years older than the perpetrators
on average, and we see slight increase in the victims age in the years 2012 and 2014.

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/avg_age.png)

#### Relationship between victim and perpetrator

Here i've calculated the top 6 most recurring relationships that the victims had with the perpetrator through the decades:<br/>

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/relat_decad.png)

We can see that acquaintance and stranger are the two most common relationships between the victim and the perpetrator throughout the years. In the 1980s there are a lot of husband appearing as victims, 
but later we see that the main perpetrators are mostly men, with wife and girlfriend being the usual victims.

#### Weapons used

Here is the date for the top 6 weapons used throughout the years:<br/>

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/weap_decad.png)

In the 1980s and 1990s, we can see that the usual weapon choices of Handgun, Knife and Blunt Object does not change. But in the 2000s, there has been an increased use of firearms.

### Average ages by city

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/age_means.png)

Here you can see the normal distribution of average victim ages by cities. From this we can see that there are some cities that are outliers and have an average age of the victims bellow 20, and arround 80.


