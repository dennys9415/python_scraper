#libraries
from bs4 import BeautifulSoup
import requests

#-------------------------------------------------------------------------------------------
#url of the webpage
url="https://luxsecondchance.com/collections/handbags"
#var2=f"https://luxsecondchance.com/collections/handbags?page={n}"

#-------------------------------------------------------------------------------------------
#Beautiful Soup
source=requests.get(url).text
soup=BeautifulSoup(source,'lxml')

#class that contain only the desired content
class_article='product-info'

#function total
#article=soup.find('div', class_=class_article).text
#print (article) #only how the first article                                            #the information of one item

#-------------------------------------------------------------------------------------------
#loop for all pages
#'''
number_pagination=soup.find('div',class_='pagination')
results=[]
for numbery in number_pagination.find_all('span', class_='pagination__number'):
    try:
        numberx=numbery.a.text
    except Exception as e:
        numberx='0'
    results.append(numberx)
#print(results)
result_desired=results[-1]                                                               #the last page of the catalog 
##print(result_desired)                                 
#'''
#-------------------------------------------------------------------------------------------
#loop for all the articles in one page
'''
for article in soup.find_all('div', class_=class_article):                                #class tha have the content of each item
    title_article=article.find('div',class_='vendor').text                                #name of the article
    print (title_article)
    description_article=article.find('div',class_='product-block__title').text            #content of each item   
    print (description_article)
    price_article=article.find('span',class_='money').text                                #price of each item
    print (price_article)
    print ("---------------------------------------------------------------")
'''
#-------------------------------------------------------------------------------------------
#loop to get all the information needed
#'''
for n in range (int(result_desired)):
    page_number=n+1
    var3=url+"?page="+str(page_number)
    #print("this is the page number: "+str(page_number))
    #print("this is the web page: "+var3)
#'''
    source2=requests.get(var3).text
    soup2=BeautifulSoup(source2,'lxml')

    for article in soup2.find_all('div', class_=class_article):                               #class tha have the content of each item
        title_article=article.find('div',class_='vendor').text                                #name of the article
        print (title_article)
        description_article=article.find('div',class_='product-block__title').text            #content of each item   
        print (description_article)
        price_article=article.find('span',class_='money').text                                #price of each item
        print (price_article)

    print ("---------------------------------------------------------------")
#'''
#'''
#-------------------------------------------------------------------------------------------


