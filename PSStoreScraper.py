from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time





class PSStoreScraper(object):
    
    def __init__(self):
        pass
    
    def scrape_site(self , output_file):
        start = time.time()
        url_base = 'https://store.playstation.com/#!/en-us/all-deals/cid=STORE-MSF77008-ALLDEALS'
        current_page = 1
        wait_for_page = 50
        pagecount = 5
        # Any page after the last page of the playstation store takes you to the last page so any iteration after the last page will  print duplicates. 
        # All the good deals are early on in the page count. The last pages are all garbage.
        #PhantomJs takes twice as long to load as using a more traditional browser so I set the wait time to 50 seconds...with phantomjs it takes about 10 or so , but 
        #it has its slow moments. 
        
        file = open('playstation_deals.txt' , 'w' , encoding = 'utf-8')
        driver = webdriver.PhantomJS()
        for i in range(pagecount):
            print("current page : {} ".format(str(i + 1)))
            url = url_base + "/{page}".format(page = str(current_page))
            driver.get(url)
            #refresh is needed for pages after 1. For some reason deals don't load if I use get and just incremenet page. 
            driver.refresh()
            try:
                WebDriverWait(driver , wait_for_page).until(EC.visibility_of_element_located((By.CLASS_NAME , 'cellBorderCtnr')))
            except TimeoutException as e:
                #print("{iter} Driver Timed Out , Page Didn't load within {seconds} seconds".format(iter =  i , seconds = wait_for_page))
                file.write("Driver Timed Out , Page Didn't load within {}".format(wait_for_page))
                break
            body_source = driver.find_element_by_tag_name('body').get_attribute('outerHTML')
            soup = bs(body_source , 'html.parser')
            for e in soup.find_all('div' , class_ = 'cellBorderCtnr'):
                name = e.find("h3" , class_ = 'cellTitle')
                name_lower = name.string.lower()
                save_percent = e.find('span')
                final_price = e.find('li' , class_="buyPrice")
                output = "{title} - {percent} - {price}".format(title = name_lower , percent = save_percent.string , price = final_price.string)
                ascii_output = output.encode('ascii', 'ignore')
                encoded_output = str(ascii_output , 'utf-8')
                file.write(encoded_output + '\n')
            
            current_page += 1
        driver.quit()
        file.close()
        end = time.time()
        run_time = end - start
        print("run time: {} seconds ".format(int(run_time)))

if __name__ == '__main__':
    ps = PSStoreScraper()
    ps.scrape_site('playstation_deals.txt')
     
         

