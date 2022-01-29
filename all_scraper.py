from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests 


def scrap_daraz(categorie_name, categorie_link, page_upto):
    #initialize driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #implicit wait
    driver.implicitly_wait(0.5)
    #maximize browser
    driver.maximize_window()
    #declare file name and open file
    filename = './data/daraz-products.csv'
    url = categorie_link
    position_to_replace = categorie_link.find("page=")
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()
        i=1
        while(i<=page_upto):
            driver.implicitly_wait(1)
            print(url)
            driver.get(url)
            driver.implicitly_wait(1)
            items = driver.find_elements(By.CLASS_NAME, 'c3KeDq')
            for item in items:
                field = item.find_element(By.TAG_NAME, 'a')
                products_url = field.get_attribute('href')
                products_name = field.get_attribute('innerHTML')

                data = {}
                data['category'] = categorie_name
                data['products-name'] = products_name
                data['products-link'] = products_url
                print(data)
                w.writerow(data)
            i+=1
            url = url[:position_to_replace+5]+str(i)+url[position_to_replace+6:]
            print(url)
        f.close()


def scrap_jadroo(categorie_name, category_slug, page_upto):
    # declare file name and open file
    filename = './data/jadroo-products.csv'
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()
        i=1
        while(i<=page_upto):
            url = "https://contents.jadroo.com/api/v1/category/products?category_slug={}&sorting=&page={}".format(category_slug,i)
            print("Page No988: ", i, url)
            res = requests.get(url).json()
            for item in res["results"]["products"]["data"]:
                data = {}
                data['category'] = categorie_name
                data['products-name'] = item["name"]
                data['products-link'] = "https://www.jadroo.com/products/"+ item["product_slug"]
                print(data)
                w.writerow(data)
            i+=1
        f.close()


def scrap_pickaboo(categorie_name, categorie_link, page_upto):
    #initialize driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #implicit wait
    driver.implicitly_wait(0.5)
    #maximize browser
    driver.maximize_window()
    # declare file name and open file
    filename = './data/pickaboo-products.csv'
    url = categorie_link
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()
        i=1
        position_to_replace = categorie_link.find("p=")
        while(i<=page_upto):
            driver.implicitly_wait(1)
            print("Page No988: ", i, url)
            driver.get(url)
            driver.implicitly_wait(1)
            items = driver.find_elements(By.CLASS_NAME, 'product-item-link')
            for item in items:
                products_url = item.get_attribute('href')
                products_name = item.get_attribute('innerHTML').strip()

                data = {}
                data['category'] = categorie_name
                data['products-name'] = products_name
                data['products-link'] = products_url
                print(data)
                w.writerow(data)
            i+=1
            url = url[:position_to_replace+2]+str(i)+url[position_to_replace+3:]
            print(url)
        f.close()


def scrap_sindabad(categorie_name, categorie_link, page_upto):
    #initialize driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #implicit wait
    driver.implicitly_wait(0.5)
    #maximize browser
    driver.maximize_window()
    # declare file name and open file
    filename = './data/sindabad-products.csv'
    url = categorie_link
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['category','products-name','products-link'])
        w.writeheader()
        i=1
        position_to_replace = categorie_link.find("p=")
        while(i<=page_upto):
            driver.implicitly_wait(1)
            print("Page No988: ", i, url)
            driver.get(url)
            driver.implicitly_wait(1)
            items = driver.find_elements(By.CLASS_NAME, 'product-item-link')
            for item in items:
                products_url = item.get_attribute('href')
                products_name = item.get_attribute('innerHTML').strip()

                data = {}
                data['category'] = categorie_name
                data['products-name'] = products_name
                data['products-link'] = products_url
                print(data)
                w.writerow(data)
            i+=1
            url = url[:position_to_replace+2]+str(i)+url[position_to_replace+3:]
            print(url)
        f.close()