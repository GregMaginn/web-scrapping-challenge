import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

def scraper():
    space_news_url = 'https://redplanetscience.com/'


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(space_news_url)

    html = browser.html


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_="list_text")

    for result in results:
        news_title = result.find('div', class_='content_title').text
        news_p = result.find('div', class_='article_teaser_body').text
        break

    print(news_title)
    print(news_p)

    space_image_url = 'https://spaceimages-mars.com/'

    browser.visit(space_image_url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results2 = soup.find_all('div', class_='header')

    for result in results2:
        mars_img = result.find('img', class_="headerimage fade-in")['src']

    print(mars_img)

    mars_facts_url = 'https://galaxyfacts-mars.com/'

    browser.visit(mars_facts_url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results3 = soup.find_all('table', class_="table table-striped")

    print(results3)

    hemi_url = 'https://marshemispheres.com/'

    browser.visit(hemi_url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemis = browser.find_by_css('a.product-item img')
    print(len(hemis))

    page_urls = []
    all_titles = []
    all_links = []

    #runs through all four of the links
    #runs through each hemi page
    for i, hemi in enumerate(hemis):
        ##print(i, hemi)
        #finds page based on i
        browser.find_by_css('a.product-item img')[i].click()
        
        #stores title of page
        hemi_titles = browser.find_by_css('h2.title').text
        print(hemi_titles)
        
        #stores image
        url = browser.find_by_css('li.href')
        print(url)
        
        #store page info in lists
        all_titles.append(hemi_titles)
        all_links.append(url)
    
        
        #return to previous page
        browser.back()
    
    mars_list_dics = dict(zip(all_titles, all_links))

    mars_scrapped = {'news title': news_title,
                     'news info':news_p,
                     'featured image':mars_img,
                     'html table': results3,
                     'mars hemispheres': mars_list_dics}

    return mars_scrapped


        
