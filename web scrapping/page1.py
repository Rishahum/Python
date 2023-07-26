from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def get_link(soup):
    
    try: 
        links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Store the links
        links_list = []

    # Loop for extracting links from Tag Objects
        for link in links:
            links_list.append(link.get('href'))

    
    except AttributeError:
        links_list=" "
        
    return links_list

# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"class":'a-size-medium a-color-base a-text-normal'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        price_att = soup.find("span", attrs={'class':'a-price'})
        price = price_att.find("span", attrs={'class':'a-offscreen'}).string.strip()

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()

        except:
            price = ""

    return price
# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'class':'a-size-base s-underline-text'}).string.strip()

    except AttributeError:
        review_count = ""	

    return review_count

# creating database
d = {"Product URL":[], "Product Name":[], "Product Price":[], "Rating":[],"Number of reviews":[]}

for i in range(0,11):
    URL ='https://www.amazon.in/s?k=bags&crid=3D5UAEE4CSMJ6&sprefix=%2Caps%2C2539&ref=nb_sb_noss_2'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
    page = requests.get(URL, headers=headers)
    if(page.status_code==200):
        print("Data fetched")
        soup = BeautifulSoup(webpage.content, "html.parser")
        
            
        d['Product URL'].append(get_link(soup))
        d['Product Name'].append(get_title(soup))
        d['Product Price'].append(get_price(soup))
        d['Rating'].append(get_rating(soup))
        d['Number of reviews'].append(get_review_count(soup))
      
    else:
        print('url not found' , i)

 
df = pd.DataFrame.from_dict(d)
df.to_csv("amazon_data.csv", header=True, index=False)

# Extracting info from 20 pages
Product_link_list=["https://www.amazon.in/s?k=bags&crid=3D5UAEE4CSMJ6&sprefix=%2Caps%2C2539&ref=nb_sb_noss_2",
                   "https://www.amazon.in/s?k=laptop&crid=3CGX3CNPG0ZTC&sprefix=laptop%2Caps%2C206&ref=nb_sb_noss_1",
                   "https://www.amazon.in/s?k=playstation&crid=WCHVFGZLEBPL&sprefix=playstation%2Caps%2C214&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=mouse&crid=2CSR7ZKM9QVG2&sprefix=mouse%2Caps%2C397&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=keyboard&crid=27KZ0OBUHVRUF&sprefix=keyboard%2Caps%2C398&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=bangles&crid=33MQNG10BMLRV&sprefix=bangles%2Caps%2C354&ref=nb_sb_noss_2",
                   "https://www.amazon.com/s?k=shorts&crid=1GVODBH594FZT&sprefix=shorts%2Caps%2C360&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=shirt&crid=1B1Y5PIGWWUI7&sprefix=shirt%2Caps%2C345&ref=nb_sb_noss_2",
                   "https://www.amazon.com/s?k=jeans&crid=1621TKJL1XF0T&sprefix=jeans%2Caps%2C385&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=earrings&crid=28NOG6UZE6PDF&sprefix=earrings%2Caps%2C353&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=top&crid=8SMK9SBT33HQ&sprefix=top%2Caps%2C407&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=bed&crid=16K6EHKWGT3T0&sprefix=bed%2Caps%2C488&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=sofa&crid=1Q8EGUP3VFFQJ&sprefix=sofa%2Caps%2C456&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=table&crid=1NUDAO5BWAPV0&sprefix=table%2Caps%2C350&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=ball&crid=15TJWVVX0OMJ4&sprefix=ball%2Caps%2C414&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=razor&crid=DIE3R5UBTMG7&sprefix=razor%2Caps%2C353&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=curtains&crid=1M86R87ZJ35ZW&sprefix=curtains%2Caps%2C344&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=bag&crid=3O1SJF0V3HJBF&sprefix=bag%2Caps%2C377&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=lipstick&crid=2NOKUFI2SHQUB&sprefix=lipstick%2Caps%2C357&ref=nb_sb_noss_1",
                   "https://www.amazon.com/s?k=eyeshadow+palette&sprefix=eyeshow%2Caps%2C352&ref=nb_sb_ss_ts-doa-p_1_7"]
                   
                   

for link in Product_link_list:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        new_webpage = requests.get(link, headers=headers)
        for i in range(0,11):
            page = requests.get(link, headers=headers)
            if(page.status_code==200):
                print("Data fetched")
                soup = BeautifulSoup(page.content, "html.parser")
        
            
                d['Product URL'].append( get_link(soup))
                d['Product Name'].append(get_title(soup))
                d['Product Price'].append(get_price(soup))
                d['Rating'].append(get_rating(soup))
                d['Number of reviews'].append(get_review_count(soup))
      
            else:
                print('url not found' , i)
   
df = pd.DataFrame.from_dict(d)

df.to_csv("amazon_data.csv", header=True, index=False)

    