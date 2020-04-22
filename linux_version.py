import sys
import os
import time
from selenium import webdriver
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

USERNAME = "moodle_username"
PASSWORD = "moodle_password"


firefoxPath="/home/mattan/Downloads/geckodriver-v0.26.0-linux64/geckodriver"
if __name__ == "__main__":
	LINK = sys.argv[1]
	OUTNAME = f"{LINK.split('=')[1]}.mp4"
	if len(sys.argv) > 2:
		OUTNAME = f"{sys.argv[2]}.mp4"
	# try:
	url = f"https://huji.cloud.panopto.eu/Panopto/Podcast/Social/{LINK.split('=')[1]}.mp4"
	driver = webdriver.Firefox(executable_path=firefoxPath)
	driver.get("https://moodle2.cs.huji.ac.il/nu19/")
	driver.set_window_size(965, 691)
	element = driver.find_element(By.LINK_TEXT, "https://moodle2.cs.huji.ac.il/nu19")
	actions = ActionChains(driver)
	actions.move_to_element(element).perform()
	driver.find_element(By.ID, "login_username").click()
	driver.find_element(By.ID, "login_username").send_keys(USERNAME)
	driver.find_element(By.ID, "login_password").send_keys(PASSWORD)
	driver.find_element(By.CSS_SELECTOR, ".form-group > .btn").click()
	driver.get(LINK)
	driver.find_element(By.ID, "providerDropdown").click()
	dropdown = driver.find_element(By.ID, "providerDropdown")
	dropdown.find_element(By.XPATH, "//option[. = 'HUJI Moodle']").click()
	driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
	driver.find_element(By.ID, "PageContentPlaceholder_loginControl_externalLoginButton").click()
	driver.get(url)
	direct_link = driver.current_url
	driver.close()
	os.system(f"wget {direct_link} -O {OUTNAME}")

