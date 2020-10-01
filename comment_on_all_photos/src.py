from selenium import webdriver
import time 
import re
from random import randint
from selenium.webdriver.common.keys import Keys
#STUFF THATS NEEDS TO BE CHANGED------------ 
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
"""
Enter the users you'd like to spam, as a python list below
NOTE: They either need to be public profiles, or you need to be following them
"""
users = ["user_1", "user_2", "user_n"] #Replace user1, user2... with respective usernames
text = ["AMAZIN", "<3 <3 <3 <3", "NIICE", "WOW SO C00OL!!!!", "AWSUM STUFF M8"] #Put in as many as you want!
#END STUFF

length_of_text = len(text)

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)
user_name = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

user_name.send_keys(USERNAME)
password.send_keys(PASSWORD)

login = driver.find_element_by_class_name('L3NKy')
login.click() #gets logged in


insta_link = 'https://www.instagram.com/' #Base URL

for i in users:
	time.sleep(5)
	try:
		driver.get(insta_link + i) #Redirect to the suer
		first_image = driver.find_element_by_class_name('_bz0w')
	except:
		continue
	first_image.click() #open first image

	time.sleep(5)
	while 1:	
		try:
			driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
			try:
				text_to_be_sent = text[randint(0, length_of_text - 1)]
				driver.find_element_by_class_name("Ypffh").send_keys(text_to_be_sent)
				driver.find_element_by_class_name("Ypffh").send_keys(Keys.ENTER)
				time.sleep(3)
				driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
				time.sleep(1)
			except: 
				continue
		except:
			break
