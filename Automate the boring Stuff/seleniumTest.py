from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r'C:\\Users\\apnat\\Downloads\\geckodriver.exe')
browser = webdriver.Firefox(service=service)
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(2) > a:nth-child(1)')
elem.click()

elems = browser.find_elements_by_css_selector('p')
print(len(elems))

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()

browser.back()
browser.forward()
browser.refresh()
browser.quit()
