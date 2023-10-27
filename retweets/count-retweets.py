import csv, argparse
from datetime import datetime
import pandas as pd

# Setup command line arguments:
argParser = argparse.ArgumentParser(description='''
**Twitter Retweet Counts **


This silly little program takes an input CSV file containing tweets along with a list of usernames.
It outputs a secondary CSV file with details of how frequently each of the specified user tweeted, how frequently their tweets were retweeted, and what the most retweeted post was
It's a great way to understand trends of Twitter activity
    
Created by Ben Pettis''',
    usage='''%(prog)s -i [input file] -o [output file]
run "%(prog)s --help" to view more information''',
    formatter_class=argparse.RawTextHelpFormatter
)
argParser.add_argument("-i", "--input", required=True, help="Path to the CSV file to read from")
argParser.add_argument("-o", "--output", required=True, help="Path to output the CSV file to")
argParser.add_argument("-l", "--user-list", required=True, type=str, help="Path to a TXT file containing a list of usernames")
argParser.add_argument("-t", "--tweet-column", type=int, default=2, help="Index of column in CSV which contains the Tweet Text. Start counting at 0! - (default value is 2)")

args = argParser.parse_args()


def get_users(filepath):
    input_file = open(filepath, "r")
    data = input_file.read()
    usernamelist = data.split("\n")
    input_file.close()
    print(f'Read {str(len(usernamelist))} usernames from {filepath}')
    return usernamelist

def setup_csv(filename):
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        row = ['username', 'rewteet_count', 'most_retweeted']
        writer.writerow(row)

def append_csv(filename, row):
    with open(filename, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)

def main():
    print(f'Reading data from {args.input}')

    # Get the CSV file and load it into a pandas dataframe
    df = pd.read_csv(args.input)
    print(f'Loaded dataframe with {df.size} rows')

    print(df)

    # Use arguments to determine which columns to read from:
    tweetColumn = df.columns[args.tweet_column]
    print(f'Reading tweets from column {args.tweet_column} - which is labelled "{tweetColumn}"')


    # Write headers for the output file
    print(f'Setting up {args.output} as output file')
    setup_csv(args.output)

    # Build a list of usernames:
    print(f'Reading list of usernames from {args.user_list}')
    usernames = get_users(args.user_list)

    # Loop through the list of usernames. For each of those:

    for user in usernames:
        print(f'Checking {user}')

    #   Search df for "RT @username" in the tweet column, and count
    
        retweet_prefix = "RT @" + user
        boolean_mask = df[tweetColumn].str.startswith(retweet_prefix, na=False)
        filtered_df = df.loc[boolean_mask]
        times_retweeted = len(filtered_df.index)
        print(f'@{user} was retweeted {str(times_retweeted)} times throughout the entire dataset')


    #   Find the top-retweeted post, and grab its ID and text content
        popular_tweet = filtered_df[tweetColumn].value_counts().nlargest(1)
        if len(popular_tweet) > 0:
            popular_tweet = popular_tweet.to_string()
            popular_tweet = popular_tweet.removeprefix('text\n') # remove the prefix
            popular_tweet = popular_tweet[:-5] # remove the trailing suffix
        else:
            popular_tweet = 'N/A'
        print(f'Their most popular tweet was: \n *** \n {popular_tweet} \n ***')


    #   Write all that information into the CSV file
        row = [user, times_retweeted, popular_tweet]
        append_csv(args.output, row)


if __name__ == '__main__':
    startTime = datetime.now()
    print(f'Started execution at {startTime}')
    main()
    endTime = datetime.now()
    totalTime = endTime - startTime
    print(f'Finished at {endTime} - a total of {totalTime}')