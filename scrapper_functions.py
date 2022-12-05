#libraries
from bs4 import BeautifulSoup
import requests

#-------------------------------------------------------------------------------------------
#url of the webpage
url="https://luxsecondchance.com/collections/handbags"
#url="https://luxsecondchance.com/collections/accessories"
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
#Function to get the number of the pages
#'''
def get_number_of_page():
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
    #print(result_desired)   
    return(result_desired)                        
#'''
#-------------------------------------------------------------------------------------------
#FUNCTION SEGMENTED
#'''
#Function will show the specific name item
def show_name_item(n):
    article=soup.find_all('div', class_=class_article)[n]   
    title_article=article.find('div',class_='vendor').text 
    #print(title_article)
    return(title_article)

#function will show the specific description
def show_description_item(n):
    article=soup.find_all('div', class_=class_article)[n]   
    description_article=article.find('div',class_='product-block__title').text  
    #print(description_article)
    return(description_article)  

#function will show the specific price
def show_price_item(n):
    article=soup.find_all('div', class_=class_article)[n]    
    price_article=article.find('span',class_='money').text
    #print(price_article)
    return(price_article)   

#-------------------------------------------------------------------------------------------
#MAIN FUNCTION
#(BOTH ARE THE SAME)
#Function will show all item in the one page
def show_first_page():
    count=0
    for article in soup.find_all('div', class_=class_article):  
        item=show_name_item(count)                                      #function for name of item
        description=show_description_item(count)                        #function for description of item
        price=show_price_item(count)                                    #function for price of item
        count=count+1
        print("item number: ",count)
        print(item)
        print(description)
        print(price)
        print("-----------------------")
    print("the total number is",count)
        #show_one_name_item(count)

#Function to show all of one page without another functions
def show_one_page():
    #number_per_page=[]
    count=0
    for article in soup.find_all('div', class_=class_article):                                #class tha have the content of each item
        title_article=article.find('div',class_='vendor').text                                #name of the article
        print (title_article)
        description_article=article.find('div',class_='product-block__title').text            #content of each item   
        print (description_article)
        price_article=article.find('span',class_='money').text                                #price of each item
        print (price_article)
        count=count+1
        print("this is the item number: ",count)
        #number_per_page.append(count)
        print ("---------------------------------------------------------------")
    print("the same I expect :",count)
    #print("this is the total of item in the page: ",number_per_page[-1])
#'''
#-------------------------------------------------------------------------------------------
#Function to show all  with the other functions
#'''
def show_all_webpage():
    count=0
    number_per_page=[]
    result_desired=get_number_of_page()
    for n in range (int(result_desired)):
        page_number=n+1
        var3=url+"?page="+str(page_number)
        print("this is the page number: "+str(page_number))
        print("this is the web page: "+var3)

        source2=requests.get(var3).text
        soup2=BeautifulSoup(source2,'lxml')
        program_count=0
        number_per_content=[]


        for article in soup2.find_all('div', class_=class_article):  
            item=show_name_item(program_count)                                      #function for name of item
            description=show_description_item(program_count)                        #function for description of item
            price=show_price_item(program_count)                                    #function for price of item
            count=count+1
            program_count=program_count+1
            print("item number: ",count)
            print(item)
            print(description)
            print(price)
            number_per_content.append(program_count)
            number_per_page.append(count)
            print("-----------------------")
        print ("---------------------------------------------------------------")
        print("this is the total of item in this collection: ",number_per_page[-1])
        print("this is the total of item in the page: ",number_per_content[-1])
        print ("---------------------------------------------------------------")
    print("this is the total of total: ",number_per_page[-1])
    print ("---------------------------------------------------------------")
#'''

#Function to show all  without another functions
#'''
def All_webpage():
    count=0
    number_per_page=[]
    result_desired=get_number_of_page()
    for n in range (int(result_desired)):
        page_number=n+1
        var3=url+"?page="+str(page_number)
        print("this is the page number: "+str(page_number))
        print("this is the web page: "+var3)

        source2=requests.get(var3).text
        soup2=BeautifulSoup(source2,'lxml')
        program_count=0
        number_per_content=[]

        for article in soup2.find_all('div', class_=class_article):                               #class tha have the content of each item
            title_article=article.find('div',class_='vendor').text                                #name of the article
            print (title_article)
            description_article=article.find('div',class_='product-block__title').text            #content of each item   
            print (description_article)
            price_article=article.find('span',class_='money').text                                #price of each item
            print (price_article)
            count=count+1
            program_count=program_count+1
            print("this is the item number: ",count)
            number_per_content.append(program_count)
            number_per_page.append(count)
        print ("---------------------------------------------------------------")
        print("this is the total of item in this collection: ",number_per_page[-1])
        print("this is the total of item in the page: ",number_per_content[-1])
        print ("---------------------------------------------------------------")
    print("this is the total of total: ",number_per_page[-1])
    print ("---------------------------------------------------------------")
#'''

#-------------------------------------------------------------------------------------------
#TESTING ZONE

#testing for show the number of pages
varx=get_number_of_page()
#print (varx)


#testing for show only the first page
#show_first_page()
#show_one_page()


#testing for show all pages
#All_webpage()
#show_all_webpage()