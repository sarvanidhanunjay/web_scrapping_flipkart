#web scrapping from flipkart
import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=mobilephones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
#collecting names of mobiles
names=soup.find_all('div',class_="_4rR01T")
#print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
#print(name)  
#collecting price information
prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
#print(prices)
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
#print(price)
#collecting ratings information
ratings=soup.find_all('div',class_="_3LWZlK")
#print(ratings)
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
#print(rate)
df=pd.DataFrame()
print(df)
print("_________________________________________________")
df["NAMES"]=name
df["prices"]=price
df["ratings"]=rate
print(df)
print("____________________________")
df.to_csv("mobiles.csv")

  