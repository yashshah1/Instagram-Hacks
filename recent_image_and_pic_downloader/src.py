# import selenium,time & requests modules
import time

import requests

from selenium import webdriver

# launch Chrome and navigate to Instagram page
driver = webdriver.Chrome()
#enter the account username that you want to get posts of: (open accounts only)"
account_name = ""
driver.get("https://www.instagram.com/" + account_name)

# scroll to the bottom of the page
lenOfPage = driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while match == False:
    lastCount = lenOfPage
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(6)
    if lastCount == lenOfPage:
        match = True

# find all links on the page and if they match '/p' append to list named posts
posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)

# print(posts)
print("total posts that will be downloaded are: ", len(posts))
download_url = ''
count = 0
for post in posts:
    count += 1
    driver.get(post)
    shortcode = driver.current_url.split("/")[-2]
    type = driver.find_element_by_xpath('//meta[@property="og:type"]').get_attribute('content')
    if type == 'video':
        download_url = driver.find_element_by_xpath("//meta[@property='og:video']").get_attribute('content')
        video_data = requests.get(download_url).content
        with open('video'+str(count) + '.mp4', 'wb') as handler:
            handler.write(video_data)
    else:
        download_url = driver.find_element_by_xpath("//meta[@property='og:image']").get_attribute('content')
        img_data = requests.get(download_url).content
        with open(str(count) + '.jpg', 'wb') as handler:
            handler.write(img_data)
    time.sleep(6)

print("Done downloaded", count, "files")
driver.close()
