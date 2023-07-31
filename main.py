from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_drive_path = "/Users/ramazanyildiz/development/chromedriver-mac-arm64"
ser = Service(chrome_drive_path)
driver = webdriver.Chrome(service=ser)

driver.get("https://www.python.org/")

#getting the names of events
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")


#getting the dates of events
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

#collecting and matching event names and dates in a dict
dict_event_date = {}

for n in range(len(event_times)):
    dict_event_date[n] = {"name": event_names[n].text, "time": event_times[n].text}

print(dict_event_date)

