from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from all_scraper import *

categorie_name = "Smartphones"
categorie_link= "https://www.daraz.com.bd/smartphones/?page=1&spm=a2a0e.home.cate_1.1.735212f75wrDcs"
page_upto = 2
scrap_daraz(categorie_name, categorie_link, page_upto)


# categorie_name = "home-garden"
# category_slug= "home-garden"
# page_upto = 5
# scrap_jadroo(categorie_name, category_slug, page_upto)


# categorie_name = "Smartphone"
# categorie_link= "https://www.pickaboo.com/smartphone.html?p=1"
# page_upto = 5
# scrap_pickaboo(categorie_name, categorie_link, page_upto)



# categorie_name = "Desktop-laptops"
# categorie_link= "https://sindabad.com/computer-it/desktop-laptops.html?p=1"
# page_upto = 2
# scrap_sindabad(categorie_name, categorie_link, page_upto)
