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

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/race_umor.png)
<br/>
So from this two graphs we can see that when it comes to sex murders are not even close. Males commit way more murders than Females.<br/>
And for race, we can see that whites and blacks are usually the perpetrators. Whites are slighty more frequent, but not by much.

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

### Ranking attributes based on how heavily they contribute to crime being solved.<br/>
![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/atributi.jpg)

### Finding similarities between years

#### Average age of victims and perpetrators
For each year, I've calculated the average ages of both victims and perpetrators, to see are there any diffrences between them. As show by the data, the victims are 3-4 years older than the perpetrators
on average, and we see slight increase in the victims age in the years 2012 and 2014.

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/avg_age.png)

#### Relationship between victim and perpetrator

Here i've calculated the top 5 most recurring relationships that the victims had with the perpetrator:<br/>
1980 -> ('Acquaintance', 5499), ('Stranger', 3667), ('Wife',   915),  ('Friend', 828), 	 ('Husband', 630)<br/>
1981 -> ('Acquaintance', 5324), ('Stranger', 3698), ('Wife',   866),  ('Friend', 841), 	 ('Husband', 638)<br/>
1982 -> ('Acquaintance', 5105), ('Stranger', 3851), ('Wife',   817),  ('Friend', 717), 	 ('Husband', 535)<br/>
1983 -> ('Acquaintance', 4813), ('Stranger', 3355), ('Friend', 830),  ('Wife',   827), 	 ('Husband', 542)<br/>
1984 -> ('Acquaintance', 4632), ('Stranger', 3479), ('Wife',   791),  ('Friend', 727), 	 ('Girlfriend', 428)<br/>
1985 -> ('Acquaintance', 4864), ('Stranger', 2947), ('Wife',   851),  ('Friend', 790), 	 ('Girlfriend', 448)<br/>
1986 -> ('Acquaintance', 5075), ('Stranger', 2887), ('Friend', 1083), ('Wife', 814), 		 ('Girlfriend', 505)<br/>
1987 -> ('Acquaintance', 4775), ('Stranger', 2816), ('Friend', 1019), ('Wife', 788), 		 ('Girlfriend', 429)<br/>
1988 -> ('Acquaintance', 4720), ('Stranger', 2692), ('Friend', 836),  ('Wife', 765), 		 ('Girlfriend', 456)<br/>
1989 -> ('Acquaintance', 4941), ('Stranger', 2982), ('Friend', 1001), ('Wife', 646), 		 ('Girlfriend', 498)<br/>
1990 -> ('Acquaintance', 5143), ('Stranger', 3478), ('Friend', 931),  ('Wife', 718), 		 ('Girlfriend', 458)<br/>
1991 -> ('Acquaintance', 4760), ('Stranger', 3814), ('Friend', 867),  ('Wife', 737), 		 ('Girlfriend', 498)<br/>
1992 -> ('Acquaintance', 4582), ('Stranger', 3671), ('Friend', 938),  ('Wife', 724), 		 ('Girlfriend', 523)<br/>
1993 -> ('Acquaintance', 4701), ('Stranger', 3878), ('Friend', 967),  ('Wife', 735), 		 ('Girlfriend', 615)<br/>
1994 -> ('Acquaintance', 4611), ('Stranger', 3533), ('Friend', 838),  ('Wife', 656), 		 ('Girlfriend', 536)<br/>
1995 -> ('Acquaintance', 4088), ('Stranger', 3551), ('Friend', 661),  ('Wife', 633), 	     ('Girlfriend', 506)<br/>
1996 -> ('Acquaintance', 3836), ('Stranger', 2837), ('Wife',   636),  ('Friend', 556), 	 ('Girlfriend', 460)<br/>
1997 -> ('Acquaintance', 3567), ('Stranger', 2522), ('Wife',   575),  ('Friend', 511),		 ('Girlfriend', 466)<br/>
1998 -> ('Acquaintance', 3102), ('Stranger', 2290), ('Wife',   640),  ('Friend', 469), 	 ('Girlfriend', 458)<br/>
1999 -> ('Acquaintance', 2769), ('Stranger', 1887), ('Wife',   556),  ('Girlfriend', 460),  ('Friend', 440)<br/>
2000 -> ('Acquaintance', 2436), ('Stranger', 2061), ('Wife',   597),  ('Girlfriend', 450),  ('Friend', 324)<br/>
2001 -> ('Acquaintance', 2517), ('Stranger', 2295), ('Wife',   608),  ('Girlfriend', 453),  ('Friend', 383)<br/>
2002 -> ('Acquaintance', 2675), ('Stranger', 2441), ('Wife',   595),  ('Girlfriend', 467),  ('Friend', 411)<br/>
2003 -> ('Acquaintance', 2709), ('Stranger', 2280), ('Wife',   542),  ('Girlfriend', 487),  ('Friend', 388)<br/>
2004 -> ('Acquaintance', 2605), ('Stranger', 2289), ('Wife',   565),  ('Girlfriend', 467),  ('Friend', 346)<br/>
2005 -> ('Acquaintance', 2616), ('Stranger', 2501), ('Wife',   581),  ('Girlfriend', 485),  ('Friend', 348)<br/>
2006 -> ('Acquaintance', 2809), ('Stranger', 2407), ('Wife',   556),  ('Girlfriend', 459),  ('Friend', 391)<br/>
2007 -> ('Stranger', 	  2431), ('Acquaintance', 2392), ('Wife',   572),  ('Friend', 508), 	 ('Girlfriend', 493)<br/>
2008 -> ('Acquaintance', 2242), ('Stranger', 1754), ('Wife',   567),  ('Friend', 511), 	 ('Girlfriend', 504)<br/>
2009 -> ('Acquaintance', 2226), ('Stranger', 2207), ('Wife',   627),  ('Girlfriend', 480),  ('Friend', 460)<br/>
2010 -> ('Stranger',     2142), ('Acquaintance', 2065), ('Wife',   594),  ('Girlfriend', 509),  ('Friend', 442)<br/>
2011 -> ('Acquaintance', 2082), ('Stranger', 1989), ('Wife',   551),  ('Girlfriend', 494),  ('Friend', 421)<br/>
2012 -> ('Stranger',     2137), ('Acquaintance', 1992), ('Wife',   525),  ('Girlfriend', 517),  ('Friend', 396)<br/>
2013 -> ('Acquaintance', 1924), ('Stranger', 1863), ('Wife',   515),  ('Girlfriend', 488),  ('Friend', 384)<br/>
2014 -> ('Stranger',     1961), ('Acquaintance', 1821), ('Wife',   502),  ('Girlfriend', 430),  ('Friend', 382)<br/>

We can see that acquaintance and stranger are the two most common relationships between the victim and the perpetrator throughout the years. The diffrences between early 1980s to the rest is that there are significant amount
of husbands being killed at that period, but later we see that the main perpetrators are mostly men, with wife and girlfriend being the usual victims.

#### Weapons used

Here is the date for the top 3 weapons used throughout the years:<br/>
1980 -> ('Handgun', 10845), ('Knife', 4255), ('Blunt Object', 2397)<br/>
1981 -> ('Handgun', 9952), ('Knife', 3945), ('Blunt Object', 2186)<br/>
1982 -> ('Handgun', 9164), ('Knife', 4107), ('Blunt Object', 2283)<br/>
1983 -> ('Handgun', 8832), ('Knife', 4120), ('Blunt Object', 2354)<br/>
1984 -> ('Handgun', 8109), ('Knife', 3675), ('Blunt Object', 2159)<br/>
1985 -> ('Handgun', 8066), ('Knife', 3727), ('Blunt Object', 2173)<br/>
1986 -> ('Handgun', 8992), ('Knife', 3997), ('Blunt Object', 2421)<br/>
1987 -> ('Handgun', 8342), ('Knife', 3675), ('Blunt Object', 2230)<br/>
1988 -> ('Handgun', 8673), ('Knife', 3484), ('Blunt Object', 2253)<br/>
1989 -> ('Handgun', 9607), ('Knife', 3483), ('Blunt Object', 2207)<br/>
1990 -> ('Handgun', 10784), ('Knife', 3569), ('Blunt Object', 2229)<br/>
1991 -> ('Handgun', 12197), ('Knife', 3461), ('Blunt Object', 2336)<br/>
1992 -> ('Handgun', 13333), ('Knife', 3337), ('Blunt Object', 2196)<br/>
1993 -> ('Handgun', 14038), ('Knife', 2998), ('Blunt Object', 2204)<br/>
1994 -> ('Handgun', 13599), ('Knife', 2823), ('Blunt Object', 2101)<br/>
1995 -> ('Handgun', 11931), ('Knife', 2584), ('Blunt Object', 2151)<br/>
1996 -> ('Handgun', 9893), ('Knife', 2498), ('Blunt Object', 1943)<br/>
1997 -> ('Handgun', 9072), ('Knife', 2215), ('Blunt Object', 1840)<br/>
1998 -> ('Handgun', 8357), ('Knife', 2023), ('Blunt Object', 1893)<br/>
1999 -> ('Handgun', 7493), ('Knife', 1868), ('Blunt Object', 1836)<br/>
2000 -> ('Handgun', 7567), ('Knife', 1908), ('Blunt Object', 1692)<br/>
2001 -> ('Handgun', 7816), ('Knife', 1976), ('Blunt Object', 1821)<br/>
2002 -> ('Handgun', 8239), ('Knife', 1950), ('Blunt Object', 1800)<br/>
2003 -> ('Handgun', 8706), ('Knife', 2013), ('Blunt Object', 1780)<br/>
2004 -> ('Handgun', 8174), ('Knife', 2060), ('Blunt Object', 1803)<br/>
2005 -> ('Handgun', 8401), ('Knife', 2099), ('Firearm', 1842)<br/>
2006 -> ('Handgun', 8845), ('Knife', 2048), ('Firearm', 1752)<br/>
2007 -> ('Handgun', 8543), ('Firearm', 2142), ('Knife', 2011)<br/>
2008 -> ('Handgun', 7310), ('Firearm', 2132), ('Knife', 2074)<br/>
2009 -> ('Handgun', 7554), ('Firearm', 2149), ('Knife', 2010)<br/>
2010 -> ('Handgun', 7084), ('Firearm', 2261), ('Knife', 1899)<br/>
2011 -> ('Handgun', 7221), ('Firearm', 1969), ('Knife', 1899)<br/>
2012 -> ('Handgun', 7418), ('Firearm', 2235), ('Knife', 1765)<br/>
2013 -> ('Handgun', 6733), ('Firearm', 2491), ('Knife', 1659)<br/>
2014 -> ('Handgun', 6594), ('Firearm', 2526), ('Knife', 1747)<br/>

From 1980 to 2004, we can see that the usual weapon choices of Handgun, Knife and Blunt Object does not change. But since 2005, Firearm are starting to get more popular, with guns occupying the top 2 spots from 2007 to 2014.

### Average ages by city

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/means.png)
![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/px.png)

Here you can see the normal distribution of average victim ages by cities.<br/>
And here are the cities that are in the bottom 5% of the results.<br/>
Allamakee | mean : 3.000<br/>
Baca | mean : 12.500<br/>
Baraga | mean : 24.000<br/>
Barnes | mean : 22.167<br/>
Bottineau | mean : 24.250<br/>
Bronx | mean : 8.000<br/>
Burt | mean : 25.333<br/>
Carlisle | mean : 14.000<br/>
Cavalier | mean : 21.000<br/>
Chase | mean : 16.000<br/>
Cloud | mean : 25.714<br/>
Crowley | mean : 13.000<br/>
Dickey | mean : 24.500<br/>
Divide | mean : 15.000<br/>
Doniphan | mean : 1.000<br/>
Dubuque | mean : 22.833<br/>
Dukes | mean : 23.750<br/>
Edmunds | mean : 11.778<br/>
Fall River | mean : 25.800<br/>
Fallon | mean : 18.000<br/>
Faulk | mean : 15.000<br/>
Foard | mean : 25.000<br/>
Gasconade | mean : 6.333<br/>
Glasscock | mean : 22.000<br/>
Goodhue | mean : 22.778<br/>
Guthrie | mean : 25.667<br/>
Hanson | mean : 16.000<br/>
Hot Springs | mean : 24.800<br/>
Ida | mean : 10.000<br/>
Jo Daviess | mean : 21.000<br/>
Labette | mean : 24.938<br/>
Lipscomb | mean : 24.500<br/>
Major | mean : 25.800<br/>
McCone | mean : 3.000<br/>
Merrick | mean : 20.857<br/>
Missaukee | mean : 24.600<br/>
Montour | mean : 22.500<br/>
Mountrail | mean : 24.429<br/>
O'Brien | mean : 25.750<br/>
Palo Alto | mean : 17.000<br/>
Parmer | mean : 25.556<br/>
Powder River | mean : 18.000<br/>
Ralls | mean : 25.333<br/>
Ransom | mean : 11.500<br/>
Rawlins | mean : 18.000<br/>
Red Lake | mean : 20.000<br/>
Richardson | mean : 23.667<br/>
Ringgold | mean : 9.000<br/>
Sibley | mean : 25.000<br/>
Skagway-Hoonah-Angoon | mean : 17.000<br/>
Somervell | mean : 25.714<br/>
Stanton | mean : 25.500<br/>
Storey | mean : 23.333<br/>
Swift | mean : 22.667<br/>
Traverse | mean : 17.000<br/>
Treasure | mean : 25.000<br/>
Tripp | mean : 19.000<br/>
Wirt | mean : 23.250<br/>
Yates | mean : 21.600<br/>
Yellow Medicine | mean : 25.333<br/>
