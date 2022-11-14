from selenium import webdriver

browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

browser.get('http://www.yahoo.com')

browser.quit()