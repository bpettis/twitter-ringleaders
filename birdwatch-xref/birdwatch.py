from datetime import datetime
import csv, psycopg2, os
from dotenv import load_dotenv, find_dotenv
from psycopg2 import pool


## set up some global variables: ##
load_dotenv(find_dotenv()) # load environment variables
db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_name = os.environ.get("DB_NAME")
db_password = os.environ.get("DB_PASS")

header = ['tweet_id', 'user', 'text', 'birdwatch', 'total_notes', 'note_id', 'note_text', 'url']

## postgres connection:
def connection_pool():
    try:
        pool = psycopg2.pool.SimpleConnectionPool(1, 10,
            user=db_user,
            password=db_password,
            host=db_host,
            port="5432",
            database=db_name)
        return pool
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
        quit()



def output_setup():
    with open('output_birdwatch-xref.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)

def write_no_birdwatch(id, user, text):
    row = [id, user, text, 'false', '0', '', '', '']
    with open('output_birdwatch-xref.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def write_yes_birdwatch(id, user, text, count):
    print(f'Getting all Birdwatch notes for Tweet {id}')
    connection = db.getconn()
    cursor = connection.cursor()
    cursor.execute('SELECT "noteId", "summary" FROM notes WHERE "tweetId" = ' + id + ';')
    notes = cursor.fetchall()
    for note in notes:
        row = [id, user, text, 'true', count, note[0], note[1], 'https://birdwatcharchive.org/notes/' + str(note[0])]
        with open('output_birdwatch-xref.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)
    cursor.close()
    db.putconn(connection)

def check_birdwatch(tweet_id):
    print(f'Checking Tweet {tweet_id} for Birdwatch notes')
    connection = db.getconn()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT COUNT(*) FROM notes WHERE "tweetId" = ' + tweet_id + ';')
        count = cursor.fetchone()
    except:
        print('Error when querying db')
        return 0
    cursor.close()
    db.putconn(connection)
    return count[0]

def main():
    output_setup()

    file = open('data/ZackSnyderJusticeLeague.csv')
    lines = csv.DictReader(file)
    for line in lines:
        tweet = line['\ufeffid_str']
        count = check_birdwatch(tweet)
        if count == 0:
            write_no_birdwatch(tweet, line['from_user'], line['text'])
        else:
            write_yes_birdwatch(tweet, line['from_user'], line['text'], count)
    file.close()



if __name__ == "__main__":
    start_time = datetime.now()
    print(f'FYI: Script started directly as __main__ at {start_time}')
    db = connection_pool()
    main()

    # close the db connection pool:
    if db:
        db.closeall
        print("PostgreSQL connection pool is closed")
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f'Finished at {end_time}')
    print(f'Total execution was: {total_time}')