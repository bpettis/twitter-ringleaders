from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import csv

# Set up input/output files here:
input_filename = 'data/testfile.csv' # don't forget that file paths will be relative to the current working directory when the script is ran
output_filename = 'output/testoutput.csv'


def main():
    print(f'Now checking usernames from {input_filename}')
    print(f'Results will be saved to {output_filename}')

    # Create an output file
    setup_output(output_filename)

    # Create a selenium driver
    headlesschrome = setup_selenium()

    # Read from an input file
    with open(input_filename) as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            username = row[1]
            print(f'Checking {username}') # print contents of column 2
            url = 'https://twitter.com/' + username # concatenate a URL to the twitter profile
            page_text = load_page(headlesschrome, url) # open the twitter profile and get the page source
            status = search_page(page_text) # guess the user status by searching for text on the page
            write_output(output_filename, username, status)

    

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

    status = 'error' # set a default status if nothing is found

    for term in terms:
        if (term[0] in page):
            print(f'{term[1]} : "{term[0]}" was found in page')
            status = term[1]
        else:
            print(f'"{term[0]}" was NOT found in page')
    
    return status


def setup_output(file):
    with open (file, 'w') as outfile:
        row = ['username', 'status']
        w = csv.writer(outfile)
        w.writerow(row)

def write_output(file, username, status):
    with open (file, 'a') as outfile:
        row = [username, status]
        w = csv.writer(outfile)
        w.writerow(row)

if __name__ == '__main__':
    startTime = datetime.now()
    print(f'Started at {startTime}')

    main()

    endTime = datetime.now()
    totalTime = endTime - startTime
    print(f'Ended at {endTime}, a total of {totalTime}')