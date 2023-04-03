import time
import hashlib
from urllib.request import urlopen, Request
from time import sleep
from selenium import webdriver
import datetime
import pandas as pd



# read the list of URLs from a file
with open(r'C:\Users\roysh\OneDrive\Desktop\MyWeb\ss.py\Urls.txt' , 'r') as f:
     urls = f.readlines()
    
# remove whitespace and newlines
urls = [url.strip() for url in urls]



def banner():
    print("\t..............................................--------------------------------------------------------------------........")
    print ("Welcome to Shot-Hunter")
    cs_banner = """
        
           ░██████╗██╗░░██╗░█████╗░████████╗░░░░░░██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
           ██╔════╝██║░░██║██╔══██╗╚══██╔══╝░░░░░░██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
           ╚█████╗░███████║██║░░██║░░░██║░░░█████╗███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
           ░╚═══██╗██╔══██║██║░░██║░░░██║░░░╚════╝██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
           ██████╔╝██║░░██║╚█████╔╝░░░██║░░░░░░░░░██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
           ╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝                 


                                            -@4w4r4         
        
        
    "This script will track changes on the URL and if there are any new post or changes it will take screenshot."
	   	 Authored by: @4w4r44                               

    """
    print(cs_banner)
    print("\-----------------------------S_H------------------------------------")

banner()

def capture(url):
    driver = webdriver.Chrome(executable_path=r"C:\Users\roysh\OneDrive\Desktop\ss.py\chromedriver.exe") #add the path of your chromium headless browser. 
    driver.get(url)

    #Giving the file name of screenshot
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "").replace(":", "").replace("-", "_")
    file_name = date_stamp + ".png"
    driver.save_screenshot(r"C:\Users\roysh\OneDrive\Desktop\newshot/"+file_name)

    driver.close() #closing the headless browser.

while True:
    for i,url in enumerate(urls):
        try:
            # set the URL you want to monitor
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

            # perform the get request and store it in a var
            response = urlopen(req).read()

            # to create the initial hash
            currentHash = hashlib.sha224(response).hexdigest()
            print( "Monitoring: " + url)
            time.sleep(4)
            while True:
                # perform the get request
                response = urlopen(req).read()

                # create a new hash
                newHash = hashlib.sha224(response).hexdigest()

                # check if new hash is same as the previous hash
                if newHash == currentHash:
                    # wait for 5 seconds
                    time.sleep(5)
                    continue

                # if something changed in the hashes
                else:
                    # notify
                    print("Something changed on " + url)

                    # take a screenshot
                    capture(url)
                    print("Screenshot taken")

                    # update the hash
                    currentHash = newHash

                    # wait for 30 seconds
                    time.sleep(20)
                    continue

        # To handle exceptions
        except Exception as e:
            print("Error monitoring " + url + ": " + str(e))





#for i, url in enumerate(urls):
   # driver = webdriver.Chrome()
    # Load the URL in the browser
   # driver.get(url)