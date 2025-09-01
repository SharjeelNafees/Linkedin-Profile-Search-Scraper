import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Enable headless mode (no browser popup)
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Launch browser
driver = webdriver.Chrome(options=options)

# Step 1: Open DuckDuckGo
driver.get("https://duckduckgo.com/")
time.sleep(2)

# Step 2: Search for LinkedIn profiles
search_query = '"email oil executives in USA" site:linkedin.com'
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Step 3: Collect search results
results = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")

data = []
for r in results[:15]:  # get top 15 results
    data.append({"title": r.text, "link": r.get_attribute("href")})

# Step 4: Save to Excel
df = pd.DataFrame(data)
df.to_excel("linkedin_search_results.xlsx", index=False)

print("📊 Search results saved to linkedin_search_results.xlsx")

driver.quit()
