🚀 Cryptocurrency Price Tracker

A Python-based web automation project that scrapes real-time cryptocurrency prices and market data from CoinMarketCap using Selenium and stores the data in a CSV file for analysis and trend tracking.

📌 Key Features

🔹 Scrapes live cryptocurrency prices

🔹 Extracts Top 10 coins data

🔹 Captures Coin Name, Price, 24h Change, Market Cap

🔹 Supports Headless browser mode

🔹 Exports data to CSV file

🔹 Historical logging with timestamp

🔹 Custom price filtering option

🔹 Ready for dashboard or data analysis integration

⚙️ Technologies Used

Python

Selenium

pandas

webdriver_manager

Google Chrome (ChromeDriver)

🔄 Working Steps

The script launches Chrome using Selenium WebDriver.

It opens the CoinMarketCap homepage.

The page loads dynamically rendered cryptocurrency data.

The program extracts details of the top 10 cryptocurrencies.

The extracted data is stored in a pandas DataFrame.

A timestamp is added for historical tracking.

The data is saved or appended to a CSV file.

The browser closes automatically after execution.

📊 Output

Generates crypto_prices.csv file

Stores real-time market data with timestamp

Appends new data on every run
