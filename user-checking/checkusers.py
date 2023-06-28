from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Set up input/output files here:
input_filename = 'put/file/here.csv'
output_filename = 'put/file/here-out.csv'


def main():
    print(f'Now checking usernames from {input_filename}')

    headlesschrome = setup_selenium()


    url = 'https://example.com'
    page_text = load_page(headlesschrome, url)

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
    terms = [['Automated by </span>', 'bot'], # Means that the account is likely labelled as a bot account by its owner
             ['This account doesn’t exist</span>', 'deleted'], # Means that the account is deleted, or never existed to start with
             ['Twitter suspends accounts that violate the Twitter Rules. </span>', 'suspended'], # Means there is a message about account being suspended
             ['Follow</span>', 'active'] # Means the account likely exists and is not deleted - because it has an active follow button
            ]

    for term in terms:
        if (term[0] in page):
            print(f'{term[1]} : "{term[0]}" was found in page')
        else:
            print(f'"{term[0]}" was NOT found in page')




if __name__ == '__main__':
    startTime = datetime.now()
    print(f'Started at {startTime}')

    main()

    endTime = datetime.now()
    totalTime = endTime - startTime
    print(f'Ended at {endTime}, a total of {totalTime}')