from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from datetime import datetime
import os

# ==============================
# SETTINGS
# ==============================

HEADLESS_MODE = False      # Change to True for background running
PRICE_FILTER = 0          # Example: 1000 (shows coins above $1000)
TOP_COINS = 10            # Number of coins to scrape

# ==============================
# BROWSER SETUP
# ==============================

chrome_options = Options()

if HEADLESS_MODE:
    chrome_options.add_argument("--headless")

chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# ==============================
# OPEN WEBSITE
# ==============================

driver.get("https://coinmarketcap.com/")
time.sleep(5)

rows = driver.find_elements(By.XPATH, "//table//tbody/tr")

data = []

for i in range(TOP_COINS):
    cols = rows[i].find_elements(By.TAG_NAME, "td")
    
    name = cols[2].text
    price = cols[3].text
    change_24h = cols[4].text
    market_cap = cols[7].text
    
    # Clean price for filtering
    clean_price = price.replace("$", "").replace(",", "")
    
    try:
        price_value = float(clean_price)
    except:
        price_value = 0

    # Apply price filter
    if price_value >= PRICE_FILTER:
        data.append([name, price, change_24h, market_cap])

driver.quit()

# ==============================
# CREATE DATAFRAME
# ==============================

df = pd.DataFrame(data, columns=[
    "Coin Name",
    "Price",
    "24h Change",
    "Market Cap"
])

# Add Timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df["Timestamp"] = current_time

# ==============================
# SAVE (APPEND MODE)
# ==============================

file_name = "crypto_prices.csv"

if os.path.exists(file_name):
    df.to_csv(file_name, mode='a', header=False, index=False)
else:
    df.to_csv(file_name, index=False)

print("Data successfully saved and updated!")
