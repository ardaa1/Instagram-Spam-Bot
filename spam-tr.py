from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os

a = (-1)
sifir = (-1)

options =   Options()
options.headless = True
spam = input ("Lütfen spam atmak istediğiniz profilin urlsini buraya yapıştırın: ")
isim = input("Lütfen İnstagram kullanıcı adınızın ve şifresinin yazılı olduğu txt dosaysının konumunu giriniz: ")
drive = input ("Lütfen Firefox driverin yolunu belirtiniz: ")
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
    browser.get("https://www.instagram.com/?hl=tr")
    time.sleep(4)
    browser.find_element_by_xpath("//*[@class='_2hvTZ pexuQ zyHYP']").send_keys(d)
    browser.find_element_by_xpath("//*[@aria-label='Şifre']").send_keys(f)
    time.sleep(2)
    gyap = browser.find_element_by_xpath("//*[@class='                     Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ']")
    gyap.click()
    time.sleep (4)
    browser.get(spam)
    spamtik = browser.find_element_by_xpath("//*[@class='wpO6b ']")
    spamtik.click()
    siyat = browser.find_element_by_xpath('//button[text()="Kullanıcıyı Şikayet Et"]')
    siyat.click()
    time.sleep(1)
    tamspam = browser.find_element_by_xpath("//*[@class='                     Igw0E     IwRSH      eGOV_        vwCYk                                                                                                               ']")
    tamspam.click()
    time.sleep(2)
    kapat = browser.find_element_by_xpath('//button[text()="Kapat"]')
    kapat.click()
    time.sleep(1)
    os.system('clear')
    print (yas,"tane kullanıcı adı ve şifreden",a+1,"tanesi tamamlandı...")
    suraya = ("https://www.instagram.com/"+d+"/?hl=tr")
    browser.get(suraya)
    time.sleep(3)
    cikda = browser.find_element_by_xpath("//*[@class='wpO6b ']")
    cikda.click()
    cikiste = browser.find_element_by_xpath('//button[text()="Çıkış Yap"]')
    cikiste.click()
    time.sleep(2)
    
    if a+1 == say:
        print ("Spam atma işleminiz bitmiştir")
        break
    else:
        pass



