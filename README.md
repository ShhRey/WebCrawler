# Web Scraping and Automation with Python

## Overview
This repository contains Python code showcasing the evolution of a web scraping project, starting from basic data extraction using BeautifulSoup to building a versatile web crawler with automation capabilities using Selenium. The project gradually progresses to data storage in MongoDB and concludes with an automated data filler for social media accounts.

## Table of Contents
1. **Introduction**
   As a beginner in web scraping, this project documents my learning journey and the progression of techniques used to extract and manipulate data from various websites.

2. **Listing and Installing Dependencies**
  a. Python 3.x
  b. BeautifulSoup
  c. Selenium
  d. MongoDB
  e. pymongo

  2.1 Installing the Dependencies
  ```bash
  pip install beautifulsoup4 selenium pymongo
  ```

3. **Project Structure**
   The project is organized into different stages, each representing a milestone in the learning process. The structure is as follows:
    ├── bs4_extraction
    ├── selenium_scraping
    ├── mongodb_integration
    ├── versatile_web_crawler
    ├── social_media_automation
   
4. **Web Scraping with BeautifulSoup**
   In the initial stage, the project focuses on extracting data from a specific website (Coingecko) using the BeautifulSoup library. The extracted data is displayed using arrays to make it more readable.
   
5. **Advancing to Selenium**
   Recognizing the limitations of BeautifulSoup, the project transitions to using Selenium for web scraping. It includes examples of scraping data from pages that require loading more data dynamically. The code demonstrates proficiency in handling dynamic content.
   
6. **Data Storage in MongoDB**
  Building on the knowledge gained, the project introduces MongoDB integration. Data scraped using Selenium is now stored in a MongoDB database. The code includes URI connection and usage of the pymongo library.

7. **Versatile Web Crawler**
  The web crawler developed in this stage is capable of scraping data from any given website. It simplifies the extracted data and stores it in MongoDB. The crawler is designed to update existing data if newer information is found, while preserving the old data.
   
8. **Automation for Social Media**
   The final stage involves creating an automated data filler for social media accounts. The code assists in creating accounts using information provided within the script. It showcases automation skills beyond web scraping.


## How to Add Chrome WebDriver for Selenium

To use Selenium for web scraping, you need to download the Chrome WebDriver. Follow the steps below to add Chrome WebDriver to your project:

1. **Check Your Chrome Browser Version:**
   - Open Chrome.
   - Click on the three dots in the top-right corner.
   - Go to "Help" > "About Google Chrome."
   - Note the version number.

2. **Download Chrome WebDriver:**
   - Visit the [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/) page.
   - Download the version of ChromeDriver that matches your Chrome browser version.

3. **Extract the Chrome WebDriver:**
   - Extract the downloaded ZIP file to get the `chromedriver.exe` file.

4. **Place the Chrome WebDriver in Your Project Directory:**
   - Copy the `chromedriver.exe` file to the directory where your Selenium script is located.

Now, you are ready to use Selenium with Chrome WebDriver in your project.

```python
# Example Selenium script using Chrome WebDriver
from selenium import webdriver

# Specify the path to the chromedriver.exe file
chrome_path = './chromedriver.exe'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_path)
```



### Additional Information
Feel free to explore for detailed code and examples associated with each stage of the project. Happy coding!
