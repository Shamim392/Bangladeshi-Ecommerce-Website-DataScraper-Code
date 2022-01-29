def Daraz_Scraper(query):
    #Open File
    file = pd.read_csv('/content/data/daraz-products.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 999999999999
    product_Data = []
    
    #Loop throw file
    for index, row in file.iterrows():
        #check wather query is present or not
        if query in str(row['products-name']):
            try:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
                #initialize chrome web driver
                #driver = webdriver.Chrome(ChromeDriverManager().install())

                #maximize browser
                #driver.maximize_window()

                #scrap site data
                driver.get(row['products-link'])
                driver.implicitly_wait(3)

                #scrap price
                product_price = driver.find_element(By.CLASS_NAME, 'pdp-price').text
                product_price = product_price[2:] #onno site er belay eita baad jabe
                product_price = int(product_price)
                
                # check and set product data for lower priced product
                if(product_price<price):
                    price = product_price
                    product_title = driver.find_element(By.CLASS_NAME, 'pdp-mod-product-badge-title').text
                    product_url = row['products-link']
                    product_image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute("src")

                    product_Data = [product_title, price, product_url, product_image_url]
                    
                #terminate webdriver
                driver.quit()
            except:
                pass
    
    return product_Data


def Banglarshopers_Scraper(query):
    #Open File
    file = pd.read_csv('/content/data/banglashoppers.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 999999999999
    product_Data = []
    
    #Loop throw file
    for index, row in file.iterrows():
        #check wather query is present or not
        if query in str(row['products-name']):
            try:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
                #initialize chrome web driver
                #driver = webdriver.Chrome(ChromeDriverManager().install())

                #maximize browser
                #driver.maximize_window()

                #scrap site data
                driver.get(row['products-link'])
                driver.implicitly_wait(3)

                #scrap price
                product_price = driver.find_element(By.CLASS_NAME, 'price').text
                product_price = product_price[2:] #onno site er belay eita baad jabe
                product_price = int(product_price)
                
                # check and set product data for lower priced product
                if(product_price<price):
                    price = product_price
                    product_title = driver.find_element(By.CLASS_NAME, 'base').text
                    product_url = row['products-link']
                    product_image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute("src")

                    product_Data = [product_title, price, product_url, product_image_url]
                    
                #terminate webdriver
                driver.quit()
            except:
                pass
    
    return product_Data


def Jadroo_Scraper(query):
    #Open File
    file = pd.read_csv('/content/data/jadroo-products.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 999999999999
    product_Data = []
    
    #Loop throw file
    for index, row in file.iterrows():
        #check wather query is present or not
        if query in str(row['products-name']):
            try:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
                #initialize chrome web driver
                #driver = webdriver.Chrome(ChromeDriverManager().install())

                #maximize browser
                #driver.maximize_window()

                #scrap site data
                driver.get(row['products-link'])
                driver.implicitly_wait(3)

                #scrap price
                product_price = driver.find_element(By.CLASS_NAME, 'product-price').text
                product_price = product_price[2:] #onno site er belay eita baad jabe
                product_price = int(product_price)
                
                # check and set product data for lower priced product
                if(product_price<price):
                    price = product_price
                    product_title = driver.find_element(By.CLASS_NAME, 'product-name').text
                    product_url = row['products-link']
                    product_image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute("src")

                    product_Data = [product_title, price, product_url, product_image_url]
                    
                #terminate webdriver
                driver.quit()
            except:
                pass
    
    return product_Data

def Othoba_Scraper(query):
    #Open File
    file = pd.read_csv('/content/data/othoba-products.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 999999999999
    product_Data = []
    
    #Loop throw file
    for index, row in file.iterrows():
      #check wather query is present or not
      if query in str(row['products-name']):
          try:
              chrome_options = webdriver.ChromeOptions()
              chrome_options.add_argument('--headless')
              chrome_options.add_argument('--no-sandbox')
              chrome_options.add_argument('--disable-dev-shm-usage')
              driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
              #initialize chrome web driver
              #driver = webdriver.Chrome(ChromeDriverManager().install())

              #maximize browser
              #driver.maximize_window()

              #scrap site data
              driver.get(row['products-link'])
              driver.implicitly_wait(3)

              #scrap price
              product_price = driver.find_element(By.CLASS_NAME, 'product-price').text
              product_price = product_price[2:] #onno site er belay eita baad jabe
              product_price = int(product_price)
                
              # check and set product data for lower priced product
              if(product_price<price):
                  price = product_price
                  product_title = driver.find_element(By.CLASS_NAME, 'product-name').text
                  product_url = row['products-link']
                  product_image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute("src")

                  product_Data = [product_title, price, product_url, product_image_url]
                    
              #terminate webdriver
              driver.quit()
          except:
              pass
    
    return product_Data

def Pickaboo_Scraper(query):
    #Open File
    file = pd.read_csv('/content/data/pickaboo-products.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 999999999999
    product_Data = []
    
    #Loop throw file
    for index, row in file.iterrows():
      #check wather query is present or not
      if query in str(row['products-name']):
          try:
              chrome_options = webdriver.ChromeOptions()
              chrome_options.add_argument('--headless')
              chrome_options.add_argument('--no-sandbox')
              chrome_options.add_argument('--disable-dev-shm-usage')
              driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
              #initialize chrome web driver
              #driver = webdriver.Chrome(ChromeDriverManager().install())

              #maximize browser
              #driver.maximize_window()

              #scrap site data
              driver.get(row['products-link'])
              driver.implicitly_wait(3)

              #scrap price
              product_price = driver.find_element(By.CLASS_NAME, 'price').text
              product_price = product_price[2:] #onno site er belay eita baad jabe
              product_price = int(product_price)
                
              # check and set product data for lower priced product
              if(product_price<price):
                  price = product_price
                  product_title = driver.find_element(By.CLASS_NAME, 'base').text
                  product_url = row['products-link']
                  product_image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute("src")

                  product_Data = [product_title, price, product_url, product_image_url]
                    
              #terminate webdriver
              driver.quit()
          except:
              pass
    
    return product_Data

def Sindabad_Scraper(query):
    #Open File
    file = pd.read_csv('/content/data/sindabad-products.csv', encoding= 'unicode_escape')

    #Declare Data
    price = 999999999999
    product_Data = []
    
    #Loop throw file
    for index, row in file.iterrows():
      #check wather query is present or not
      if query in str(row['products-name']):
          try:
              chrome_options = webdriver.ChromeOptions()
              chrome_options.add_argument('--headless')
              chrome_options.add_argument('--no-sandbox')
              chrome_options.add_argument('--disable-dev-shm-usage')
              driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
              #initialize chrome web driver
              #driver = webdriver.Chrome(ChromeDriverManager().install())

              #maximize browser
              #driver.maximize_window()

              #scrap site data
                #scrap price
              product_price = driver.find_element(By.CLASS_NAME, 'price').text
              product_price = product_price[2:] #onno site er belay eita baad jabe
              product_price = int(product_price)
                
              # check and set product data for lower priced product
              if(product_price<price):
                  price = product_price
                  product_title = driver.find_element(By.CLASS_NAME, 'base').text
                  product_url = row['products-link']
                  product_image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute("src")

                  product_Data = [product_title, price, product_url, product_image_url]
                    
              #terminate webdriver
              driver.quit()
          except:
              pass
    
    return product_Data

qry = input('Enter Product Name: ')

product_Data_Daraz = Daraz_Scraper(qry)
# product_Data_Banglarshopers = Banglarshopers_Scraper(qry)
product_Data_Jadroo = Jadroo_Scraper(qry)
product_Data_Othoba = Othoba_Scraper(qry)
product_Data_Pickaboo = Pickaboo_Scraper(qry)
product_Data_Sindabad = Sindabad_Scraper(qry)


print(product_Data_Daraz)
# print(product_Data_Banglarshopers)
print(product_Data_Jadroo)
print(product_Data_Othoba)
print(product_Data_Pickaboo)
print(product_Data_Sindabad)