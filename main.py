from selenium import webdriver

start = "https://cab.brown.edu/"
browser = webdriver.Firefox()
browser.get(start)
browser.close()
