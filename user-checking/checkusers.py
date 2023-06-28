from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


filename = 'put/file/here.csv'

def main():
    print(f'Now checking usernames from {filename}')
    test_selenium()

def test_selenium():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://duckduckgo.com/")
    print(driver.current_url)
    driver.quit()



if __name__ == '__main__':
    startTime = datetime.now()
    print(f'Started at {startTime}')

    main()

    endTime = datetime.now()
    totalTime = endTime - startTime
    print(f'Ended at {endTime}, a total of {totalTime}')