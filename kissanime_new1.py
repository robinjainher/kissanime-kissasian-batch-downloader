from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
import os
import pprint

options = Options()
options.headless = True
#driver = webdriver.Firefox(options=options, executable_path=r'C:\Utility\BrowserDrivers\geckodriver.exe')

browser = webdriver.Firefox(options=options,executable_path='geckodriver.exe')
#browser = webdriver.Chrome();
#browser.maximize_window()

#addonpath = "C:\\Users\\Robin\\AppData\\Local\\Programs\\Python\\Python37\\firefox@ghostery.com.xpi"
#addonpath = "C:\\Users\\Robin\\Desktop\\ghostery-chrome-v8.2.6.crx"
addonpath = os.getcwd()+"\\firefox@ghostery.com.xpi"
browser.install_addon(addonpath,temporary=True)

#URL = 'https://kissanime.ru/Anime/Sword-Art-Online-Alicization'

if os.path.isfile('user.txt'):
    file = open('user.txt','r')
    user = file.readline()
    passw= file.readline()
    file.close()
else:
    user = input("Enter your Username : ")
    passw= input("Enter your Password : ")
    file = open('user.txt','w')
    file.write(user+'\n'+passw)
    file.close()
#user = 'rjav333'
#passw= 'rjav333@130'

timeout = 20

print('Logging In')

browser.get('https://kissanime.ru/Login')
#sleep(10)
element_present = EC.presence_of_element_located((By.ID,'username'))
WebDriverWait(browser, timeout).until(element_present)

browser.find_element_by_id('username').send_keys(user)
browser.find_element_by_id('password').send_keys(passw)
browser.find_element_by_id('btnSubmit').click()

URL = input("Enter URL of anime : ")
name = URL.split('/')[-1]

try:
    browser.get(URL)
except:
    print("Error : URL not working\nEnter correct URL")
    URL = input("Enter URL of anime : ")
    name = URL.split('/')[-1]

    

la = browser.find_elements_by_tag_name('td > a')
la.reverse()
lin = []
list_a = []
list_n = []


for elem in la:
    #abc = elem.find_element_by_tag_name('a')
    #lin.append(abc.get_attribute('href'))
    try:
        lin.append(elem.get_attribute('href')+'&s=rapidvideo')
        list_n.append(elem.text)
    except:
        print(elem.text)

start = 0
end = len(lin)

pprint.pprint(list_n)
start = int(input('Enter Start (From 1 to '+str((len(lin)))+' ) : ')) - 1
end = int(input('Enter End (From 1 to '+str((len(lin)))+' ) : ')) 

file = open(name+'_RP.txt','w')

try:
    for i in range(end-start):
        print("Downloading " + list_n[i+start])
        browser.get(lin[i+start])
        try:
            #element_present = EC.presence_of_element_located((By.ID,'divDownload'))
            #WebDriverWait(browser, timeout).until(element_present)
            href = browser.find_element_by_id('divDownload')
            href = href.find_element_by_tag_name('a')
            list_a.append(href.get_attribute('href'))
            print(list_a[i])
        except:
            print("Error Not Found : "+url.split('/')[-1].split('?')[0])
except:
    print("Error : Unexpectedly Closed")
finally:
    str1 = '\n'.join(list_a)
    file.write(str1)
    file.close()
    print("RapidVideo Links Saved in "+name+"_RP.txt File ")
    print("Now Use RP_Downloader.py to create txt file of live links")
input("press any key to exit")        




    
