from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
option.set_preference('intl.accept_languages', 'en-GB')
option.set_preference('general.useragent.override', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')
option.add_argument('-headless')






browser = webdriver.Firefox(options=option)
browser.get("https://zoom.us/signin#/login")


xpathlogin = '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div[1]/div/div/input'
browser.find_element(By.XPATH, xpathlogin).send_keys('videomost1@pulse.insure')

xpathpassword = '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div[2]/div/div/input'
browser.find_element(By.XPATH, xpathpassword).send_keys('Pulse321')




xpathloginbutton = '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div[4]/button/span'
browser.find_element(By.XPATH, xpathloginbutton).click()

time.sleep(5)


#Free recording space
browser.get("https://us06web.zoom.us/account/metrics/dashboard")
time.sleep(5)
recspacexpath = '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[7]/label[1]'
recspace = browser.find_element(By.XPATH, recspacexpath)
recspacetxt = recspace.text
print(recspacetxt)


#Number of conference this week
browser.get("https://zoom.us/account/metrics/pastmeetings")
time.sleep(10)
confnumxpath = '/html/body/div[1]/div[2]/div[2]/div[4]/div/div[1]/div[1]/div/div[1]/span[1]'
confnum = browser.find_element(By.XPATH, confnumxpath)
confnumtxt = confnum.text
print(confnumtxt)
time.sleep(1)

#Licensing
browser.get("https://us06web.zoom.us/billing/plan")
time.sleep(1)
licnumxpath = '/html/body/div[1]/div[4]/div[4]/div[3]/div/div/div[2]/div[4]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]'
licnum = browser.find_element(By.XPATH, licnumxpath)
licnumtxt = licnum.text
print(licnumtxt)

licdatexpath = '/html/body/div[1]/div[4]/div[4]/div[3]/div/div/div[2]/div[4]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[7]/div[1]'
licdate = browser.find_element(By.XPATH, licdatexpath)
licdatetxt = licdate.text


browser.close()
browser.quit()


d1 = datetime.datetime.today()
d2 = datetime.datetime(2023, 10, 26, 0, 0)

#print((d2-d1).days)

licenddate = ((d2-d1).days)
licenddatestr = str(licenddate)
print(licenddatestr)

try:
 with open("zoom.txt", "w+") as file:
     file.write(recspacetxt)
     file.write('\n')
     file.write(licenddatestr)
     file.write('\n')
     file.write(confnumtxt)
     file.write('\n')
     file.write(licnumtxt)
     file.close()
except:
   print ("Error")    #comment
   