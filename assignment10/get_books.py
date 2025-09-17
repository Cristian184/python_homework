from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json

# Task 3

driver = webdriver.Chrom(service=ChromeService(ChromeDriverManager().install()))

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

li = driver.find_elements(By.CSS.SELECTOR, "li.cp-search-result-item")

results = []

for entry in li:
    title = entry.find_element(By.CSS_SELECTOR, "span.title-content")
    titles = title.text.strip()
    print("Title:", titles)

    author = entry.find_elements(By.CSS_SELECTOR, "span.cp=author-link")
    authors = []
    for a in author:
        authors.append(a.text.strip())
    author2 = "; ".join(authors)
    print("Author;", author2)

    format = entry.find_element(By.CSS_SELECTOR, "div.cp-format-info")
    year = format.text.strip()
    print("Format-Year:", year)

    results.append({
        "Title": titles,
        "Author": author2
        "Format-Year": year
    })

df = pd.DataFrame(results)
print(df)

# Task 4

df.to_csv("get_books.csv", index = False)

with open("get_books.json:", "w") as f:
    json.dump(results, f, indent = 4)