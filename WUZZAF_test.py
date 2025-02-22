import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest 

jop_title = []
campany_name = []
location_name = []
skills =[]

result = requests.get ("https://wuzzuf.net/search/jobs/?q=python")
src = result.content 
soup= BeautifulSoup(src , "lxml")

jop_titles = soup.find_all("h2" , {"class":"css-m604qf"})
campany_names = soup.find_all("a", {"class":"css-17s97q8"})
location_names= soup.find_all("span", {"class":"css-5wys0k"})
jop_skills =  soup.find_all("div", {"class":"css-y4udm8"})

for i in range (len (jop_titles)):
    jop_title.append(jop_titles[i].text )
    campany_name.append(campany_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(jop_skills[i].text)

file_list = [jop_title , campany_name , location_name , skills]
exported = zip_longest(*file_list)

with open ("D:/job.csv",'w') as myfile :
 wr= csv.writer(myfile)
 wr.writerow(["Jop Title", "Campany Name" , "Location", "Skills"])
 wr.writerows(exported)
  