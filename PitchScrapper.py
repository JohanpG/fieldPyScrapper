# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import html5lib

i=0
data = []
strData=""
f= open("pitchs.txt","w+")
f.write("[")
# Set the URL you want to webscrape from
urls = ['https://partidito.com/index.php?option=com_pitchesranking&Itemid=484&category_id=66&lang=en&page=1', 
'https://partidito.com/index.php?option=com_pitchesranking&Itemid=484&category_id=66&lang=en&page=2', 
'https://partidito.com/index.php?option=com_pitchesranking&Itemid=484&category_id=66&lang=en&page=3',
'https://partidito.com/index.php?option=com_pitchesranking&Itemid=484&category_id=66&lang=en&page=4',
'https://partidito.com/index.php?option=com_pitchesranking&Itemid=484&category_id=66&lang=en&page=5',
'https://partidito.com/index.php?option=com_pitchesranking&Itemid=484&category_id=66&lang=en&page=6']
for url in urls:
    # Connect to the URL
    response = requests.get(url)
    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html5lib")
    table = soup.find('table', attrs={'class':'table table-hover table-bordered'})
    #print(table)
    rows = table.find_all('tr')
    for row in rows:
        one_a_tag = row.find('a')
        if one_a_tag:
            i=i+1
            link = one_a_tag['href']
            print(link)
            # Connect to the URL
            responseIndividual = requests.get(link)
            # Parse HTML and save to BeautifulSoup object¶
            soup2 = BeautifulSoup(responseIndividual.text, "html5lib")
            objec = soup2.find('script', attrs={'type':'application/ld+json'})
            strobjec=str(objec)
            strobjec= strobjec.replace('<script type="application/ld+json">', "")
            strobjec= strobjec.replace("</script>", "")
            if i==1:
                strData= strobjec
            else:
                strData= strData + "," + strobjec
            #print(strobjec)
        #cols = row.find_all('td')
        #cols = [ele.text.strip() for ele in cols]
        #data.append([ele for ele in cols if ele]) # Get rid of empty values

#print(data)
#print(strData)

f.write(strData)
f.write("]")
f.close()

 



