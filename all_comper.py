from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd
from texttable import Texttable




def Daraz_Scraper(query):
    #Open File
    file = pd.read_csv('data/daraz-products.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 999999999999
    product_Data = ["https://www.daraz.com.bd", 'None', 'None', 'None', 'None']
    
    #Loop throw file
    for index, row in file.iterrows():
        # print(str(row['products-name']).lower())
        #check wather query is present or not
        # print(query.lower())
        if query.lower() in str(row['products-name']).lower():
            # print(query.lower(), str(row['products-name']).lower())
            try:
                # chrome_options = Options()
                # chrome_options.add_argument('--headless')
                # chrome_options.add_argument('--no-sandbox')
                # chrome_options.add_argument('--disable-dev-shm-usage')
                # driver = webdriver.Chrome('chromedriver',options=chrome_options)
                driver = webdriver.Chrome(ChromeDriverManager().install())
                #initialize chrome web driver
                #driver = webdriver.Chrome(ChromeDriverManager().install())

                #maximize browser
                #driver.maximize_window()
                # print(row['products-link'])
                #scrap site data
                driver.get(row['products-link'])
                driver.implicitly_wait(3)

                #scrap price
                product_price = driver.find_element(By.CLASS_NAME, 'pdp-price').text
                product_price = product_price[2:] #onno site er belay eita baad jabe
                product_price = int(product_price)

                print("product price: ", product_price)
                
                # check and set product data for lower priced product
                if(product_price<price):
                    price = product_price
                    product_title = driver.find_element(By.CLASS_NAME, 'pdp-mod-product-badge-title').text
                    product_url = row['products-link']
                    product_image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute("src")

                    product_Data = ["https://www.daraz.com.bd", product_title, price, product_url, product_image_url]
                    
                #terminate webdriver
                driver.quit()
            except:
                pass
    
    return product_Data



query = "realme C11"

print(Daraz_Scraper(query))