**🚀 Yahoo Finance Stock Scraper & Data Cleaning**

**📌 About this Project :**

This project involves scraping the most active stocks from Yahoo Finance, followed by data ingestion and cleaning to ensure structured and meaningful stock data.

Yahoo Finance is a widely used financial platform that provides real-time stock data, financial news, and market trends. In this project, we automate the extraction of most active stocks, process the data, and clean it for further analysis.

🔄 Project Workflow :

1️⃣ Web Scraping: Extracting Stock Data

Automate the process of extracting stock market data from Yahoo Finance using a web scraper:

1. Open a web browser and maximize the window.

2. Initialize an explicit wait for stable web interactions.

3. Navigate to Yahoo Finance (https://finance.yahoo.com/) and wait for the page to load.

4. Hover over the Markets menu.(Highlighed with yellow)

![image](https://github.com/user-attachments/assets/2f61be63-e2c9-4c36-a32f-d7cd98bcee20)

5. Click on Trending Tickers.

6. Select the Most Active stocks section.(Highlighed with yellow)

![image](https://github.com/user-attachments/assets/8fb80d8d-2460-42b1-b979-f7db4853beff)

7. Extract stock data (e.g., ticker, price, volume, market cap, etc.).

8. Navigate through all pages to ensure full data collection.

9. Store the extracted data in a structured format (list or DataFrame) and finally into CSV file.

10. Close the browser.

2️⃣ Data Ingestion: Storing Raw Data

After scraping, the raw stock data needs to be stored efficiently for further processing. The steps include:

1. Save the extracted stock data as a CSV file (raw_stocks_details.csv).

2. Implement error handling to ensure smooth file storage.

3. Log the success or failure of data ingestion.

3️⃣ Data Cleaning: Processing Extracted Data

Once we have the raw stock data, we perform the following cleaning steps:

1. Standardize column formats (strip unnecessary spaces, remove special characters, etc.).

2. Convert object columns to proper data types:

3. Remove symbols like + and % from percentage change.

4. Convert large volume numbers into one single unit (e.g., M for millions, B for billions).

5. Export the cleaned data as cleaned_stocks_details.csv.

6. Log each step to track data processing status.

**📁 Project Structure :**

![image](https://github.com/user-attachments/assets/a19bdf52-bc4d-4493-a601-f57ab7018e41)

**Conclusion**

This project automates the process of extracting, storing, and cleaning stock data from Yahoo Finance, making it ready for analysis or further processing. 
By structuring and standardizing the stock data, we ensure consistency and accuracy in financial insights.
