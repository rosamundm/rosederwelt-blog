#first functional test 

from selenium import webdriver

browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver/geckodriver')
browser.get('http://134.209.234.215:8000/')

assert 'Wagtail' in browser.title
