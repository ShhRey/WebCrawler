from selenium import webdriver                                                                      # Monitor Browser Activities
from selenium.webdriver.chrome.options import Options                                               # Keep Browser Open after Script Execution
from selenium.webdriver.common.by import By                                                         # Filter/Search Webpage Elements
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_experimental_option("detach", True)
path = "D:\\webdrivers\\chromedriver.exe"                                                           # WebDriver File Path
fbURL = "https://www.facebook.com/"                                                       # URL you want to Scrape
driver = webdriver.Chrome(executable_path=path, options=options)         
driver.get(url=fbURL)
driver.implicitly_wait(30)

try:
    create_acc_button = driver.find_element(By.XPATH, "//*[text()='Create new account']").click()
    time.sleep(3)

    # Take User Inputs
    fname = driver.find_element(By.NAME, 'firstname').send_keys("Nisha")
    lname = driver.find_element(By.NAME, 'lastname').send_keys("Yadav")
    email = driver.find_element(By.NAME, 'mailto:reg_email__').send_keys('nishayadav2000@gmail.com')
    conf_email = driver.find_element(By.NAME, 'mailto:reg_email_confirmation__').send_keys('nishayadav2000@gmail.com')
    password = driver.find_element(By.NAME, "reg_passwd__").send_keys("nisha1666910")
    # bday = Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
    bday = Select(driver.find_element(By.NAME, "birthday_day"))
    bday.select_by_visible_text("6")
    bmonth = Select(driver.find_element(By.NAME, "birthday_month"))
    bmonth.select_by_visible_text('Jun')
    byear = Select(driver.find_element(By.NAME, "birthday_year"))
    byear.select_by_visible_text('2000')
    gender = driver.find_element(By.XPATH, "//label[text() = 'Female']").click()
    signup_button = driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    time.sleep(3)
    exist_acc = driver.find_element(By.XPATH, "//*[text()='No, Create New Account']").click()
    

except Exception as e:
    raise Exception('Wait time exceeded')