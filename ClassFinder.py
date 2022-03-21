import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#asking the user for class number and modifying link
classNumber = input("Enter Class Number: ")
url = "https://webapp4.asu.edu/catalog/classlist?t=2227&k=" + classNumber + "&hon=F&promod=F&e=open&page=1"

#setting the location of chrome application on local device
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

#sets path of chromedriver and initializes driver as the Chrome webdriver variable
PATH = "C:\\Users\\ibmou\\OneDrive\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chromeOptions)

#accessing the site
driver.get(url)

#executes the javascript code on the site and sets the resulting html into variable src
src = driver.execute_script("return document.body.innerHTML;")

#creates the src html into a BeautifulSoup object so that we can use BS methods
soup = BeautifulSoup(src,"lxml")

#finds the number of available seats for the inputted class and sets that to variable availableSeats
content = soup.find("td", class_="availableSeatsColumnValue")
availableSeats = content.find("span").get_text()


print(availableSeats)
