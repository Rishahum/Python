data_set=[]
for links in data:
    data_set=links
# print(data_set)
DATA = {"Description":[], "ASIN":[], "Manufacturer":[]}
for link in data_set:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        new_webpage = requests.get("http://amazon.in" + link, headers=headers)
        if(new_webpage.status_code==200):
            print("Data fetched")
            soup = BeautifulSoup(new_webpage.content, "html.parser")
            
            # Description
            description = soup.find("ul", attrs={"class":'a-unordered-list a-vertical a-spacing-mini'})
            des_value = description.text
                # Title as a string value
            des_string = des_value.strip()

            # ASIN
            asin = soup.find("table", attrs={"id":'productDetails_detailBullets_sections1'}).find("td", attrs={"class":'a-size-base prodDetAttrValue'})
            asin_text = description.text
                # Title as a string value
            asin_string = asin_text.strip()

            #Manufacturer
            manu=soup.find("table", attrs={"id" : "productDetails_techSpec_section_1"}).find("td", attrs={"class":"a-size-base prodDetAttrValue"})
            manu_text = description.text
                # Title as a string value
            manu_string = manu_text.strip()

            DATA['Description'].append(des_string)
            DATA['ASIN'].append(asin_string)
            DATA['Manufacturer'].append(manu_string)
            
        else:
            print('url not found' , i)

DF = pd.DataFrame.from_dict(DATA)
DF.to_csv("amazondata.csv", header=True, index=False)
