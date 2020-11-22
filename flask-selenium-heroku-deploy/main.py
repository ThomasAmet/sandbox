# Git commands to push on differents remotes
# git push origin master # push to Github, origin is the branch in github master is the branch in local
# git push heroku master # push to Heroku
# git remote add origin https://github.com/ThomasAmet/sandbox/flask-selenium-heroku-deploy.git
# git remote remove origin


# Import required packages
from selenium import webdriver
import os

# Set url to scrap
url = "https://www.google.com"

# Set webdriver options
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

# Initiate webdriver
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
driver.get(url)
print(driver.page_source)