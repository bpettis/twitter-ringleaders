from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


filename = 'put/file/here.csv'

def main():
    print(f'Now checking usernames from {filename}')

    headlesschrome = setup_selenium()


    url = 'https://example.com'
    page_text = load_page(headlesschrome, url)
    print(page_text)

    search_page(page_text)

    # Quit/Close the headless chrome browser
    if headlesschrome: 
        headlesschrome.quit()

def setup_selenium():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://example.com")
    print(f'Loaded: {driver.current_url}')
    return driver

# load a specified URL and return the page source as text
def load_page(driver, url):
    driver.get(url)
    return driver.page_source

def search_page(page):
    term = 'Example'
    # print True if text is present else False
    print(term in page)




if __name__ == '__main__':
    startTime = datetime.now()
    print(f'Started at {startTime}')

    main()

    endTime = datetime.now()
    totalTime = endTime - startTime
    print(f'Ended at {endTime}, a total of {totalTime}')