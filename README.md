# PR17DDEEJVTH
Seminarska naloga, Podatkovno rudarjenje

## Data

We got data from [Kaggle](https://www.kaggle.com/murderaccountability/homicide-reports), it has reports about murders commited in US between 1980 and 2014. <br/>
Data comes in a cvs file, it is presented in a table with rows and columns, each row describes a murder and columns represent "attributes" about that murder, such as victim and perpetrators sex, weapon used, agency that tried to solve this murder, was it solved or not... <br/>
In this data there were also unknown values, always marked as "Unknown", for some atributs like weapons we tried to "calculate" which weapon was used, for this we used attributes such as victim and perpetrators sex.<br/>


## Findings

We tried to find some interesting things in the data.<br/>

1) First we wanted to know which sex and which race commits more murders in US.<br/>
![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/spol_umor.png)

![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/race_umor.png)
<br/>
So from this two graphs we can see that when it comes to sex murders are not even close. Males commit way more murders than Females.<br/>
And for race, we can see that whites and blacks are usually the perpetrators. Whites are slighty more frequent, but not by much.

2) Katera agencija je najbolj učinkovita pri reševanju umorov.<br/>

'County Police': 0.66<br/>
'Municipal Police': 0.68<br/>
'Regional Police': 0.79<br/>
'Sheriff': 0.78<br/>
'Special Police': 0.71<br/>
'State Police': 0.82<br/>
'Tribal Police': 0.92<br/>
<br/>
3) Frekvenca uporabljenih orožij/načinov umora.<br/>
![alt text](https://github.com/bambuco2/PR17DDEEJVTH/blob/master/orozja.png)




