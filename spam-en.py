from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os

a = (-1)
sifir = (-1)

options =   Options()
options.headless = True
spam = input ("Please paste the url of the profile you want to spam here: ")
isim = input("Please enter the .txt query with the Instagram username and password file: ")
drive = input ("Please specify the path to the Firefox driver: ")
driver_path = drive
browser = webdriver.Firefox(options=options)

while True:
    arda = open(isim,"r")
    bro = arda.readlines ()
    a = a+1
    b =(bro[a])
    c = b.find(" ")
    d = (b[:c])
    e = (b[c:])
    f = (e[1:])
    say = len(bro)
    yas = len(bro)
    cıkra = say-1
    browser.get("https://www.instagram.com/")
    time.sleep(4)
    browser.find_element_by_xpath("//*[@class='_2hvTZ pexuQ zyHYP']").send_keys(d)
    browser.find_element_by_xpath("//*[@aria-label='Password']").send_keys(f)
    time.sleep(2)
    gyap = browser.find_element_by_xpath("//*[@class='                     Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ']")
    gyap.click()
    time.sleep (4)
    browser.get(spam)
    spamtik = browser.find_element_by_xpath("//*[@class='wpO6b ']")
    spamtik.click()
    siyat = browser.find_element_by_xpath('//button[text()="Report User"]')
    siyat.click()
    time.sleep(1)
    tamspam = browser.find_element_by_xpath("//*[@class='                     Igw0E     IwRSH      eGOV_        vwCYk                                                                                                               ']")
    tamspam.click()
    time.sleep(2)
    kapat = browser.find_element_by_xpath('//button[text()="Close"]')
    kapat.click()
    time.sleep(1)
    os.system('clear')
    print (a+1,"out of",yas,"usernames and passwords have been completed...")
    suraya = ("https://www.instagram.com/"+d+"/")
    browser.get(suraya)
    time.sleep(3)
    cikda = browser.find_element_by_xpath("//*[@class='wpO6b ']")
    cikda.click()
    cikiste = browser.find_element_by_xpath('//button[text()="Log Out"]')
    cikiste.click()
    time.sleep(2)
    
    if a+1 == say:
        print ("your spamming process is finished")
        break
    else:
        pass



