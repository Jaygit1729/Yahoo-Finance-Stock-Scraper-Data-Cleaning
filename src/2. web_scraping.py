from logger_utils import setup_logger
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# Initialize Logger

logger = setup_logger("logs/web_scraping")
logger.info("Logging has been set up successfully for web_scraping modules")

def initialize_driver():

    """Initialize the webdriver object"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def wait_for_page_to_load(driver,wait):

    """Wait for the page to fully load"""
    try:
        wait.until(lambda d:d.execute_script("return document.readySate")== 'complete')
        logger.info(f"Page {driver.title} loaded successfully")
    except:
        logger.info(f"Page {driver.title} not loaded within given time")

def navigating_to_trending_tickers(driver,wait):

    """Navigate to the trending tickers section"""
    actions = ActionChains(driver)
    market_menu = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/header/div/div/div/div[4]/div/div/ul/li[3]/a/span')))
    actions.move_to_element(market_menu).perform()

    trending_ticker = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/trending-tickers')]")))
    trending_ticker.click()
    wait_for_page_to_load(driver,wait)

def navigate_to_most_active(driver,wait):

    """Navigate to the most active stocks section"""
    most_active = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Most Active']")))
    most_active.click()

    try:
        section_title = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/main/section/section/section/article/section/div/nav/ul/li[1]/a/span')
        )).text
        logger.info(f"Page {section_title} loaded successfully")
    except:
        logger.info("Could not find the Most Active page title.")

def scrape_stock_data(driver,wait):

    """Scrape stock data from the Most Active stocks page"""

    data = []
    counter = 0
    while True:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        rows = driver.find_elements(By.CSS_SELECTOR,"table tbody tr")

        for row in rows:

            stock_details = row.find_elements(By.TAG_NAME,"td")
            most_active_stocks = [data.text for data in stock_details]

            stocks = {
                "Company_Name": most_active_stocks[1],
                "Symbol": most_active_stocks[0],
                "Price": most_active_stocks[3],
                "Change": most_active_stocks[4],
                "Change_in_pct": most_active_stocks[5],
                "Volume": most_active_stocks[6],
                "Avg_Vol_Per_3M": most_active_stocks[7],
                "Market_Cap": most_active_stocks[8],
                "PE_Ratio": most_active_stocks[9],
            }
            data.append(stocks)
        
        # Check for Next Button
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div/div[3]/div[3]/button[3]')))
        except:
            logger.info("The next_button is not clickable anymore. We have scraped the data from all the pages!")
            break
        
        next_button.click()
        time.sleep(2)
        counter += 1
        logger.info(f"Successfully Scraped the Most Active Stock data from the page: {counter}")
    
    return data


def main():

    """Main function to execute the web scraping process"""
    
    logger.info("Starting Yahoo Finance Web Scapper...")
    driver = initialize_driver()
    wait = WebDriverWait(driver, 5)

    try :
        driver.get('https://finance.yahoo.com/')
        wait_for_page_to_load(driver,wait)
        navigating_to_trending_tickers(driver,wait)
        navigate_to_most_active(driver,wait)
        data = scrape_stock_data(driver, wait)
        stocks_df = pd.DataFrame(data)
        stocks_df.to_csv("data/raw_stocks_details.csv", index= False)
        logger.info(f"Scrapped Data from the Yahoo Finance has been saved successfully to raw_stocks_csv file!")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

