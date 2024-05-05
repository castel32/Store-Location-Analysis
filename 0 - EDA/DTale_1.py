#First time to play with DTale EDA Tool
#pip install dtale
import dtale
import pandas as pd

#CENSUS2021
#/Users/c32/Documents/NYCDSA/Projects/DATA/Census 2021/ACSDP5Y2021.DP05-Data.csv
df=pd.read_csv('/Users/c32/Documents/NYCDSA/Projects/DATA/Census 2021/ACSDP5Y2021.DP05-Data.csv')
d= dtale.show(df)
d

#CENSUS2011
#/Users/c32/Documents/NYCDSA/Projects/DATA/Census 2011/ACSDP5Y2011.DP05-Data.csv
df=pd.read_csv('/Users/c32/Documents/NYCDSA/Projects/DATA/Census 2011/ACSDP5Y2011.DP05-Data.csv')
d= dtale.show(df)
d

#IRS
#2021
#/Users/c32/Documents/NYCDSA/Projects/DATA/IRS/21zpallagi/21zpallagi.csv
df1=pd.read_csv('/Users/c32/Documents/NYCDSA/Projects/DATA/IRS/21zpallagi/21zpallagi.csv')
d1= dtale.show(df1)
d1
#2011
#/Users/c32/Documents/NYCDSA/Projects/DATA/IRS/2011zipcode/11zpallagi.csv
df2=pd.read_csv('/Users/c32/Documents/NYCDSA/Projects/DATA/IRS/2011zipcode/11zpallagi.csv')
d2= dtale.show(df2)
d2



#Fast Food SAMPLE
#/Users/c32/Documents/NYCDSA/Projects/DATA/Fast Food America/Datafiniti_Fast_Food_Restaurants.csv

#Walmart
#/Users/c32/Documents/NYCDSA/Projects/walmart_2018_11_06.csv



df2021=pd.read_csv('/Users/c32/Documents/NYCDSA/Projects/DATA/Census 2021/ACSDP5Y2021.DP05-Data.csv')
df2011=pd.read_csv('/Users/c32/Downloads/ACSDP5Y2011.DP05_2024-05-02T150505/ACSDP5Y2011.DP05-Data.csv')

myzip_21=df2021[df2021['NAME'].str.contains('10002')]
myzip_11=df2011[df2011['NAME'].str.contains('10002')]

print(myzip_11)
print(myzip_21)

df=pd.read_csv('/Users/c32/Documents/NYCDSA/Projects/DATA/IRS/21zpallagi/21zpallagi.csv')
d= dtale.show(df)
d
