from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
import requests
 
chrome_options = Options()
 
 
# chrome_options.debugger_address = "localhost:9222"
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
driver.get("https://flexibook.boschassociatearena.com/home")
start_time = datetime.now()
timeout = timedelta(minutes=5)
# message = "Seat not booked, please act fast"
driver.execute_script("window.open('about:blank', '_blank');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://npz2kor:@stfs.bosch.com/adfs/ls/wia")
driver.switch_to.window(driver.window_handles[0])
 
print("Booking started at", start_time.strftime("%H:%M:%S"))
while True:
    if datetime.now() - start_time > timeout:
        print("Timeout reached, exiting...")
        break
    try:
        now = datetime.now()
        bookingtime = now.strftime("%H:%M:%S")
        driver.get("https://flexibook.boschassociatearena.com/home")
        cell = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//table//tr[4]//td[3]"))
        )
        cell.click()
        time.sleep(7)
        rect = driver.find_element(By.ID, "Location143-218")
        rect.click()
        print("Element clicked!")
        button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary')]")
        button.click()
        time.sleep(10)
        cell = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//table//tr[4]//td[3]"))
        )
        cell.click()
        print("seat booked at " , bookingtime)
        message = "SEAT BOOKED :)"
        break  # Exit loop once clicked
    except:
        print("Element not found, retrying...")
        time.sleep(1)  # Wait 1 second before retrying
 
 
# Keep browser open
# input("Press Enter to close...")
 
# Close the browser
# driver.quit()
