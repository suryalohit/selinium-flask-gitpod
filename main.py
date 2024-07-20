from seleniumwire import webdriver
import datetime
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
TOKEN = "6994416717:AAH_qEF1vSy1gZc1nXQ4eyM4dErJshFGJaM"
chat_id = "998041732"



chrome_options = Options()
# Important Arguments won't eun without them in Gitpod
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--headless")  

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.set_window_size(2020, 980)
driver.get("https://x.com/i/flow/login")

time.sleep(5)
driver.save_screenshot("loginpage.png")
print(driver.get_window_size())
print("1")
username = driver.find_element("name", "text")
username.click()
username.send_keys('devikagoud245@gmail.com')
driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
time.sleep(3)
try:
    print("2")
    driver.save_screenshot("2ndstep.png")
    check = driver.find_element("name", "text")
    check.click()
    check.send_keys('retiredHippo')
    driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()
    time.sleep(3)

except:
    print("except")

print("3")
driver.save_screenshot("3rdstep.png")
driver.save_screenshot("mon3.png")
password = driver.find_element("name", "password")
password.click()
password.send_keys('Asailohit30@')
driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').click()
time.sleep(4)
driver.get("https://x.com/")

time.sleep(5)
driver.save_screenshot("afterlogin.png")
print(driver.title)
dt = datetime.datetime.fromtimestamp(time.time())
print(dt)
for i in range(1000):
    driver.get("https://x.com/")
    print(driver.title)
    dt = datetime.datetime.fromtimestamp(time.time())
    message = "hello ra"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()

    time.sleep(60)
    print(i)
    
    print(dt)



driver.quit()
