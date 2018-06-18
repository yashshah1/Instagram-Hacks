from selenium import webdriver
import time 
import re

#STUFF THATS NEEDS TO BE CHANGED------------ 
USERNAME = "ENTER_YOUR_USERNAME_HERE"
PASSWORD = "ENTER_YOUR_PASSWORD_HERE"
"""
Enter the users you'd like to spam, as a python list below
NOTE: They either need to be public profiles, or you need to be following them
"""
users = ["user_1", "user_2", "user_n"] #Replace user1, user2... with respective usernames
#END STUFF


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')

user_name = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

user_name.send_keys(USERNAME)
password.send_keys(PASSWORD)

login = driver.find_element_by_class_name('_5f5mN')
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

	time.sleep(10)
	while 1:	
		try:
			driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
			try:   
				driver.find_element_by_class_name('coreSpriteHeartOpen').click() 	   
				driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
				time.sleep(2)
			except: 
				try:
					driver.find_element_by_class_name('coreSpriteHeartFull').click()
					driver.find_element_by_class_name('coreSpriteHeartOpen').click() 	   
					driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
					time.sleep(2)
					driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
				except:
					continue 
		except:
			break
	"""Last image"""
	try:
		driver.find_element_by_class_name('coreSpriteHeartOpen').click()
	except:
		driver.find_element_by_class_name('coreSpriteHeartFull').click()
		driver.find_element_by_class_name('coreSpriteHeartOpen').click() 	
