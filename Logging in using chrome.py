import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#  ---------- EDIT ----------
email = '---\n' # replace email
password = '---\n' # replace password
#  ---------- EDIT ----------

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/ServiceLogin?service=accountsettings&continue=https://myaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button'
driver.get(url)


wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(password)
time.sleep(10)
driver.get("http://www.youtube.com")
time.sleep(10)
print("You're in!! enjoy")
