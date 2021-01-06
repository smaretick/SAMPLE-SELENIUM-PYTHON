# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal MDKicy4nya2192zewKpz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from datetime import datetime
import unittest, time, re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

f = open('SeleniumNATURA.txt', 'w')
#RUNS WITH FIREFOX OR CHROME
#driver = webdriver.Firefox()
driver = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
driver.get("https://www.natera.com/")
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/1COOKIES.png')  #screenshot
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button").click() #AGREE COOKIES
print ("COOKIES ACCEPTED")
f.write('COOKIES ACCEPTED \n')

#================================================================================================
#ONCOLOGY
#1. SIGNATURA RESIDUAL DISEASE TEST
#2. SIGNATURA RESEARCH RESEARCH PIPELINE 
#3. SIGNATURA BLOG
#4. ONOCOLOGY RESOURCE HUB

f.write('Starting NATURA SELENIUM test \n')
driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[1]/a").click() #ONCOLOGY
time.sleep(20)
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/NATERA0.png')  #screenshot
driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[1]/ul/li[2]/a").click() #SIGNATURA RESIDUAL
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/1SIGNATURA_RESIDUAL_DT.png')  #screenshot
driver.back()
print ("SIGNATURA RESIDUAL")
f.write('SIGNATURA RESIDUAL \n')

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[1]/a").click() #ONCOLOGY
time.sleep(20)
driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[1]/ul/li[2]/a").click() #2 SIGNATURA RESEARCH RP
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/2SIGNATURA_RESEARCH_RP.png')  #screenshot
driver.back()
print ("SIGNATURA RESEARCH")
f.write('SIGNATURA RESEARCH \n')

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[1]/a").click() #ONCOLOGY
time.sleep(20)
driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[1]/ul/li[3]/a").click() #3 SIGNATURA BLOG 
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/3SIGNATURA_BLOG.png')  #screenshot
#driver.get("https://www.natera.com/") #HOME
print ("SIGNATURA BLOG")
f.write('SIGNATURA BLOG \n')

driver.get("https://www.natera.com/") #HOME
driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[1]/a").click() #ONCOLOGY
time.sleep(20)
driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[1]/ul/li[4]/a").click() #4 ONOCOLOGY RESOURCE HUB
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/4ONOCOLOGY_RESOURCE_HUB.png')  #screenshot
#driver.get("https://www.natera.com/") #HOME
print ("ONOCOLOGY RESOURCE HUB")
f.write('ONOCOLOGY RESOURCE HUB \n')
# /html/body/header/div/nav/div[2]/ul/li[1]/ul/li[4]/a
#================================================================================================
#5.ORGAN HEALTH
#6.PROSPERA TRANSPLANT ASSESSMENT
#7.RENASIGHT KIDNEY HEALTH

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[2]/a").click()  #ORGAN HEALTH
time.sleep(20)
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/5ORGAN_HEALTH.png')  #screenshot
print ("ORGAN HEALTH")
f.write('ORGAN HEALTH \n')
#driver.get("https://www.natera.com/") #HOME

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[2]/a").click()  #ORGAN HEALTH
time.sleep(20)
driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[2]/a").click()  #PROSPERA TRANSPLANT ASSESSMENT
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/6PROSPERA_TRANSPLANT_ASSESSMENT.png')  #screenshot
print ("PROSPERA TRANSPLANT ASSESSMENT")
f.write('PROSPERA TRANSPLANT ASSESSMENT \n')
#driver.get("https://www.natera.com/") #HOME

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[2]/a").click()  #ORGAN HEALTH
time.sleep(20)
driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[2]/ul/li[2]/a").click()  #RENASIGHT KIDNEY HEALTH
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/7RENASIGHT_KIDNEY_HEALTH.png')  #screenshot
print ("RENASIGHT KIDNEY HEALTH")
f.write('RENASIGHT KIDNEY HEALTH \n')
#driver.get("https://www.natera.com/") #HOME

#================================================================================================
#WOMEN'S HEALTH
#1.HORIZON ADVANCED CARRIER SCREENING
#2.PANORAMA NIPT
#3.EMPOWER HEREDITARY CANCER TEST
#4.VISTARA SINGLE-GENE NIPT
#5.ANORA MISCARRIAGE TEST
#6.SPECTRUM PREIMPLANTATION GENETICS
#7.COVID-19 RESOURCES
#8.PRICING & BILLING
#9.WEBINARS
#10.NATERA ACADEMY

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[3]/a").click()  #WOMENS HEALTH
time.sleep(20)NATERA
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/8WOMENSHEALTH.png')  #screenshot
print ("WOMENS HEALTH")
f.write('WOMENS HEALTH \n')


#================================================================================================
#NATERACORE
#1.ONCOLOGY CORE ( /html/body/header/div/nav/div[2]/ul/li[4]/ul/li[1]/a )
#2.ORGAN HEALTH CORE ( /html/body/header/div/nav/div[2]/ul/li[4]/ul/li[2]/a)
#3.WOMEN'S HEALTH CORE /html/body/header/div/nav/div[2]/ul/li[4]/ul/li[3]/a)

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[4]/a").click()  #NATERACORE
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/9NATERACORE.png')  #screenshot
print ("NATERACORE")
f.write('NATERACORE \n')


#================================================================================================
#ABOUT US
#1.OUR STORY ( /html/body/header/div/nav/div[2]/ul/li[5]/ul/li[1]/a )
#2.OUR PEOPLE ( /html/body/header/div/nav/div[2]/ul/li[5]/ul/li[2]/a )
#3.OUR TECHNOLOGY (/html/body/header/div/nav/div[2]/ul/li[5]/ul/li[3]/a )
#4.INVESTOR RELATIONS (/html/body/header/div/nav/div[2]/ul/li[5]/ul/li[4]/a)
#5.MEDIA (/html/body/header/div/nav/div[2]/ul/li[5]/ul/li[5]/a )
#6.CAREERS ( /html/body/header/div/nav/div[2]/ul/li[5]/ul/li[6]/a)
#7.CONTACT US (/html/body/header/div/nav/div[2]/ul/li[5]/ul/li[7]/a)

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[5]/span").click()  #ABOUT US
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/10ABOUTUS.png')  #screenshot
print ("ABOUT US")
f.write('ABOUT US \n')


#================================================================================================
#PORTAL 

driver.find_element_by_xpath("/html/body/header/div/nav/div[2]/ul/li[6]/a").click()  #PORTAL
driver.save_screenshot('//Users/scottmaretick/Desktop/NATERA_SCREEN/11PORTAL.png')  #screenshot
print ("PORTAL")
f.write('PORTAL \n')

#date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#print("end date and time:",date_time)	
#elapsed_time = end - start
#print ("elapsed times", elapsed_time)
f.close()
driver.quit()
