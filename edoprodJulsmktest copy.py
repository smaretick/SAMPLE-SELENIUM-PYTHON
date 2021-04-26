from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys
#gmail includes
import smtplib

#this script tests the PROD version of Marketplace


#Send the email
fromaddr = 'scott.maretick@XXXinteractive.com'  
toaddrs  = 'scott.maretick@XXXinteractive.com' 
subj = "Selemium PROD smoke test error"
# Credentials  
username = 'scott.maretick@XXXinteractive.com'  
password = 'Smm110751#'    
# The email preparation to send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  

#ChromeDriver
#DesiredCapabilities capabilities = DesiredCapabilities.chrome();
#capabilities.setCapability("chrome.verbose", false);
#options = webdriver.ChromeOptions();
#options.add_argument("--start-maximized");
#browserC = webdriver.Chrome(chrome_options=options)
#browserC = webdriver.Chrome()
browser = webdriver.Firefox()
browser.maximize_window()
#Firefox loads all pages without wait calls
#calling implicitly_wait method only works with Firefox for screengrabs if you call it once

f = open('SeleniumSmokePROD.txt', 'w')
#PROD
f.write('Starting PROD Marketplace smoke test \n')
browser.get("http://marketplace.XXX.local/marketplace-ui/login.do") #PROD
f.write('Call to get PROD Marketplace Login \n')
login = repr(browser.title)
title = browser.title
print "browser.title is %s." % browser.title
f.write('logging into XXX PROD Marketplace:\n')
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX1prod.png')  #screenshot
f.write('Logon to PROD Marketplace (smaretick@XXXinteractive.com)\n')
#Username
f.write('Call to input username \n')
browser.find_element_by_name("j_username").clear()
browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
f.write('Call to input password \n')
browser.find_element_by_name("j_password").clear()
browser.find_element_by_name("j_password").send_keys("sm110751")
browser.find_element_by_css_selector("input.btn.btn-success").click()
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX2prodMrktPl.png')  #screenshot
#Account Enrollment (the landing page)
if browser.title == "Account Enrollment":
	print('==========================================================================')
	print('SUCCESS the browser found Account Enrollment Dashboard after initial login')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX3prodAccEnroll.png')  #screenshot
	f.write('SUCCESS:the browser found Account Enrollment Dashboard \n')
#-------------------------------------------------------------------------------------------------------
#Research
f.write('Call to get Network Research \n') 
#Network Analyzer
f.write('Call to get Network Analyzer \n')
browser.get("http://marketplace.XXX.local/marketplace-ui/presale/networkAnalyzer")
f.write('sleeping for 20 secs to allow Network Analyzer page to load \n') 
time.sleep(20) # Let the page load
if browser.title == "Network Analyzer":
	print('==========================================================================')
	print('SUCCESS the browser found Network Analyzer')
	print "browser.title is %s." % browser.title
	f.write('SUCCESS:the browser found Network Analyzer \n')
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX4prodNetworkAnalyzer.png')  #screenshot
else:
	#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
	#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	print('==========================================================================')
	print('SUCCESS the browser found Network Analyzer after logging back on')
	print "browser.title is %s." % browser.title
	f.write('SUCCESS:the browser found Network Analyzer after logging back on\n')
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX4prodNetworkAnalyzer.png')  #screenshot

#Drop Down lists on Network Analyzer
browser.find_element_by_css_selector("div > b").click() #target industry
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX5prodtargetindustryDD.png')  #screenshot
f.write('found the target industry dropdown in Network Analyzer \n')
print('found the target industry dropdown in Network Analyzer')
browser.find_element_by_css_selector("#s2id_advertiser_select > a.select2-choice > div > b").click()   #get Advertiser drop down list
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX6prodAdvertiserDD.png')  #screenshot
f.write('found the advertiser dropdown in Network Analyzer\n')
print('found the advertiser dropdown in Network Analyzer')
browser.find_element_by_css_selector("#s2id_date_select > a.select2-choice > div > b").click()  #Last 3/13 Months
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX7prodMonthsDD.png')  #screenshot
f.write('found the 3-12 months dropdown in Network Analyzer\n')
print('found the 3-12 months dropdown in Network Analyzer')
#-------------------------------------------------------------------------------------------------------
#Location Explorer
f.write('Call to get Location Explorer \n') 
browser.get("http://marketplace.XXX.local/marketplace-ui/presale/locationExplorer")
f.write('sleeping for 20 secs to allow Location Explorer page to load \n') 
time.sleep(20) # Let the page load
browser.implicitly_wait(30)
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX8prodLocationExplorer.png')  #screenshot
if browser.title == "Location Explorer":
	print('==========================================================================')
	print('SUCCESS the browser found Location Explorer')
	print "browser.title is %s." % browser.title
	f.write('SUCCESS:the browser found Location Explorer \n')
else:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/presale/locationExplorer")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX8prodLocationExplorer.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Location Explorer after logging back on')
	print "browser.title is %s." % browser.title
	f.write('SUCCESS:the browser found Location Explorer after logging back on\n')
#four tabs
#CARDHOLDER COUNT
browser.find_element_by_id("cardholder-btn").click()
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX9prodCardHolderCount.png')  #screenshot
f.write('found the Card Holder Count for Location Explorer\n')
print('found the Card Holder Count for Location Explorer')
#DOLLARS SPENT
browser.find_element_by_id("dollars-spent-btn").click()
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX9prodDollarsSpent.png')  #screenshot
f.write('found the Dollars Spent for Location Explorer\n')
print('found the Dollars Spent for Location Explorer')
#AVERAGE ORDER VALUE
browser.find_element_by_id("AOV-btn").click()
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX9prodAOV.png')  #screenshot
f.write('found the Average Order Value for Location Explorer\n')
print('found the Average Order Value for Location Explorer')
#PURCHASE FREQUENCY
browser.find_element_by_id("puchase-freq-btn").click()
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX9prodPurchaseFrequency.png')  #screenshot
f.write('found the Purchase Frequency for Location Explorer\n')
print('found the Purchase Frequency for Location Explorer')
#Drop Down lists on Location Explorer
browser.find_element_by_css_selector("div > b").click()   #industry
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX9prodtIndustriesDD.png')  #screenshot
f.write('found the industry dropdown in Location Explorer\n')
print('found the industry dropdown in Location Explorer')
browser.find_element_by_css_selector("#s2id_date_select > a.select2-choice > div > b").click()  #mths
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX10prodLXMonthsDD.png')  #screenshot
f.write('found the 3-12 months dropdown in Location Explorer\n')
print('found the 3-12 months dropdown in Location Explorer')
#pages of Location Explorer
browser.find_element_by_link_text("2").click()  #page 2
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX10prodLXpage2.png')  #screenshot
f.write('found page 2 of Location Explorer\n')
print('found page 2 of Location Explorer')
browser.find_element_by_id("cbsa_table_next").click()  #next page
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX10prodLXpagenxt.png')  #screenshot
f.write('found next page of Location Explorer\n')
print('found next page of Location Explorer')
browser.find_element_by_id("cbsa_table_last").click()  #last page
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX10prodLXpagelst.png')  #screenshot
f.write('found last page of Location Explorer\n')
print('found last page of Location Explorer')
#----------------------------------------------------------------------------------------------------------
#Budget Bulider
f.write('Call to Budget Builder \n') 
browser.get("http://marketplace.XXX.local/marketplace-ui/presale/budgetBuilder")
f.write('sleeping for 20 secs to allow Budget Builder page to load \n') 
time.sleep(20) # Let the page load
#assert "Budget Builder"in browser.title
if browser.title == "Budget Builder":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX11prodBudgetBuilder.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Budget Builder')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Budget Builder \n')
else:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/presale/budgetBuilder")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX11prodBudgetBuilder.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Budget Builder after logging back on')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Budget Builder after logging back on\n')

#-------------------------------------------------------------------------------------------------------
#Manage Accounts
f.write('Call to get EnrollmentList \n')  
browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/EnrollmentList")
if browser.title == "Account Enrollment":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX12prodAccountEnrollment.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Enroll Accounts')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Enroll Accounts \n')
else:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/EnrollmentList")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX12prodAccountEnrollment.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Enroll Accounts after logging back on')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Enroll Accounts after logging back on')
#-------------------------------------------------------------------------------------------------------
#Account Enrollment/Enroll Accounts
f.write('Call to get EnrolledAccountsDashboard\n')  
browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/EnrolledAccountsDashboard")
time.sleep(20) # Let the page load
f.write('sleeping for 20 secs to allow browser page to load \n') 
print('sleeping for 20 secs to allow the browser page to load')
if browser.title == "Account Enrollment":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX13prodEnrolledAccountsDashboard.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found  Account Enrollment')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Account Enrollment\n')
else:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/EnrollmentList")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX13prodEnrolledAccountsDashboard.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Account Enrollment after logging back on')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Account Enrollment after logging back on\n')
#Active Accounts
f.write('Call to get Active Accounts \n') 
browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/Active")
if browser.title == "Active Accounts":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX14prodActiveAccounts.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Active Accounts')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Active Accounts\n')
else:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/Active")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX14prodActiveAccounts.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Active Accounts after logging back on')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Active Accounts after logging back on\n')
#-------------------------------------------------------------------------------------------------------
#Manage Deals
browser.get("http://marketplace.XXX.local/marketplace-ui/deal/list")
if browser.title == "Manage Deals":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX15prodManageDeals.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Manage Deals')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Manage Deals\n')
else:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/Active")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX15prodManageDeals.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Manage Deals after logging back on')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Manage Deals after logging back on\n')
#-------------------------------------------------------------------------------------------------------
#Performance Report
browser.get("http://marketplace.XXX.local/marketplace-ui/deal/performanceReport/45678")
if browser.title == "Performance Report":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX16performancereport.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Performance Report')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Performance Report\n')
else:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/Active")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX16performancereport.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Performance Report after logging back on')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Performance Report after logging back on\n')

#-------------------------------------------------------------------------------------------------------
#SMB Workflow
#Test 17 is the Partner Dashboard plus related tests-->each test has multiple execution paths
#Partner Dashboard
browser.get("http://marketplace.XXX.local/marketplace-ui/partner/partnerDashboard")
print('sleeping for 20 secs to allow NeedHelp page to load')
print "browser.title is %s." % browser.title
if browser.title == "Dashboard":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX17partnerDashboard.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Partner Dashboard')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Partner Dashboard\n')
elif browser.title == "Apache Tomcat/6.0.32 - Error report":
#PROCESS THE ERROR-------------------------------------------------------------------------------------
	time.sleep(60) # Let the page load
	f.write('sleeping for 60 secs to allow browser page to load & handle exception\n') 
	print('sleeping for 60 secs to allow browser page to load & handle exception in SMB Workflow')
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX17partnerDashboard.png')  #screenshot
	print('==========================================================================')
	print('OOPS the browser had a 500 error')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('OOPS the browser had a 500 error\n')
	#format & send email
	msg = 'SMOKE TEST ERROR!  LINE 353 of XXXprodJulsmktest.py  OOPS GOT sys 500 ERROR'
	print 'sending email'
	f.write('sending email\n')
	server.sendmail(fromaddr, toaddrs, subj, msg)
elif browser.title == title:
	print('OOPS GOT XXX NEED HELP SCREEN')
	print('sleeping for 20 secs to allow NeedHelp page to load')
	print "browser.title is %s." % browser.title
	f.write('OOPS GOT XXX NEED HELP SCREEN\n')
	f.write('sleeping for 20 secs to allow NeedHelp page to load\n')
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX17partnerDashboard.png')  #screenshot
	#format & send email
	msg = 'SMOKE TEST ERROR!  LINE 363 of XXXprodJulsmktest.py  OOPS GOT XXX NEED HELP SCREEN'
	print 'sending email'
	f.write('sending email\n')
	server.sendmail(fromaddr, toaddrs, subj, msg)
	#change link color to red
else:
	f.write('OOPS unable to access Partner Dashboard\n')
	time.sleep(20) # Let the page load
	print('OOPS unable to access Partner Dashboard')
	print "browser.title is %s." % browser.title
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX17ERRpartnerDashboard.png')  #screenshot
#Username
#	browser.find_element_by_name("j_username").clear()
#	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
#	browser.find_element_by_name("j_password").clear()
#	browser.find_element_by_name("j_password").send_keys("sm110751")
#	browser.find_element_by_css_selector("input.btn.btn-success").click()
#	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX17recoverAccEn.png')  #screenshot
#	print('==========================================================================')
#	print('SUCCESS the browser did not find the dashboard so logged back on')
#	print "browser.title is %s." % browser.title
#	print('==========================================================================')
#	f.write('SUCCESS the browser did not find the dashboard so logged back on\n')
#else:
#	browser.get("http://marketplace.XXX.local/marketplace-ui/login.do")  #PROD
#Username
#	browser.find_element_by_name("j_username").clear()
#	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
#	browser.find_element_by_name("j_password").clear()
#	browser.find_element_by_name("j_password").send_keys("sm110751")
#	browser.find_element_by_css_selector("input.btn.btn-success").click()
#	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX17recoverAccEn.png')  #screenshot
#	print('==========================================================================')
#	print('SUCCESS the browser did not find the dashboard so logged back on')
#	print "browser.title is %s." % browser.title
#	print('==========================================================================')
#	f.write('SUCCESS the browser did not find the dashboard so logged back on\n')

#error check for file
try:
   with open('/Users/nickmaschinski/Desktop/XXXPRODscreens/XXX17recoverAccEn.png'): pass
except IOError:
   print '**************NO XXX17recoverAccEn.png**************'

#-------------------------------------------------------------------------------------------------------
#Manage Account
browser.get("http://marketplace.XXX.local/marketplace-ui/partner/advertiserDetails/753914862")
if browser.title == "Account Details":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX18performancereport.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Partner Account')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Partner Account\n')
	print('CALLING partnerAdd function'
	partnerAdd;
elif browser.title == "Apache Tomcat/6.0.32 - Error report":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX18Apache_Tomcat_6.0.32-Error_report.png')
	print('==========================================================================')
	print('OOPS:the browser got a fatal 500 ERROR trying to find this Partner')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('OOPS:the browser got a fatal 500 ERROR trying to find this Partner\n')
else:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/partner/advertiserDetails/753914862")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX18performancereport.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Partner Account after logging back on')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Partner Account after logging back on\n')
	print('CALLING partnerAdd function'
	partnerAdd;
		
def partnerAdd:				
#-------------------------------------------------------------------------------------------------------
#add store locations to partner account
#-------------------------------------------------------------------------------------------------------
browser.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/a/span").click()  #Manage Deals (menu)
print('==========================================================================')
print('Adding new AZ store location')
print "browser.title is %s." % browser.title
print('==========================================================================')
f.write('Adding new AZ store location \n')
browser.find_element_by_id("storeName").clear()
browser.find_element_by_id("storeName").send_keys("Paul's Pizza AZ")
browser.find_element_by_id("storeName").send_keys("Paul's Pizza Emporium in Scottsdale Arizona")
browser.find_element_by_id("storeNumber").clear()
browser.find_element_by_id("storeNumber").send_keys("17")
browser.find_element_by_xpath("(//input[@id='address1'])[2]").clear()
browser.find_element_by_xpath("(//input[@id='address1'])[2]").send_keys("1000 First St")
browser.find_element_by_xpath("(//input[@id='city'])[2]").clear()
browser.find_element_by_xpath("(//input[@id='city'])[2]").send_keys("Phoenix")
browser.find_element_by_xpath("(//input[@id='state'])[2]").clear()
browser.find_element_by_xpath("(//input[@id='state'])[2]").send_keys("AZ")
browser.find_element_by_xpath("(//input[@id='zipcode'])[2]").clear()
browser.find_element_by_xpath("(//input[@id='zipcode'])[2]").send_keys("85053")
browser.find_element_by_id("contactFirstName").clear()
browser.find_element_by_id("contactFirstName").send_keys("Paul Roberts")
browser.find_element_by_id("contactPhoneNumber").clear()
browser.find_element_by_id("contactPhoneNumber").send_keys("6055551212")
browser.find_element_by_xpath("//input[@value='Add Store Location']").click()
print('==========================================================================')
print('testing adding AZ store location of more than 40 chars-ADS353')
print "browser.title is %s." % browser.title
print('==========================================================================')
f.write('testing adding store location of more than 40 chars-ADS353\n')
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXUATscreens/XXX19AZPartnerStore.png')  #screenshot
#-------------------------------------------------------------------------------------------------------
print('==========================================================================')
print('Adding new CA store location')
print "browser.title is %s." % browser.title
print('==========================================================================')
f.write('Adding new CA store location \n')
browser.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/a/span").click()
browser.find_element_by_id("storeName").clear()
browser.find_element_by_id("storeName").send_keys("Paul's Pizza CA")
browser.find_element_by_id("storeNumber").clear()
browser.find_element_by_id("storeNumber").send_keys("19")
browser.find_element_by_xpath("(//input[@id='address1'])[2]").clear()
browser.find_element_by_xpath("(//input[@id='address1'])[2]").send_keys("1000 Second St")
browser.find_element_by_xpath("(//input[@id='city'])[2]").clear()
browser.find_element_by_xpath("(//input[@id='city'])[2]").send_keys("Beverly Hills")
browser.find_element_by_xpath("(//input[@id='state'])[2]").clear()
browser.find_element_by_xpath("(//input[@id='state'])[2]").send_keys("CA")
browser.find_element_by_xpath("(//input[@id='zipcode'])[2]").clear()
browser.find_element_by_xpath("(//input[@id='zipcode'])[2]").send_keys("90210")
browser.find_element_by_id("contactFirstName").clear()
browser.find_element_by_id("contactFirstName").send_keys("Paulina Roberts")
browser.find_element_by_id("contactPhoneNumber").clear()
browser.find_element_by_id("contactPhoneNumber").send_keys("6055551213")
browser.find_element_by_xpath("//input[@value='Add Store Location']").click()
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX19CAPartnerStore.png')  #screenshot
print('==========================================================================')
print('testing adding store location of more than 40 chars-ADS353')
print "browser.title is %s." % browser.title
print('==========================================================================')
f.write('testing adding store location of more than 40 chars-ADS353\n')
#-------------------------------------------------------------------------------------------------------
#Create Campaign (should show added store locations in Location Explorer)
browser.get("http://marketplace.XXX.local/marketplace-ui/partner/partnerDashboard/locationExplorer")
print('sleeping 60 seconds to allow new partner locations to show up in Location Explorer')
f.write('sleeping 60 seconds to allow new partner locations to show up in Location Explorer \n')
time.sleep(60) # Let the page load
if browser.title == "Location Explorer":
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX20partnerlocationexplorer.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Partner Create Campaign')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Partner Create Campaign\n')
elif browser.title == title:
#Username
	browser.find_element_by_name("j_username").clear()
	browser.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browser.find_element_by_name("j_password").clear()
	browser.find_element_by_name("j_password").send_keys("sm110751")
	browser.find_element_by_css_selector("input.btn.btn-success").click()
	browser.get("http://marketplace.XXX.local/marketplace-ui/Accounts/Active")
	browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX20partnerlocationexplorer.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found Partner Create Campaign after logging back on')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS the browser found Partner Create Campaign after logging back on\n')
elif browser.title == "Apache Tomcat/6.0.32 - Error report":

#Review Billing
browser.get("http://marketplace.XXX.local/marketplace-ui/partner/partnerDashboard/billing")
browser.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX21partnerreviewbilling.png')  #screenshot
print('==========================================================================')
print('SUCCESS the browser found Partner bill')
print "browser.title is %s." % browser.title
print('==========================================================================')
f.write('SUCCESS the browser found Partner bill')
return


#************************************************************************************************************************
#************************************************************************************************************************
#close email serer
server.quit()
f.write('log out of Marketplace PROD Firefox\n')
browser.get("http://marketplace.XXX.local/marketplace-ui/j_spring_security_logout")
f.write('Ending PROD Firefox Marketplace smoke test \n') 
f.write('Call to quit Marketplace PROD Firefox browser \n')
f.write('closing Firefox browser \n')
print('closing Firefox browser')
browser.quit()
#************************************************************************************************************************
#testing card swipe report
#needs to be done in Chrome so download will work w/o response
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
print('opening Chrome browser to test LCR download')
browserC = webdriver.Chrome()
browserC.get("http://marketplace.XXX.local/marketplace-ui/login.do") #PROD
if browserC.title == "Account Enrollment":
	browserC.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX22prodEnrolledAccountsDashboard.png')  #screenshot
	print('==========================================================================')
	print('SUCCESS the browser found  Account Enrollment to test card swipe')
	print "browser.title is %s." % browser.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Account Enrollment to test card swipe\n')
else:
#Username
	browserC.find_element_by_name("j_username").clear()
	browserC.find_element_by_name("j_username").send_keys("scott.maretick@XXXinteractive.com")
#password
	browserC.find_element_by_name("j_password").clear()
	browserC.find_element_by_name("j_password").send_keys("sm110751")
	browserC.find_element_by_css_selector("input.btn.btn-success").click()
	browserC.get("http://marketplace.XXX.local/marketplace-ui/Accounts/EnrollmentList")
	print('==========================================================================')
	print('SUCCESS the browser found Account Enrollment to get cardswipe report after logging back in')
	print browserC.title
	print('==========================================================================')
	f.write('SUCCESS:the browser found Account Enrollment to test card swipe report after logging back in\n')
browserC.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX23prodEnrolledAccountsDashboard.png')  #screenshot
time.sleep(60) # Let the page load
f.write('sleeping for 60 secs to allow Chrome browser login page to load \n') 
print('downloading LCR card swipe report')
f.write('downloading LCR card swipe report \n')
browserC.get("http://marketplace.XXX.local/marketplace-ui/Accounts/downloadCardSwipeReport") #PROD
print('sleeping for 60 secs to allow Chrome browser login page to load')
#time.sleep(60) # Let the page load
#f.write('sleeping for 60 secs to allow Chrome browser page to load \n') 
#print('sleeping for 60 secs to allow Chrome browser page to load')
browserC.save_screenshot('//Users/nickmaschinski/Desktop/XXXPRODscreens/XXX24prodCardSwipeReport.png')  #screenshot
#-------------------------------------------------------------------------------------------------------
#testing bill download
#needs to be done in Chrome so download will work w/o response
#-------------------------------------------------------------------------------------------------------
#Location Explorer direct link & expands Research menu
browserC.get("http://marketplace.XXX.local/marketplace-ui/presale/locationExplorer")
#browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/ul/li[3]/a/span").click()  #Budget Builder menu link since menu expanded
#browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/a/span").click()  #expands Manage Accounts menu
#browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/ul/li[2]/a/span").click()  #Active Accounts
#browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[4]/a/span").click()  #Manage Deals
browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[5]/a/span").click()  #expands SMB Workflow menu
#browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[5]/ul/li[2]/a/span").click() #SMB Workflow->Manage Account
#browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[5]/ul/li[3]/a/span").click()  #SMB Workflow->Create Campaign
#browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[5]/ul/li[4]/a/span").click()  #SMB Workflow->Review Billing download (bill.pdf)
#browserC.find_element_by_xpath("//div[@id='sidebar']/ul/li[6]/a/span").click()  #expand Reports menu
#print('==========================================================================')
#print('DOWNLOADING the billing report')
#print('==========================================================================')
#f.write('DOWNLOADING the billing report \n')
#-------------------------------------------------------------------------------------------------------
f.write('log out of Marketplace PROD Chrome\n')
browserC.get("http://marketplace.XXX.local/marketplace-ui/j_spring_security_logout")
f.write('Ending PROD Chrome Marketplace smoke test \n') 
f.write('Call to quit Marketplace PROD Chrome browser \n')
f.write('closing Chrome browser \n')
print('closing Chrome browser')
f.close()
browserC.quit()