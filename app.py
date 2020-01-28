url = 'https://www.nationsonline.org/oneworld/country_code_list.htm'

from bs4 import BeautifulSoup
import requests
import json
import csv

page = requests.get(url).text

# print('page',dir(page),page.text)
soup = BeautifulSoup(page,'html.parser')

# print(soup)

# get table with id CountryCode
countryCodeTable = soup.find('table')
# countryCodeTable = countryCodeTable.find('tbody')
# print('countryCodeTable',countryCodeTable)
trs = countryCodeTable.find_all('tr')
print('trs',trs)
countriesAlpha2Data = []
with open('filewithflag.csv','w') as f:
    writer = csv.writer(f)
    for tr in trs:
        tds = tr.find_all('td')
        print(len(tds))
        if(len(tds)>=3):
            country = tds[1].text
            alpha2 = tds[2].text
            countriesAlpha2Data.append([country,alpha2])
            writer.writerow([country,alpha2])

    f.close()

print(countriesAlpha2Data[:10])
