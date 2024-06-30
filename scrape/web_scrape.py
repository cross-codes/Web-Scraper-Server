# web_scrape.py

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import re

URL: str = "https://www.nvidia.com/en-in/geforce/buy/"

options: webdriver.ChromeOptions = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser"
options.add_argument("--headless")
driver: webdriver = webdriver.Chrome(options)

driver.get(URL)
content_arr: list[WebElement] = driver.find_elements(
    By.CSS_SELECTOR, "div.text-center.lap-text-center.tab-text-center.mob-text-center"
)

gpu_names: list[str] = []
prices: list[str] = []

for content in content_arr:
    try:
        h3_element: WebElement = content.find_element(By.CLASS_NAME, "title")
        text: str = h3_element.text
        gpu_match: re.Match = re.search(r"(?<!Shop )\bGe\w+", text)
        if gpu_match:
            if len(gpu_names) > len(prices):
                prices.append("N/A")
            gpu_names.append(text)
        else:
            price_match: re.Match = re.search(r"Rs\. ([\d,]+)", text)
            if price_match:
                price_str = price_match.group(1)
                price_number = int(price_str.replace(",", ""))
                prices.append(price_number)
            elif len(gpu_names) > len(prices):
                prices.append("N/A")
    except NoSuchElementException:
        continue

# pylint: disable=bad-builtin
PRICE_MAP: dict = dict(map(lambda i, j: (i, j), gpu_names, prices))
