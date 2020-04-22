from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import datetime

import arrow
import re
import requests

def main():
	try:	
		print ('Starting the login script at ' + str(arrow.now().format('YYYY-MM-DD HH:mm:ss')))
		
		# Initiate browser options, browser, and load search results page	
		chrome_options = Options()
		chrome_options.headless = True
		chrome_options.add_argument("--window-size=1920x1080")
		
		browser = webdriver.Chrome(options = chrome_options)
		browser.delete_all_cookies()
		
		print ('Navigating to the test page...')
		browser.get('http://www.pprune.org/rumours-news-13/')
	
		# Find and filter first set of links 
		print ('Finding log-in button')
		try:
			login_button = browser.find_element_by_xpath('//input[@type="submit" and @ value="Agree and Connect"]')
			print ('We are at the captive portal. Clicking the log-in button.')
			login_button.click()
		except:
			print ('We appear to be connected to the internet')
			#!# Add test to check if it really PPRUNE

	finally:		
		# Quit selenium browser
		browser.delete_all_cookies()
		browser.close()
		browser.quit()


main()

	
	
	
