# ad-scraper
Python ad scraper using Selenium

Why Selenium? Scraping ads may require a "user interaction" that could not be done with other scraping libraries like BeautifulSoup

Dependencies/To-Run:

Python 3

Download Selenium at https://pypi.org/project/selenium/ or use "pip install selenium"

Selenium requires a web driver, I used ChromeDriver. Go to  https://chromedriver.chromium.org/ and select the latest stable release of your operating system. Make sure that your version of chrome is also up to date.

---------------------------------

After using selenium to access a social media account on Instagram or Facebook, the scraper can perform two actions…

Search add keywords in a specific niche or scroll through the accounts feed collecting ad targeted to the account.

The account is currently pre-created to follow a specific niche, (e.g., skincare, makeup, jewelry, pet supplies). In the future I will be automating this process as well.

The collected information is then stored locally in an excel file.





