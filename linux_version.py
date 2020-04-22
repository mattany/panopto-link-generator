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


def download_file(link,out=None):
	if out is None:
		out_name = f"{LINK.split('=')[1]}.mp4"
	else:
		out_name = out
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
	os.system(f"wget {direct_link} -O {out_name}")


if __name__ == "__main__":
	LINK = sys.argv[1]
	if os.path.isfile(LINK):
		with open(LINK, "r") as f:
			for i, line in enumerate(f.readlines()):
				if sys.argv[2]:
					download_file(line, f"{sys.argv[2]}_{i}.mp4")
				else:
					download_file(line, f"file{i}.mp4")
	elif len(sys.argv) > 2:
		output = f"{sys.argv[2]}.mp4"
		download_file(LINK, output)

